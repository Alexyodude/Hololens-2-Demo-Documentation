Download the [python 3.10.12 tarball](https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz) on the [3.10.12 python website](https://www.python.org/downloads/release/python-31012/)

Download [conda](https://www.anaconda.com/download)and open the conda powershell.

Then type in the conda powershell ,
```
conda create -n python310 python=3.10.12   
```

This will make a virtual environment where you can use python 3.10.12 in the PowerShell.

You can check your if you created your virtual environment by typing,
```
conda env list
```

You should see python310. Activate the environment by typing,
```
conda activate python310
```

This should change the (base) status on your left to (python310).

Go to the directory of your unity project and copy and pasting the directory to go there. It should look like this,
```
cd C:\Users\****\Unity\NameOfProject
```

Any spacing won't work on conda. If you can't do this then manually work up the directory by using the commands,
```
cd 
dir
```

"dir" will show you the directory in your current folder. Typing "cd" and the directory you want to go to will move you up to the directory, as an example, 
```
cd filename
```

You can also press tab which will cycle through your directory.

Before continuing in the unity project directory, clone/download the [ml-agents](https://github.com/Unity-Technologies/ml-agents) repository from Github. Open the folder of the cloned repository and copy the ml-agents and ml-agents-envs folder to your project directory "Unity/NameOfProject"

![[Pasted image 20240911110839.png]]

Then back in the conda powershell type,
```
python -m pip install --upgrade pip
pip3 install torch -f https://download.pytorch.org/whl/torch_stable.html
```

VERY IMPORTENT:
Go into /ml-agents/mlagents/torch_utils/torch.py and change the line of code to
```
def set_torch_config(torch_settings: TorchSettings) -> None:

    global _device

  

    if torch_settings.device is None:

        device_str = "cuda" if torch.cuda.is_available() else "cpu"

    else:

        device_str = torch_settings.device

  

    _device = torch.device(device_str)

  

    if _device.type == "cuda":

        torch.set_default_device(_device.type)

        #torch.set_default_dtype(torch.cuda.FloatTensor)

        torch.set_default_dtype(torch.float32)

    else:

        torch.set_default_dtype(torch.float32)

    logger.debug(f"default Torch device: {_device}")
```

Where we change line 56 in the file from torch.cuda.FloatTensor to torch.float32

Then type the order matters,
```
pip3 install -e ./ml-agents-envs
pip3 install -e ./ml-agents
```

After any changes inside ml-agents you will need to do the command again to build it.

Typing
```
mlagents-learn --help
```

Should prompt you with the Unity logo and then your done with the installation ctrl+c to exit the process.