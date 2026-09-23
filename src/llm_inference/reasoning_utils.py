from huggingface_hub import hf_hub_download
import json
import jinja2.meta as meta
from transformers.utils.chat_template_utils import _compile_jinja_template

def determine_reasoning_ability(model_name_or_path):
    """
    Determine if the model's tokenizer has a "thinking" token and extract reasoning-related template variables from its chat template.

    Args:
        model_name_or_path (str): The name or path of the model on Hugging Face Hub.

    Returns:
        has_thinking_token (bool): True if the tokenizer has a "thinking" token, False otherwise.
        template_reasoning_vars (list): List of reasoning-related template variables.
    """

    # (down)load model's chat template template from hugging face cache/hub (if exists)
    tokenizer_config_path = hf_hub_download(repo_id=model_name_or_path, filename="tokenizer_config.json")
    with open(tokenizer_config_path, "r") as fp:
        tokenizer_config = json.load(fp)

    has_thinking_token = None
    if 'additional_special_tokens' in tokenizer_config:
        has_thinking_token = any('thinking' in tok for tok in tokenizer_config['additional_special_tokens'])

    template_reasoning_vars = None
    if 'chat_template' in tokenizer_config:
        chat_template = tokenizer_config['chat_template']
        # Private Transformers helper: its API may change between versions.
        compiled = _compile_jinja_template(chat_template)
        syntax_tree = compiled.environment.parse(chat_template)

        variables = meta.find_undeclared_variables(syntax_tree)

        # get reasoning/thinking related template variables (if any)
        template_reasoning_vars = [v for v in variables if any(s in v for s in ('think', 'reason'))]

    return has_thinking_token, template_reasoning_vars

def validate_chat_template_kwargs(model_name_or_path, chat_template_kwargs):
    """
    Validate user-provided chat template kwargs against the model's reasoning variables

    Args:
        model_name_or_path (str): The name or path of the model on Hugging Face Hub.
        chat_template_kwargs (dict): User-provided chat template keyword arguments.

    Returns:
        dict: Validated chat template keyword arguments.

    Raises:
        ValueError: If invalid chat template kwargs are provided.
    """
    has_thinking_token, template_reasoning_vars = determine_reasoning_ability(model_name_or_path)
    if template_reasoning_vars is None:
        print(f"WARNING: Cannot validate chat template kwargs because the model's chat template reasoning variables could not be parsed.")
        return chat_template_kwargs

    chat_template_issue = False
    for k in chat_template_kwargs.keys():
        if k not in template_reasoning_vars:
            chat_template_issue = True
            print(f"WARNING: {k} is not a chat template variable.")
    if chat_template_issue:
        if has_thinking_token is not None and not has_thinking_token:
            print(f"WARNING: Model does not have a thinking token. Check the model card at https://huggingface.co/models/{model_name_or_path} and check whether the model enables reasoning.")
        if len(template_reasoning_vars) > 0:
            print(f"INFO: Available reasoning-related chat template variables: {template_reasoning_vars}\n ")
        raise ValueError("Invalid chat template kwargs provided.")
    return chat_template_kwargs
