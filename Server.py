import time 

import os

import shutil 

from pathlib import Path

import requests

import socket

import subprocess

#from jproperties import Properties

import argparse

from zipfile import ZipFile

import json

version = "1.4"


chk_file = Path("ElytraSettings/install.txt")

if chk_file.is_file():
    print("Server not installed! Installing now...")
    print("What os are you using? (windows or linux)")
    s = input()
    if s == "windows" :
        print("Downloading BDS")
    
        get = "https://minecraft.azureedge.net/bin-win/bedrock-server-1.19.10.03.zip"
    
        r = requests.get(get, allow_redirects=True)
    
        open('bedrock-server-1.19.10.03.zip', 'wb').write(r.content)
    
        shutil.unpack_archive('bedrock-server-1.19.10.03.zip')
    
        print("Install Complete! Starting...")
    
        os.remove(chk_file)
        delete = "bedrock-server-1.19.10.03.zip"
        os.remove(delete)
    
        print("[Elytra] Server marked as installed")
    if s == "linux" :
        print("Downloading BDS")
    
        get = "https://minecraft.azureedge.net/bin-linux/bedrock-server-1.19.10.03.zip"
    
        r = requests.get(get, allow_redirects=True)
    
        open('bedrock-server-1.19.10.03.zip', 'wb').write(r.content)
    
        shutil.unpack_archive('bedrock-server-1.19.10.03.zip')
    
        print("Install Complete! Starting...")
    
        os.remove(chk_file)
        delete = "bedrock-server-1.19.1.01.zip"
        os.remove(delete)
    
        print("[Elytra] Server marked as installed")



else:
 
    print("[Elytra] Server already marked as installed! Starting")



subprocess.Popen('bedrock_server.exe', shell=True)


def cont ():
    print("continue")


startmsg = "[Elytra] Finding resource and behavior packs..."

print("Starting Elytra...")

time.sleep(0.5)

Path("mods").mkdir(parents=True, exist_ok=True)

Path("mods/resource_packs").mkdir(parents=True, exist_ok=True)

Path("mods/behavior_packs").mkdir(parents=True, exist_ok=True)

Path("logs").mkdir(parents=True, exist_ok=True)

Path("info").mkdir(parents=True, exist_ok=True)

Path("ElytraSettings").mkdir(parents=True, exist_ok=True)

Path("other").mkdir(parents=True, exist_ok=True)





print("[Elytra] Folder check Complete...")





print("[Elytra] Type help for commands")

print(startmsg)

chk_file2 = Path("mods/resource_packs/pack")

if chk_file2.is_file():
    rfrom = "mods/resource_packs/pack"
    rto = "worlds/world/behavior_packs"
    shutil.move(rfrom, rto)

else:
    print("[Elytra] No resource packs detected")


chk_file3 = Path("mods/behavior_packs/pack")
if chk_file3.is_file():
    modfrom = "mods/behavior_packs/pack"
    modto = "worlds/world/resource_packs"
    shutil.move()

else:
    print("[Elytra] No Behavior packs detected")



chk_file9 = Path("ElytraSettings/Enter_beta.txt")

if chk_file9.is_file():
    print("==================================================================")
    print("|                         Elytra (V1.4)                          |")
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
    time.sleep(4)
    print("==================================================================")
    print("|                         Elytra (V1.4)                          |")
    print("|          To enter the beta versions of elytra make a file      |")
    print("|                called Enter_beta.txt in ElytraSettings         |")
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
    print("[Elytra] Error behavior_packs folder is missing and is needed to start the server!")
    time.sleep(4)
    print("Stopping server...")
    time.sleep(2)
    exit()

chk_file3 = Path("resource_packs/vanilla/blocks.json")

if chk_file3.is_file():
    cont 
else:
    print("[Elytra] Error Resource_packs folder is missing and is needed to start the server!")
    time.sleep(4)
    print("Stopping server...")
    time.sleep(2)
    exit()

time.sleep(0.5)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))

print("[Elytra] Joinable IP: ",s.getsockname()[0])
s.close()

while True :
    time.sleep(0.5)
    cmd = input()
    if cmd == "elytra sys" :
        Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
        new = []

        
        for item in Id:
            new.append(str(item.split("\r")[:-1]))
        for i in new:
            print(i[2:-2])
    cmd = input()
    if cmd == "elytra mods" :
        path = 'mods'
        files = os.listdir(path)
        for filename in files:
            print(filename)
    if cmd == "elytra worlds" :
        path = 'worlds'
        files = os.listdir(path)
        for filename in files:
            print(filename)
    if cmd == "elytra info" :
        print("You might want to check github for new features, info and updates! (you are currently on version " + version + ")")
    if cmd == "elytra kill" :
        print("are you sure you want to kill the server? This can cause world corruption or 1-5 minute set backs and other errors! (yes or no)")
        confirm = input()
        if confirm == "yes" :
            print("[Elytra] killing...")
            subprocess.Popen('server.exe', shell=True)
            exit()
        if confirm == "no" :
            pass


