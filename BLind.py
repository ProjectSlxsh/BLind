import time
import os
print("""
     ...     ..            ..    .                     ..
  .=*8888x <"?88h.   x .d88"    @88>                 dF
 X>  '8888H> '8888    5888R     %8P      u.    u.   '88bu.
'88h. `8888   8888    '888R      .     x@88k u@88c. '*88888bu
'8888 '8888    "88>    888R    .@88u  ^"8888""8888"   ^"*8888N
 `888 '8888.xH888x.    888R   ''888E`   8888  888R   beWE "888L
   X" :88*~  `*8888>   888R     888E    8888  888R   888E  888E
 ~"   !"`      "888>   888R     888E    8888  888R   888E  888E
  .H8888h.      ?88    888R     888E    8888  888R   888E  888F
 :"^"88888h.    '!    .888B .   888&   "*88*" 8888" .888N..888
 ^    "88888hx.+"     ^*888%    R888"    ""   'Y"    `"888*""
        ^"**""          "%       ""                     ""

""")

print("------------------------------------------------------------------------------------")
#shits fucked stand by
print("""
 _______ __     __ __               ___              __             __
|     __|  |--.|__|  |_.-----.    .'  _|.--.--.----.|  |--.-----.--|  |
|__     |     ||  |   _|__ --|    |   _||  |  |  __||    <|  -__|  _  |
|_______|__|__||__|____|_____|    |__|  |_____|____||__|__|_____|_____|

        __                  __      __
.-----.|  |_.---.-.-----.--|  |    |  |--.--.--.
|__ --||   _|  _  |     |  _  |    |  _  |  |  |
|_____||____|___._|__|__|_____|    |_____|___  |
                                         |_____|""")


a = input ("""Modules:
1)Spamming, 
2)Cli Programs 
3)Clock
Select a number:""")
# Spamming tools
a_int= int(a)
if a_int== (1):
  import pyautogui
  x = input("Text to spam \n:")
  z = input("Delay, delay between each message being sent, 0.1 is tenth of a second 1 is a second \n:")
  y = input(" General mode,  Discord mode,  Alarm mode,  Kamari mode \nMode selection:")
  
  if y ==("Discord"):
    pyautogui.click(900,1000)
    time.sleep(0.3)
    while True:
        pyautogui.typewrite((x))
        time.sleep((z))
        pyautogui.press("enter")

  if y ==("general"): 
    while True:
        pyautogui.typewrite((x))
        time.sleep((z))
        pyautogui.press("enter")

  if y == ("Kamari mode"):
    pyautogui.click(900,1000)
    time.sleep(0.3)
    while True:
        pyautogui.typewrite((x))
        time.sleep((z))
        pyautogui.press("enter")
        pyautogui.press("enter")        

  if y ==("Alarm"):
    import datetime, time
    print("Hours in 24 hour format!")
    o = input("Hour of start \n:")
    u = input("Minute of start \n:")
    k = input("Number of minutes to spam once started \n:")
    u_int = int(u)
    o_int = int(o)
    k_int = int(k)
    today = datetime.datetime.now()
    sleep = (datetime.datetime(today.year, today.month, today.day, (o_int),(u_int)) - today).seconds
    #This shits works now, i feel bad for people that might eventually work on this, may god be on your side, even i dont remember what I was doing 
    print('time till start: ' + str(datetime.timedelta(seconds=sleep)))
    time.sleep(sleep)
    
    pyautogui.click(900,1000)
    time.sleep(0.3)
    t_end = time.time() + 60*(k_int)
    #things might work now, stfu i fixed it eventually 
    while time.time() < t_end:
      pyautogui.typewrite((x))
      time.sleep((z))
      pyautogui.press("enter")




#Command line tools / programs
if a_int == (2):
  import pyautogui
  import os

  pos=input("""
1)spotdl-scripts
2)ping-test
3)yt-dlp-scripts

Select Number:""")
  pos_int=int(pos)
  if pos_int== (1):
      pop=int(input("""File Type:
1) mp3
2) m4a
3) flac
Select Number """))
      fax=input("Spotify Link:")
      if pop==(1):
        oop=(" spotdl --audio youtube-music --format mp3 download ")
      if pop==(2):
        oop=("spotdl --audio youtube-music --format m4a download ")
      if pop==(3):
        oop=("spotdl --audio youtube-music --format flac download ")
      os.system("cls")
      pyautogui.click(150,1060)
      time.sleep(0.5)
      pyautogui.typewrite (" command prompt ")
      pyautogui.press("enter")
      time.sleep(1)
      pyautogui.typewrite(oop + fax)
      
      
  

  if pos_int==(2):
    os.system("cls")
    os.system("ping 1.1.1.1 -t")
  
  if pos_int==(3):
    import yt_dlp
    os.system('cls')
    tot=int(input("""File type:
1) mp3
2) m4a
3) flac
4) mp4
Select Number:"""))
    xof= input("Input link:")
    if tot==(1):
      fox=(" -x --audio-format mp3 ")
    
    if tot==(2):
      fox=(" -x --audio-format m4a ")
    
    if tot==(3):
      fox=(" -x --audio-format flac ")
    
    if tot==(4):
      fox=(" --remux-video mp4")
    os.system("cls")
    os.system('yt-dlp' + fox + xof)
   
    
  

# This a fukcing clock
if a_int ==(3):
  import pyautogui
  import datetime
  import pyfiglet
  import time
  from pyfiglet import Figlet
  os.system('cls')
  while True:
    p= datetime.datetime.now()
    f= (datetime.datetime.strftime(p, '%H : %M : %S'))
    o_u = f
    i= Figlet(font='letters')
    print (i.renderText((o_u)), end="")
    print('\033[6A\033[2K', end='')
    time.sleep(1)
    #The \033[5A\033[2K allows for refresh with pyfiglet in without clearing, each font needs a differnt amount of room for clear so, changing the number 5a will change how many lines
    #it clears, this is something that will needed to be editted by the eu but its not a big deal, maybe figure out a way to fix in future?