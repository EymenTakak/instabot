#LİBRARY
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random as rn
import pyfiglet
import colorama
import json
from urllib.request import urlopen
from progress.bar import Bar


colorama.init()
def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))


def prPurple(skk): print("\033[95m {}\033[00m".format(skk))


def prCyan(skk): print("\033[96m {}\033[00m".format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))


def prBlack(skk): print("\033[98m {}\033[00m".format(skk))
YELLOW = "\x1b[1;33;40m"
RED = "\x1b[1;31;40m"

prCyan(pyfiglet.figlet_format("INSTAGRAM BOT"))
prCyan("# ==============================================================================")
prRed("# author       :Eymen Takak")
prRed("# github       :https://github.com/EymenTakak")
prCyan("# ==============================================================================")


print(f"\n{YELLOW}Number Of Repeat: ", end='')
accnumber = int(input())
# URLS
url = "https://www.instagram.com/?hl=tr"
print(f"\n{YELLOW}Post Url: ", end='')
posturl = input()

#NEEDED TO FOLLOW PROFİLES URL
print(f"\n{YELLOW}Profile URL: ", end='')
profile1 = input()
print(f"\n{YELLOW}Profile URL2: ", end='')
profile2 = input()
print(f"\n{YELLOW}Profile URL3: ", end='')
profile3 = input()
print(f"\n{YELLOW}Profile URL4: ", end='')
profile4 = input()
print(f"\n{YELLOW}Profile URL5: ", end='')
profile5 = input()

#HOW MANY USERS NEED TO TAG
print(f"\n{YELLOW}HOW MANY NEED TO TAG(MİN VALUE=1): ", end='')
usernum = int(input())

#NEEDED COMMENT
comment = "Katıldım."

#SAVE POST
print(f"\n{YELLOW}ARE YOU NEED TO SAVE POST ? Y/N: ", end='')
answer = input()
answer.capitalize()
if answer=="Y":
    savepostt=1
elif answer=="N":
    savepostt=0




#INSTAGRAM ACCOUNTS
accounts = {"iplikci8yavuzselim4":"XSMGSBB973",
            "dal3abidin3":"GVJKQQX960",
            "buyukcam2cagri2":"DHNLVKN975",
            "altun5irfanyildirim7":"GPAOJNH980",
            "babacan4haluk5":"PEMJKHT981",
            "alici8ovunc8":"ZLCKXEH976",
            "basar5nuray2":"KMRAFBY982",
            "isik8berfu2":"YJLJRTP983",
            "sahin5irem4":"RXEGPBS985",
            "saricicek6bahadir1":"GUJAZFC986",
            "nalbant4cihan6":"RQSEXSI988",
            "erdogan4orkun7":"NLDOSTC989",
            "seven4mehtap5":"KPCITID990",
            "azar4latife6":"SOQXEGW991",
            "copur7murat1":"TEDRRKG987",
            "ekiz9hatun3":"TMZAEXP992",
            "gul9miray5":"CMHYKLX994",
            "karkin4aylinsevil0":"BQOJMXP993",
            "cevik2ozgur8":"JHBGNFA995",
            "koc4fatihmehmet5":"ECEBIGL996",
            "kozanoglu3mustafa7":"XYRYHVE999",
            "karadeniz7emrah4":"GYXDKFD1001",
            "batmaz9eser4":"QOUVACM1002",
            "kaya1huseyin7":"LZFYRQC1000",
            "baygeldi2rukiye8":"NJGZXSV1003",
            "ozcelik9ozlem8":"FSHMIJM1005",
            "destegul9yeliz4":"QUMRKXP1006",
            "bacak1serhat4":"IXJIWJO1007",
            "sengul4mehmet2":"IQVPKMM1008",
            "keles3elzem7":"ATFZSCE1010",
            "yardimci6cebbar7":"YDVFUKE1012",
            "yilmaz2savas0":"MTOFJBK1015",
            "asig9kubra3":"KLBQKIB1014",
            "ozturk4abdullah0":"JUDGWEV1016",
            "kor5esra8":"MJRVTAW1018",
            "buyukkal1sibel3":"FMZTKJP1019",
            "sari0mucadiye8":"LATYIMB1022",
            "uzum4zehra5":"FYPQSBT1023",
            "okur2belgin5":"PHDYLMA1021",
            "sasmaz1velienes2":"SBKLWQV1026",
            "esen8veysi1":"KZQGMMF1028",
            "hoke9efnan5":"AGZJXHY1027",
            "kazan1ali5":"MMTSGQB1030",
            "eken5zeynep2":"MGJMOUE1029",
            "tekin2bengu9":"JKBOCPY971",
            "sengul9isik6":"JFZKEPO1032",
            "seyhan5zuhal8":"MVSWJOY1033",
            "demir0selahattin4":"FBWOPVO1035",
            "kinalioglu7edipguvenc2":"WGVNKKP1037",
            "sokmen2volkan8":"ETKCSVX1038",
            }




#RANDOM USERNAMES
user1 = "@"+rn.choice(list(accounts.keys()))
user2 = "@"+rn.choice(list(accounts.keys()))
user3 = "@"+rn.choice(list(accounts.keys()))
user4 = "@"+rn.choice(list(accounts.keys()))
user5 = "@"+rn.choice(list(accounts.keys()))


def test():
    # PROXY
    with urlopen("http://pubproxy.com/api/proxy") as response:
        kaynak = response.read()
    veri = json.loads(kaynak)
    PROXY = veri["data"][0]["ipPort"]

    # PROFİLE PATH
    profile_path = r'C:\Users\Eymen\AppData\Roaming\Mozilla\Firefox\Profiles\jsglx7fq.default'
    options = Options()
    options.set_preference('profile', 'profile_path')
    options.add_argument('--proxy-server=%s' % PROXY)
    options.add_argument("--headless")
    # GECKODRİVER PATH
    service = Service("C:\\geckodriver.exe")
    driver = Firefox(service=service, options=options)

    username = rn.choice(list(accounts.keys()))
    password = accounts[username]

    #LOGİN SCREEN
    driver.get(url)
    time.sleep(10)
    driver.set_window_size(500, 1100)



    try:
        loginname = driver.find_element(By.XPATH, (
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"))
        loginname.send_keys(username)
    except:
        loginname2 = driver. find_element(By.className("username"))
        loginname2.send_keys(username)

    try:
        loginpass = driver.find_element(By.XPATH, (
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"))
        loginpass.send_keys(password)
    except:
        loginpass2 = driver.find_element(By.className("password"))
        loginpass2.send_keys(username)


    try:
        loginbutton = driver.find_element(By.XPATH, (
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div"))
        loginbutton.click()
        time.sleep(6)
    except:
        pass



    if not profile1== "":
        driver.get(profile1)
        time.sleep(4)
        follow =driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[3]/div/div/button"))
        follow.click()
        time.sleep(4)

    if not profile2== "":
        driver.get(profile2)
        time.sleep(4)
        follow2=driver.find_element(By.XPATH, ("//html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[3]/div/div/button"))
        follow2.click()
        time.sleep(4)

    if not profile3== "":
        driver.get(profile3)
        time.sleep(4)
        follow3 =driver.find_element(By.XPATH, ("//html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[3]/div/div/button"))
        follow3.click()
        time.sleep(4)

    if not profile4== "":
        driver.get(profile4)
        time.sleep(4)
        follow4 =driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[3]/div/div/button"))
        follow4.click()
        time.sleep(4)

    if not profile5== "":
        driver.get(profile5)
        time.sleep(4)
        follow5 =driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[3]/div/div/button"))
        follow5.click()
        time.sleep(4)

    driver.get(posturl)
    time.sleep(10)

    try:
        time.sleep(2)
        likepost = driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[1]/span[1]"))
        likepost.click()
        time.sleep(4)
    except:
        pass

    if savepostt==1:
        savepost = driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[1]/span[4]/div"))
        savepost.click()
        time.sleep(3)


    try:
        time.sleep(2)
        commentbutton = driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[1]/span[2]/button"))
        commentbutton.click()
        time.sleep(4)
    except:
        time.sleep(2)
        commentbutton = driver.find_element(By.XPATH, (
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[1]/span[2]/button"))
        commentbutton.click()
        time.sleep(4)



    commentclick = driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[3]/div/form/textarea"))
    if usernum==1:
        commentclick.send_keys(f"{user1}")
    if usernum==2:
        commentclick.send_keys(f'{user1} {user2}')
    if usernum==3:
        commentclick.send_keys(f'{user1} {user2} {user3}')
    if usernum==4:
        commentclick.send_keys(f'{user1} {user2} {user3} {user4}')
    if usernum==5:
        commentclick.send_keys(f'{user1} {user2} {user3} {user4} {user5}')
    try:
        postit = driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[3]/div/form/button/div"))
        postit.click()
        time.sleep(6)
        driver.quit()
    except:
        time.sleep(2)
        postit = driver.find_element(By.XPATH, (
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[3]/div/form/button/div"))
        postit.click()
        time.sleep(3)
        driver.quit()


total = 0
#START
print(f"\n{RED}Start Program ? Y/N: ", end='')
start = input()
start.capitalize()
if start =="Y":
    with Bar('Processing...', max=accnumber) as b:
        for _ in range(accnumber):
            test()
            b.next()
elif start == "N":
    pass

