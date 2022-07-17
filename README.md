# ElytraMC
Minecraft Bedrock server software based of BDS

# OS Info
Elytra supports both Windows and Linux however on linux (Ubuntu only) you have to build it from source (scroll all the way down) or use the install script (coming soon)!



# Features
More features coming soon!
Current features:
+ Easy installation of mods (work in progress)
+ Says your IP to join
+ Custom commands
+ Will not edit your world in any way (except for adding mods)



# Notes:
+ If you open Bedrock_server.exe elytra will not pack your mods inside your worlds and non of the stuff that elytra does will 
work so try not to open bedrock_server.exe! <strong> So make sure you open Server.exe instead! </strong>

# installation
go to Releases> V1.3 > click Elytra.V1.3.zip > Unzip > Open Server.exe

# Custom commands:
Elytra has custom commands only available from the console if the command 
failes the first time try again until it works.
 






Commands:

+ elytra sys (tells info about your system)
+ elytra mods (lists mods)
+ elytra worlds (lists worlds)
+ elytra info (info about elytra)
+ elytra kill (force kill the server)

# Build from source (Linux):

``` apt install python
 pip install requests
 apt install unzip
 wget "https://github.com/nobody1256/ElytraMC/archive/refs/heads/main.zip"
 unzip filename.zip
 ./server.py


