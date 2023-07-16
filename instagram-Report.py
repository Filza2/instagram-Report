try:
	import json,sys,requests,re,os
	from requests import post,get
	from time import time
	from secrets import token_hex
	from random import choice
	from threading import Lock
	from time import sleep
except Exception as Joker:
	input(Joker);sys.exit()


def header():
    os.system("cls" if os.name=='nt' else "clear");print(f"""
██╗███╗   ██╗███████╗████████╗ █████╗       ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗      ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║█████╗██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
██║██║╚██╗██║╚════██║   ██║   ██╔══██║╚════╝██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║██║ ╚████║███████║   ██║   ██║  ██║      ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝      ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝
                        By @TweakPY - @vv1ck / v2
""")

class RSP:
	def Login():
		return 'logged_in_user'
	def BDpes():
		return '"error_type":"bad_password"'
	def BDusr():
		return '"exception_name":"UserInvalidCredentials"'
	def BadLog():
		return '"Please wait a few minutes before you try again."'
class REQUESTS:
	def UUID():
		lst='QAZ123WSX456EDC789RFV012TGV345YHBUJN678IKLPO0'
		return str(str(''.join((choice(lst) for i in range(8))))+'-'+str(''.join((choice(lst) for i in range(4))))+'-'+str(''.join((choice(lst) for i in range(4))))+'-'+str(''.join((choice(lst) for i in range(4))))+'-'+str(''.join((choice(lst) for i in range(12)))))
	def HEADERS(uuids):
		return {"X-FB-Client-IP" : "True","X-IG-Connection-Type" : "WiFi","Accept-Language" : "en-EN;q=1.0","x-fb-rmd" : "state=URL_ELIGIBLE","Host" : "i.instagram.com","X-IG-Capabilities" : "36r/F/8=","X-Bloks-Version-Id" : str(token_hex(8)*4),"X-IG-App-Locale" : "en","X-IG-ABR-Connection-Speed-KBPS" : "130","X-IG-Timezone-Offset" : "10800","X-IG-Mapped-Locale" : "en_EN","Connection" : "keep-alive","X-IG-App-ID" : "124024574287414","X-FB-Friendly-Name" : "api","X-IG-Bandwidth-Speed-KBPS" : "303.000","X-Bloks-Is-Panorama-Enabled" : "true","Priority" : "u=2, i","X-Pigeon-Rawclienttime" : str(time()),"User-Agent" : "Instagram 275.0.0.17.100 (iPhone8,1; iOS 13_5; en_JO; en-JO; scale=2.00; 750x1334; 457382757) AppleWebKit/420+","X-IG-Family-Device-ID" : uuids,"X-MID" : "ZK0F5gAAAAFe8doHU5fRFe4Tx8Qa","X-Tigon-Is-Retry" : "False","Content-Length" : "860","X-FB-Connection-Type" : "wifi","X-IG-Device-ID" : uuids,"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8","X-FB-Server-Cluster" : "True","X-IG-Connection-Speed" : "0kbps","IG-INTENDED-USER-ID" : "0","X-IG-Device-Locale" : "en-JO","X-FB-HTTP-Engine" : "Liger"}
	def DATA(uuids,username,password):
		return {"phone_id":uuids,"reg_login":"0","device_id":uuids,"has_seen_aart_on":"0","username": username,"adid":REQUESTS.UUID(),"login_attempt_count":"0","enc_password":f"#PWD_INSTAGRAM:0:&:{password}"}
	def URLR1():
		return 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/'
	def URLR2():
		return 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/'

class REPORTING_INSTAGRAM:
	def __init__(self,token,meID):
		self.DN,self.ER,self.tim=0,0,0
		self.RUN=True;self.PRNT=Lock()
		self.meID=meID
		self.hed = REQUESTS.HEADERS(REQUESTS.UUID())
		self.hed['Authorization']=str(token)
		self.mode=input('Modes: \n\t-1) Unimportant_or_fraudulent\n\t-2) Abuse_or_harassment\n [?] Choose: ')
		if (self.mode=='1'):pass
		elif (self.mode=='2'):pass
		else:input('error');sys.exit()
		self.TargetUser=input('Enter Target Username: ')
		self.GetIdTarget()
		
	def Unimportant_or_fraudulent(self,report):
		while self.RUN:
			sleep(self.tim)
			RPTS=post(REQUESTS.URLR1(),headers=self.hed,data='signed_body=SIGNATURE.%7B%22_uuid%22%3A%2289A76011-25F9-4871-855E-642529E73098%22%2C%22_uid%22%3A%2251490708520%22%2C%22params%22%3A%22%7B%5C%22server_params%5C%22%3A%7B%5C%22tag_source%5C%22%3A%5C%22tag_selection_screen%5C%22%2C%5C%22serialized_state%5C%22%3A%5C%22'+str(report)+'%5C%22%2C%5C%22INTERNAL__latency_qpl_marker_id%5C%22%3A36707139%2C%5C%22INTERNAL__latency_qpl_instance_id%5C%22%3A96250710900022%2C%5C%22show_tag_search%5C%22%3A0%2C%5C%22is_bloks%5C%22%3A1%7D%2C%5C%22client_input_params%5C%22%3A%7B%5C%22tags%5C%22%3A%5B%5C%22ig_spam_v3%5C%22%2C%5C%22ig_report_account%5C%22%2C%5C%22ig_its_inappropriate%5C%22%5D%7D%7D%22%2C%22bloks_versioning_id%22%3A%2226347c83bfc5586e67915b911fda34fde25be1948c63367c19788ac4900343f1%22%7D');R=RPTS.text
			
			if ('Thanks for letting us know' in RPTS.text):self.DN+=1
			
			elif R.__contains__('‏Thanks for letting us know'):self.DN+=1
			else:
				print(RPTS)
			
			with self.PRNT:
				print(f'\r[+] Done: [{self.DN}] , Error: {self.ER}\r',end="")
	def Abuse_or_harassment(self,report):
		self.hed["X-IG-Nav-Chain"]="IGExploreViewController:explore_popular:2:main_explore:1689343193.642112::,IGSearchTypeaheadViewController:search_typeahead:3::1689343194.537297::,IGSearchResultsViewController:search_typeahead:4::1689343194.538094::,IGProfileViewController:profile:5::1689343195.984527::,IGProfileUserGridFeedViewController:profile:11::1689343216.883084::,IGBloksBottomSheetViewController:bloks_unknown:12::1689343236.554670::,IGBloksBottomSheetViewController:bloks_unknown:13::1689343240.578664::"
		self.hed["IG-U-Shbts"]="1689219683,51490708520,1720755683:01f789ab91c347a951caec7abe415fefd7ab9d2261f86bb83843048f10782c73bab5109b"
		self.hed["IG-U-IG-Direct-Region-Hint"]="RVA,51490708520,1720546042:01f790c9037bdb8b77fc7da9bfac92c56a4c9b3fe745ca0a4f1e4aa61e115354bae81656"
		while self.RUN:
			sleep(self.tim)
			RPT=post(REQUESTS.URLR2(),headers=self.hed,data='signed_body=SIGNATURE.%7B%22_uuid%22%3A%2289A76011-25F9-4871-855E-642529E73098%22%2C%22_uid%22%3A%2251490708520%22%2C%22params%22%3A%22%7B%5C%22server_params%5C%22%3A%7B%5C%22INTERNAL__latency_qpl_marker_id%5C%22%3A36707139%2C%5C%22serialized_state%5C%22%3A%5C%22'+str(report)+'%3D%5C%22%2C%5C%22INTERNAL__latency_qpl_instance_id%5C%22%3A141172918900002%2C%5C%22selected_option%5C%22%3A%5C%22report%5C%22%7D%7D%22%2C%22bloks_versioning_id%22%3A%2226347c83bfc5586e67915b911fda34fde25be1948c63367c19788ac4900343f1%22%7D').text
			if RPT.__contains__('"شكرًا، لقد تلقينا بلاغك."'):self.DN+=1
			elif RPT.__contains__('"Thank you, we received your report"'):self.DN+=1
			else:
				print(RPT)
			with self.PRNT:
				print(f'\r[+] Done: [{self.DN}] , Error: {self.ER}\r',end="")
	def getTOKENS(self,TarID):
		report=post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.ig.ixt.triggers.bottom_sheet.ig_content/',headers=self.hed,data={"trigger_session_id":REQUESTS.UUID(),"preloading_enabled":"0","entry_point":"chevron_button","_uuid":REQUESTS.UUID(),"_uid":self.meID,"bloks_versioning_id":"26347c83bfc5586e67915b911fda34fde25be1948c63367c19788ac4900343f1","is_in_holdout":"0","trigger_event_type":"ig_report_button_clicked","location":"ig_profile","ixt_initial_screen_id":REQUESTS.UUID(),"ig_object_value":TarID,"shopping_session_id": str(token_hex(8)*2),"ig_container_module":"profile","ig_object_type":"5","logging_extra":{"navigation_chain":"IGExploreViewController:explore_popular:2:main_explore:1689330714.586023::,IGSearchTypeaheadViewController:search_typeahead:3::1689330715.318819::,IGSearchResultsViewController:search_typeahead:4::1689330715.320813::,IGProfileViewController:profile:5::1689330716.482498::"}}).json()['layout']['bloks_payload']['embedded_payloads'][0]['payload']['layout']['bloks_payload']['tree']['㓟']['#']['㐈'][' '][1]['㐈'][' '][0]['㐅'][' '][1]['㐈'][' '][0]['㐈']['-'].split('"tag_selection_screen", "')[1].split('", (bk.action.i32.Const')[0]
		try:self.tim=int(input('[!] Enter Time sleep : '))
		except ValueError:self.tim=3
		print('\n -------------------------\n')
		if (self.mode == '1'):self.Unimportant_or_fraudulent(report)
		elif (self.mode=='2'):self.Abuse_or_harassment(report)
	def GetIdTarget(self):
		try:
			IDS=post('https://i.instagram.com:443/api/v1/users/lookup/',headers=REQUESTS.HEADERS(REQUESTS.UUID()),data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % self.TargetUser}).json()['user_id']
		except KeyError:
			try:
				IDS=get(f'https://www.instagram.com/{self.TargetUser}',headers={'Host': 'www.instagram.com','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Connection': 'keep-alive','Cookie':  f'csrftoken=5cwfemJ18nNQ8KxjZZcAYxuQ790Swlbj','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','TE': 'trailers'});IDS=re.findall('"profile_id":"(.*?)"',IDS.text)[0]
			except IndexError:
				IDS = input('[-] I could not extract the account ID, please enter it manually: ')
		self.getTOKENS(IDS)
class LOGIN_INSTAGRAM_API:
	def __init__(self):
		self.username=input('[?] username : ')
		self.password=input('[?] password : ')
		self.CheckLog()
	def CheckLog(self):
		uuids=REQUESTS.UUID()
		try:
			CHEACK=post('https://i.instagram.com/api/v1/accounts/login/',headers=REQUESTS.HEADERS(uuids),data=REQUESTS.DATA(uuids,self.username,self.password))
			if (RSP.Login() in CHEACK.text ):
				print('[+] Logged in successfully..')
				token=CHEACK.headers['ig-set-authorization']
				meID = CHEACK.json()['logged_in_user']['pk']
				REPORTING_INSTAGRAM(token,meID)
			
			elif (RSP.BDusr() in CHEACK.text):
				input('[-] Username is incorrect')
					
			elif (RSP.BDpes() in CHEACK.text):
				input('[-] Password is incorrect')
			elif (RSP.BadLog() in CHEACK.text):
				input('[-] Too many login attempts, please try again later or use vpn')
			else:
				input(CHEACK.text,CHEACK)
		except requests.exceptions.ConnectionError:
			input('error log')
			
header()
LOGIN_INSTAGRAM_API()
