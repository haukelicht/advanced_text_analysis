# Hugging Face Pro account and access token

## 1. Create or sign in to a Hugging Face account

Go to [Hugging Face](https://huggingface.co/login) and sign in or create an account.

## 2. Upgrade to a PRO subscription

1. Click your profile avatar in the top-right corner of the page.
2. Open **Settings**.

<img src="./imgs/hugging_face_pro/02-go_to_settings.png" alt="Open settings from the profile menu" style="width:400px;"/>

3. In the settings menu, click **Billing**.

<img src="./imgs/hugging_face_pro/03-settings_popup.png" alt="Settings menu with billing entry" style="width:250px;"/>

4. In the billing page, open the **Subscriptions** tab.
5. If you do not yet have PRO, click the option to upgrade to **PRO** and complete the payment flow.
6. If your account already shows a **PRO subscription active**, you can continue with the next step.

<img src="./imgs/hugging_face_pro/04-go_to_billing.png" alt="Billing page" style="width:400px;"/>

<img src="./imgs/hugging_face_pro/05-go_to_subscriptions.png" alt="Subscriptions tab with PRO subscription" style="width:400px;"/>

## 3. Create an access token

1. Open the profile menu again and choose **Access Tokens**.

<img src="./imgs/hugging_face_pro/07-go_to_access_tokens.png" alt="Access Tokens entry in the profile menu" style="width:250px;"/>

2. Click **Create new token**.
3. Select token type **Read**.
4. Enter a token name.
5. Click **Create token**.

<img src="./imgs/hugging_face_pro/08-click_create_new_token.png" alt="Create new token button" style="width:400px;"/>

<img src="./imgs/hugging_face_pro/09-create_new_read_token.png" alt="Create a new read token" style="width:350px;"/>

6. Copy the token immediately and store it somewhere safe. You will only see it once.

<img src="./imgs/hugging_face_pro/10-copy_token.png" alt="Copy the access token" style="width:400px;"/>

## 4. Make the token accessible in VS Code

1. Create a file called `.env` in the root of your project folder. (It is important that the file name starts with a dot.)
2. Open the file in a text editor.
3. Add `HF_TOKEN=` on the first line.
4. Paste your Hugging Face token after the `=` sign.
5. Save the file and close it.

<img src="./imgs/hugging_face_pro/11-add_token_to_dotenv.png" alt="Add the token to a .env file" style="width:400px;"/>
