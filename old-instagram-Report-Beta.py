try:from requests import get,post;from time import sleep;from user_agent import generate_user_agent;from colorama import Fore;import random,uuid,requests
except Exception as TweakPY:exit(TweakPY)
uid=str(uuid.uuid4());dpi_phone=['133','320','515','160','640','240','120''800','480','225','768','216','1024'];model_phone=['TweakPY-Local','TweakPY-Phone','TweakPY-With-Flavor','Nokia 2.4','HUAWEI','Galaxy','Unlocked Smartphones','Nexus 6P','Mobile Phones','Xiaomi','samsung','OnePlus'];pxl_phone=['623x1280','700x1245','800x1280','1080x2340','1320x2400','1242x2688'];i_version=['114.0.0.20.2','114.0.0.38.120','114.0.0.20.70','114.0.0.28.120','114.0.0.0.24','114.0.0.0.41'];red=Fore.RED;grn=Fore.GREEN;RS=Fore.RESET;yel=Fore.YELLOW;P=print
User_Agent=f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'



def IG_Report(RN):
	user=input(f"[?] username : ")
	if user=="":exit("[!] You must write The username")
	pess=input(f"[?] Password : ")
	if pess=="":exit("[!] You must write The password")
	LR=post('https://i.instagram.com/api/v1/accounts/login/',headers={'User-Agent': User_Agent,"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "en-US","X-IG-Capabilities": "3brTvw==","X-IG-Connection-Type": "WIFI","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",'Host': 'i.instagram.com'},data={'_uuid': uid,'password': pess,'username': user,'device_id': uid,'from_reg': 'false','_csrftoken': 'missing','login_attempt_count': '0'},allow_redirects=True)
	if 'logged_in_user' in LR.text:P(grn+"\n[+] Done Login .."+RS);SS=LR.cookies['sessionid'];CST=LR.cookies['csrftoken']
	elif 'The password you entered is incorrect' in LR.text:P(red+"\n[-] Please check Your Password !"+RS);exit()
	elif "Please check your username and try again." in LR.text:P(red+"\n[-] username Not Found !"+RS);P("\n[/] Check Your user And Try .");exit()
	elif 'challenge_required' in LR.text:P(yel+"\n[-] Secure Account ! .."+RS);P("\n[/] Try a diffrent Account .");exit()
	elif 'inactive user' in LR.text:P(red+'\n[!] This user is BAN From insta ...'+RS);P("\n[/] Try a diffrent Account .");exit()
	elif "We're working on it and we'll get it fixed as soon as we can." in LR.text:P(red+"\n[#] Retry After A minute !"+RS);exit()
	elif 'Please wait a few minutes before you try again' in LR.text:P(red+"\n[#] Retry After A minute !"+RS);exit()
	elif 'Bad request' in LR.text:P("\n[-] Error in insta retry after 15 minute ..");exit()
	elif 'Invalid Parameters' in LR.text:P(red+"\n[-] Error Please Reinstall The Tool From @TweakPY .."+RS);exit()
	else:exit("\n[!] Insta Having a Error with The Request Please Retry ... ")    
	target=input("[?] Target: ")
	RID=post('https://i.instagram.com:443/api/v1/users/lookup/',headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Instagram 99.4.0 vv1ck_TweakPY (vv1ck_TweakPY)","Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % target}).json();TID=str(RID['user_id'])
	if 'No users found' in RID:exit('[!] No users Found Check Your Traget !')#The username Must Be Entered Manually Not Copy Paste
	while True:
		try:
			RR=post("https://i.instagram.com/users/"+TID+"/flag/",headers={"User-Agent": generate_user_agent(),"Host": "i.instagram.com",'cookie': f"sessionid={SS}","X-CSRFToken": CST,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},data='source_name=&reason_id=1&frx_context=',allow_redirects=False)
			if 'ok' in RR.text:P(grn+f"── Done Report"+RS)
			else:exit(f"\n[-] Error Report .") 				
		except requests.exceptions.TooManyRedirects:
			exit()


def main():
	P(f"""\n\t{red}IG{RS} Report vBeta.1.3
        /\ /| 
       |||| |
        \ | \\
    _ _ /  @ @    
  /    \   =>{red}X{RS}<=  
/|      |   /   By @TweakPY - @vv1ck                  
                
\|     /__| | 
  \_____\ \__\\
  """)
	IG_Report(RN=0)
main()
