#!/env/bin/python
#coding UTF-8
###dont change anything. every line depends on the other
###Trust me
##Errors? contact whatsapp +254112185425
#Import
try:
    from telethon import TelegramClient, sync, events
    from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
    from telethon.errors import SessionPasswordNeededError
    from bs4 import BeautifulSoup
    from time import sleep as Kelvoh
    import time
    import datetime
    from datetime import datetime
    import requests, json, re, sys, os
    import colorama as Mbithi
    from colorama import Fore, Back, Style
    
    #color
    Mbithi.init(autoreset=True)
    set = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
    set2 = Style.NORMAL+Fore.GREEN
    dear = Style.RESET_ALL
    mine = Style.DIM+Fore.WHITE
    line = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
    get = Style.NORMAL+Fore.MAGENTA
    yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
    yellow2 = Style.NORMAL+Fore.YELLOW
    red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
    red2 = Style.NORMAL+Fore.RED
    timezone = datetime.now().strftime("%c")
    #banner
    banner = f"""{line}===================================================
{set}Author           {yellow}|{mine}      g1ng3rb1t3 > 0x41414141
{set}code             {yellow}|{mine}      Public not obfuscated
{set}Note             {yellow}|{mine}      Knowledge is free
{set}Created          {yellow}|{mine}      04:41 PM Sep 30, 2020
{set}Time now         {yellow}|{mine}      {timezone}
{line}============{yellow}Whatsapp{line} = {mine}+254112185425{line}==============="""
    #System_Script
    if not os.path.exists('session'):
        os.makedirs('session')
    
    
    
    api_id = '717425'
    api_hash = '322526d2c3350b1d3530de327cf08c07'
    
    if len(sys.argv) < 2:
        print(banner)
        print(f'\n{yellow}Usage : {set}python main.py +254')
        sys.exit(1)
    phone_number = sys.argv[1]
    print(banner)
    client = TelegramClient('session/'+phone_number,api_id,api_hash)
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone_number)
            me = client.sign_in(phone_number,input('{}Enter Code you received {}>>{} '.format(set,mine,dear)))
        except SessionPasswordNeededError:
            password = input('{}Your 2fa password {}>>{} '.format(set,mine,dear))
            me = client.start(phone_number,password)
    myself = client.get_me()
    print(f'          {yellow}Logged in as  {mine}{myself.first_name}{line}')
    print(f'{set}[01] {mine}Claim')
    print(f'{set}[02] {mine}Check balance')
    opti = input(f'{line}[{mine}Choose a choice{line}]> {mine}')
    if opti in ('01','1'):  
        channel_username = '@Dogecoin_click_bot'
        
        
        c = requests.session()
        
        ua = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        
        channel_entity = client.get_entity(channel_username)
        for ulang in range(999999999):
            sys.stdout.write('\r                                                        \r')
            sys.stdout.write(f'\r{mine}Getting URL')
            client.send_message(entity=channel_entity,message=' Visit sites')
            Kelvoh(10)
            message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            channel_id = message_history.messages[0].id
            if message_history.messages[0].message.find('Sorry, there are no new ads available.') != -1:
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write(f'\r{red}Sorry!! There are no new ads available!!!!!\n')
                break
            url = message_history.messages[0].reply_markup.rows[0].buttons[0].url
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write('\r{}Visitting  URL {}'.format(yellow2,dear)+url)
        
            r = c.get(url,headers=ua)
            soup = BeautifulSoup(r.text,"html.parser")
        
            if soup.find('div',class_='g-recaptcha') is None and soup.find('div',id='headbar') is None:
                Kelvoh(2)
                message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                message = message_history.messages[0].message
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write('\r'+yellow+message)
                if message_history.messages[0].message.find('Please stay on') != -1 or message_history.messages[0].message.find('You must stay') != -1:
                    timer = re.findall(r'([\d.]*\d+)',message)
                    Kelvoh(int(timer[0]))
                    Kelvoh(3)
                    posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                    messageres = posts.messages[1].message
                    Kelvoh(2)
                    sys.stdout.write('\r                                                     \r')
                    sys.stdout.write("\r\033[1;30m==> \033[1;32m"+messageres+"\n")
            elif soup.find('div',id='headbar') is not None:
                for data in soup.find_all('div',class_='container-fluid'):
                    code = data.get('data-code')
                    timer = data.get('data-timer')
                    token = data.get('data-token')
                    sleep(int(timer))
                    r = c.post('https://dogeclick.com/reward',data={'code': code, 'token': token},headers=ua)
                    jsn = json.loads(r.text)
                    sys.stdout.write('\r                                                     \r')
                    sys.stdout.write(set+"\rYou earned "+jsn['reward']+" Doge for visiting sites\n")
            else:
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write(red+'\rCaptcha detected')
                Kelvoh(2)
                client(GetBotCallbackAnswerRequest(channel_username,channel_id,data=message_history.messages[0].reply_markup.rows[1].buttons[1].data))
                sys.stdout.write('\r                                                     \r')
                print (red+'\rSuccess Skip Captcha\n')
    elif opti in ('2','02'):
        channel_entity=client.get_entity("@Dogecoin_click_bot")
        channel_username="@Dogecoin_click_bot"
        client.send_message(entity=channel_entity,message="\xf0\x9f\x92\xb0 Balance")
        Kelvoh(5)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        print (f'{red}[+] {set}{message}')
        sys.exit()
    else:
        print(f'{mine}[{red}Error Option{mine}]{yellow} -> {opti}')
        Kelvoh(1)
        sys.exit()
except KeyboardInterrupt:
    print(f'\n\n{red}[\!/]{yellow}! closed')
    print(f'{red}[++]{yellow}by g1ng3rb1t3 > {red}0x41414141'+'\a\a\a')
    sys.exit()
except Exception as kevo:
    Kelvoh(2)
    print(f'{yellow}[!] Error: {red}{kevo}')
    sys.exit()