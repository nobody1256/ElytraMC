import time 

import os

import shutil 

from pathlib import Path

import requests

import socket

import subprocess

from optparse import OptionParser

import argparse

chk_file = Path("ElytraSettings/install.txt")

if chk_file.is_file():
    print("Server not installed! Installing now...")
    
    print("Downloading BDS")
 
    get = "https://minecraft.azureedge.net/bin-win/bedrock-server-1.19.1.01.zip"
 
    r = requests.get(get, allow_redirects=True)
 
    open('bedrock-server-1.19.1.01.zip', 'wb').write(r.content)
 
    shutil.unpack_archive('bedrock-server-1.19.1.01.zip')
 
    print("Install Complete! Starting...")
 
    os.remove(chk_file)
    delete = "bedrock-server-1.19.1.01.zip"
    os.remove(delete)
 
    print("[Server] Server marked as installed")
else:
 
    print("[Server] Server already marked as installed! Starting")



subprocess.Popen('bedrock_server.exe', shell=True)


def cont ():
    print("continue")


startmsg = "Finding mods..."

print("Starting Elytra...")

time.sleep(0.5)

try: 
    os.mkdir('mods') 
except OSError as error: 
    print(error)

try: 
    os.mkdir('Logs') 
except OSError as error: 
    print(error)

try: 
    os.mkdir('info') 
except OSError as error: 
    print(error)

try: 
    os.mkdir('ElytraSettings') 
except OSError as error: 
    print(error)




print("Folder check Complete...")



def install ():
    get = "https://minecraft.azureedge.net/bin-win/bedrock-server-1.19.1.01.zip"
    r = requests.get(get, allow_redirects=True)
    open('bedrock-server-1.19.1.01.zip', 'wb').write(r.content)
    shutil.unpack_archive('bedrock-server-1.19.1.01.zip')


print("[Server] Type help for commands")

print(startmsg)

chk_file2 = Path("mods/resource_packs/pack")

if chk_file2.is_file():
    rfrom = "mods/resource_packs/pack"
    rto = "worlds/world/behavior_packs"
    shutil.move(rfrom, rto)

else:
    print("[Server] No resource packs detected")


chk_file3 = Path("mods/behavior_packs/pack")
if chk_file3.is_file():
    modfrom = "mods/behavior_packs/pack"
    modto = "worlds/world/resource_packs"
    shutil.move()

else:
    print("[Server] No Behavior packs detected")


chk_file9 = Path("temp/Enter_beta.txt")

if chk_file9.is_file():
    print("==================================================================")
    print("|                         Elytra (V1.0)                          |")
    print("|                             (Beta)                             |")
    print("|             Leave the beta by removeing Enter_beta.txt         |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("==================================================================")
else:
    time.sleep(3)
    print("==================================================================")
    print("|                         Elytra (V1.0)                          |")
    print("|          To enter the beta versions of elytra make a file      |")
    print("|                   called Enter_beta.txt in temp                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("==================================================================")

chk_file3 = Path("behavior_packs/vanilla_1.19.0/biomes/cold_taiga_hills.biome.json")

if chk_file3.is_file():
    cont 
else:
    print("[Server] Error behavior_packs folder is missing and is needed to start the server!")
    time.sleep(4)
    print("Stopping server...")
    time.sleep(2)
    exit()

chk_file3 = Path("resource_packs/vanilla/blocks.json")

if chk_file3.is_file():
    cont 
else:
    print("[Server] Error Resource_packs folder is missing and is needed to start the server!")
    time.sleep(4)
    print("Stopping server...")
    time.sleep(2)
    exit()

time.sleep(0.5)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


s.connect(("8.8.8.8", 80))

print("Joinable IP: ",s.getsockname()[0])
s.close()





