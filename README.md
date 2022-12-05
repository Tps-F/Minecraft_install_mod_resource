# Minecraft_Install_mod_resource

Automatically install any mod and resource to Minecraft

# Required Warnings
## This project is still incomplete.

There may still be areas in this code that can be improved. Please note that there may be changes in the future.

## OS

This code currently works only on windows.

## Copyright notices

This code is distributed under the GPL. The author assumes no responsibility whatsoever for its use.



#  Distributor Preparation

Tips: You can use pyinstaller to make it an executable file.



## Set your mods and resource

This needs to be done only by those who distribute.

I may eventually write code to automate this part as well.

You need these two things.
```
1. open %appdata%\.minecraft\
2. zip the mods folder.

3. open %appdata%\.minecraft\resourcepacks 
```
* These two zip files can be raised to the cloud for easier management.
* Set the mods.url and resource_url in install_mods_resource.py


## Make Executable File
If you want to distribute the software as an executable file, please follow this procedure.

### Install Library
Open cmd and run to install requests.
```
pip install pyinstaller
``` 
And run command
```
pyinstaller install_mod_resource.py --onefile
```
This will generate install_mod_resource.py in the dist folder and You can release this.
# User Preparation
If you get Executable File, Just open it.
## Install library(Not Executable File)

Open cmd and run to install requests.
```
pip install requests
``` 

The other libraries are standard ones.

And run
```
python instlal_mod_resource.py
```

# Possible Errors
The ones made executable by pyinstaller are sometimes recognized as viruses.
You need to build the Bootloader and replace files.
![image](https://user-images.githubusercontent.com/63702646/205706644-1940e86a-333e-404d-81ec-f597af9c49f8.png)


Infomation: https://pyinstaller.org/en/stable/bootloader-building.html
