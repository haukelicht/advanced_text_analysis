from pydantic import BaseModel
from huggingface_hub.inference._generated.types.chat_completion import (
    ChatCompletionInputResponseFormatJSONSchema, 
    ChatCompletionInputJSONSchema
)

def get_response_format(output_class: BaseModel, schema_name: str):
    schema = output_class.model_json_schema()
    json_schema = ChatCompletionInputJSONSchema(name=schema_name, schema=schema)
    response_format = ChatCompletionInputResponseFormatJSONSchema(type="json_schema", json_schema=json_schema)
    return response_format
