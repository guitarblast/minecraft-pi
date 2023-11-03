#!/usr/bin/python3
#-----------------------------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#     Minecraft Skin Fixer
#     minecraft_skin_fixer.py
#
# This is a supporting set of functions that are used
# by the main script (poolmain.py) and the web front-end (poolweb.py).
#
# Author : Matt Hawkins
# Date   : 21/06/2018
#
# For details on how to use this script please visit :
# https://www.raspberrypi-spy.co.uk/2016/03/how-to-change-your-character-skin-in-minecraft-pi-edition/
#
#-----------------------------------------------------------
from PIL import Image

skinFile='/opt/minecraft-pi/data/images/mob/char.png'

try:
  # Open skin, resize to 64x32 and set to RGBA
  image=Image.open(skinFile)
  image=image.crop((0,0,64,32))
  image=image.convert('RGBA')
  image.save(skinFile)
except:
  print("There was an error. Did you run with sudo?")
