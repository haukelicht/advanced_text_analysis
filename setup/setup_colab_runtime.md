# Connect to a GPU runtime in Google Colab

Some notebooks run much faster with a GPU. Follow these steps to switch your Colab runtime to a GPU before running the notebook.

## 1. Open the Runtime menu

In your open Colab notebook, click **Runtime** in the menu bar.

<img src="./imgs/colab/01-menu_runtime.png" alt="Runtime menu in Colab" style="width:400px;"/>

## 2. Choose "Change runtime type"

From the dropdown, click **Change runtime type**.

<img src="./imgs/colab/02-change_runtime.png" alt="Change runtime type option" style="width:250px;"/>

## 3. Select the GPU hardware accelerator

In the dialog that appears, select **T4 GPU** under **Hardware accelerator**, then click **Save**.

<img src="./imgs/colab/03-choose_gpu.png" alt="Select T4 GPU hardware accelerator" style="width:350px;"/>

## 4. Reconnect and run your notebook

Colab will reconnect using the new runtime. Run your notebook cells as usual — they will now execute on the GPU.
