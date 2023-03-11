try:
	from requests import get,post
	from time import sleep
	from user_agent import generate_user_agent
	from colorama import Fore
	import random,secrets,uuid,requests
except Exception as TweakPY:exit(TweakPY)
RQ=requests.session();uid=str(uuid.uuid4());RN=0;dpi_phone=['133','320','515','160','640','240','120''800','480','225','768','216','1024'];model_phone=['TweakPY-Local','TweakPY-Phone','TweakPY-With-Flavor','Nokia 2.4','HUAWEI','Galaxy','Unlocked Smartphones','Nexus 6P','Mobile Phones','Xiaomi','samsung','OnePlus'];pxl_phone=['623x1280','700x1245','800x1280','1080x2340','1320x2400','1242x2688'];i_version=['114.0.0.20.2','114.0.0.38.120','114.0.0.20.70','114.0.0.28.120','114.0.0.0.24','114.0.0.0.41'];red=Fore.RED;grn=Fore.GREEN;RS=Fore.RESET;yel=Fore.YELLOW;P=print
User_Agent=f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'




def AT_target(LR,RN):
	target=input("[?] Target: ")
	try:RID=post('https://i.instagram.com:443/api/v1/users/lookup/',headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=", "Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": User_Agent,"Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % target});TID=str(RID.json()['user_id'])
	except:
		try:RIDT=get(f'https://www.instagram.com/{target}/?__a=1',headers={'HOST': "www.instagram.com", 'KeepAlive': 'True','user-agent': generate_user_agent() ,'Cookie': secrets.token_hex(8)*2, 'Accept': "*/*", 'ContentType': "application/x-www-form-urlencoded","X-Requested-With": "XMLHttpRequest", "X-IG-App-ID": "936619743392459", "X-Instagram-AJAX": "missing","X-CSRFToken": "missing", "Accept-Language": "en-US,en;q=0.9"});TID=str(RIDT.json()['graphql']['user']['id'])
		except:exit("[-] Failed in get Target ID ..")
	RQ.headers.update({'X-CSRFToken': LR.cookies['csrftoken']})    
	while True:
		RR=RQ.post("https://i.instagram.com/users/"+TID+"/report/",data={'source_name': '', 'reason_id': 1, 'frx_context': ''});sleep(5)
		if 'Your reports help keep our community free of spam.' in RR.text:P(grn+f"\r┌─── Done Report >> [{RN}]",end=""+RS);RN+=1
		else:exit(f"\n[-] Error Report .") 				                    		                    

#See u
def Login():
	user=input(f"[?] user: ")
	if user=="":exit("[!] You must write The user")
	pess=input(f"[?] Password: ")
	if pess=="":exit("[!] You must write The password")
	P(red+'\r//',end='');sleep(0.4);P('\r///',end="");sleep(0.4);P('\r////',end="");sleep(0.4);P('\r/////',end="");sleep(0.4);P('\r\\\ %100',end=""+RS)
	LR=RQ.post('https://i.instagram.com/api/v1/accounts/login/',headers={'User-Agent': User_Agent,"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "en-US","X-IG-Capabilities": "3brTvw==","X-IG-Connection-Type": "WIFI","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",'Host': 'i.instagram.com'},data={'_uuid': uid,'password': pess,'username': user,'device_id': uid,'from_reg': 'false','_csrftoken': 'missing','login_attempt_count': '0'},allow_redirects=True)
	if 'logged_in_user' in LR.text:P(grn+"\n[+] Done Login .."+RS);AT_target(LR,RN)
	elif 'The password you entered is incorrect' in LR.text:P(red+"\n[-] Please check Your Password !"+RS);return Login()
	elif "Please check your username and try again." in LR.text:P(red+"\n[-] username Not Found !"+RS);P("\n[/] Check Your user And Try .");return Login()
	elif 'challenge_required' in LR.text:P(yel+"\n[-] Secure Account ! .."+RS);P("\n[/] Try a diffrent Account .");return Login()
	elif 'inactive user' in LR.text:P(red+'\n[!] This user is BAN From insta ...'+RS);P("\n[/] Try a diffrent Account .");return Login()
	elif "We're working on it and we'll get it fixed as soon as we can." in LR.text:P(red+"\n[#] Retry After A minute !"+RS)
	elif 'Please wait a few minutes before you try again' in LR.text:P(red+"\n[#] Retry After A minute !"+RS)
	elif 'Bad request' in LR.text:P("\n[-] Error in insta retry after 15 minute ..")
	elif 'Invalid Parameters' in LR.text:P(red+"\n[-] Error Please Reinstall The Tool From @TweakPY .."+RS)
	else:exit("\n[!] Insta Having a Error with The Request Please Retry ... ")    


def main():
	P(f"""\n\t{red}IG{RS} Report v1.3
        /\ /| https://github.com/{red}Filza2{RS}
       |||| |
        \ | \\
    _ _ /  @ @    
  /    \   =>{red}X{RS}<=  
/|      |   /   TweakPY-vv1ck                  
                {red}Avoiding failure is to avoid progress{RS}
\|     /__| | 
  \_____\ \__\\
  """)
	Login()
main()
