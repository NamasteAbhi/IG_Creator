# -*- coding: utf-8 -*-
import requests
import uuid
import random
import time
from datetime import datetime
import base64
import json
import hashlib
import os
from faker import Faker
import string
import spintax


cl = Client()
print('                Instagram Account Creator\n                 Telegram @NamasteHacker\n')


# Functions
def generate_uuid(prefix: str = '', suffix: str = '') -> str:
    return f'{prefix}{uuid.uuid4()}{suffix}'


def generate_android_device_id() -> str:
    return "android-%s" % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]


def generate_useragent():
    with open("UserAgent.txt", "r")as file:
        agents = file.read().splitlines()
        a = random.choice(agents)
        user = a.split(",")
    return f'Instagram 261.0.0.21.111 Android ({user[7]}/{user[6]}; {user[5]}dpi; {user[4]}; {user[0]}; {user[1]}; {user[2]}; {user[3]}; en_US; {user[9]})'


def get_mid():
    params = None
    api_url = f"https://i.instagram.com/api/v1/accounts/login"
    response = requests.get(api_url, params=params)
    mid = response.cookies.get("mid")
    if mid != None:
        return mid
    else:
        u01 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        us1 = str("".join(random.choice(u01)for k in range(int(8))))
        return f'Y4nS4g{us1}zwIrWdeYLcD9Shxj'


def Username():
    fake = Faker()
    name = fake.name()
    return str(name)


def Password():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all, 9)
    password = "".join(temp)
    return password


def generate_jazoest(symbols: str) -> str:
    amount = sum(ord(s) for s in symbols)
    return f'2{amount}'


def Birthday():
    day = str(random.randint(1, 28))
    month = str(random.randint(1, 12))
    year = str(random.randint(1988, 2003))
    birth = [day, year, month]
    return birth

def DP():
    directory = r'Data/DP/'
    files = os.listdir(directory)
    random_file = random.choice(files)
    file_path = os.path.join(directory, random_file)
    return file_path

def Posts():
    posts = []
    directory = r'Data/Posts/'
    files = os.listdir(directory)
    for i in range(3):
        random_file = random.choice(files)
        file_path = os.path.join(directory, random_file)
        posts.append(file_path)
    return posts
    



# Veriables
BlockVersion = 'a399f367a2e4aa3e40cdb4aab6535045b23db15f3dea789880aa0970463de062'
App_ID = '567067343352427'

Device_ID = generate_uuid()
Family_ID = generate_uuid()
Android_ID = generate_android_device_id()
UserAgent = generate_useragent()
X_Mid = get_mid()
adid = str(uuid.uuid4())

water = str(uuid.uuid4())
username = Username()

password = "Test@9988"
jazoest = generate_jazoest(Family_ID)
birth = Birthday()

bio_spintax=r'{Reposting|Uploading|Posting|Reuploading} {videos|content|shorts} that make you {laugh|lol|😂|😆|😲|😵|🤣}\n You will {thank me|be thankful|be grateful|gr8ful} later {🤜🤛|👍|🤘|🤟|🙏} \n {Giveaways Happening Here|Free Giveaways Here|Product Giveaways Here|Free Products Here|Free Stuff Here|Products Giveaways Happening|Claim your Freebies Now|Claim Free Stuff Now|Get Free Stuff Here|Get Free Products Here|Get Free Gift Cards Here} {🗝|🔑|🔌|📱|💻|⌚️|💰|💵|💎|🎉}\n {⬇️⬇️⬇️|👇👇👇|🔽🔽🔽|⤵️⤵️⤵️}'






headers = {
    'Host': 'i.instagram.com',
    'X-Ig-App-Locale': 'en_US',
    'X-Ig-Device-Locale': 'en_US',
    'X-Ig-Mapped-Locale': 'en_US',
    'X-Pigeon-Session-Id': generate_uuid('UFS-', '-1'),
    'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),
    'X-Ig-Bandwidth-Speed-Kbps': str(random.randint(2500000, 3000000) / 1000),
    'X-Ig-Bandwidth-Totalbytes-B': str(random.randint(5000000, 90000000)),
    'X-Ig-Bandwidth-Totaltime-Ms': str(random.randint(2000, 9000)),
    'X-Bloks-Version-Id': BlockVersion,
    'X-Ig-Www-Claim': '0',
    'X-Bloks-Is-Layout-Rtl': 'false',
    'X-Ig-Device-Id': Device_ID,
    'X-Ig-Family-Device-Id': Family_ID,
    'X-Ig-Android-Id': Android_ID,
    'X-Ig-Timezone-Offset': '16500',
    'X-Fb-Connection-Type': 'WIFI',
    'X-Ig-Connection-Type': 'WIFI',
    'X-Ig-Capabilities': '3brTv10=',
    'X-Ig-App-Id': App_ID,
    'Priority': 'u=3',
    'User-Agent': UserAgent,
    'Accept-Language': 'en-US',
    'X-Mid': X_Mid,
    'Ig-Intended-User-Id': '0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Fb-Http-Engine': 'Liger',
    'X-Fb-Client-Ip': 'True',
    'X-Fb-Server-Cluster': 'True',
    'Connection': 'close',
}

num = input('Enter Num : ')
data = {
    'signed_body': 'SIGNATURE.{"phone_id":"'+Family_ID+'","login_nonce_map":"{}","phone_number":"'+num+'","guid":"'+Device_ID+'","device_id":"' + Android_ID + '","prefill_shown":"False"}',
}
response = requests.post(
    'https://i.instagram.com/api/v1/accounts/check_phone_number/', headers=headers, data=data).text
print(response)
data = {
    'signed_body': 'SIGNATURE.{"phone_id":"' + Family_ID + '","phone_number":"' + num + '","guid":"' + Device_ID + '","device_id":"' + Android_ID + '","android_build_type":"release","waterfall_id":"' + water + '"}',
}
res = requests.post('https://i.instagram.com/api/v1/accounts/send_signup_sms_code/',
                    headers=headers, data=data).text
print(res)
cood = input('Enter Code : ')
data = {
    'signed_body': 'SIGNATURE.{"verification_code":"'+cood+'","phone_number":"'+num+'","guid":"'+Device_ID+'","device_id":"' + Android_ID + '","waterfall_id":"'+water+'"}',
}
ree = requests.post('https://i.instagram.com/api/v1/accounts/validate_signup_sms_code/',
                    headers=headers, data=data).text
print(ree)
data = {
    'signed_body': 'SIGNATURE.{"phone_id":"'+Family_ID+'","guid":"'+Device_ID+'","name":"' + username + '","device_id":"' + Android_ID + '","email":"","waterfall_id":"'+water+'"}',
}
ree = requests.post('https://i.instagram.com/api/v1/accounts/username_suggestions/',
                    headers=headers, data=data).json()
usname = ree['suggestions_with_metadata']['suggestions'][0]['username']
print('UserName => '+usname)
print('Password => '+password)
timpp = int(datetime.now().timestamp())
data = {
    'signed_body': 'SIGNATURE.{"is_secondary_account_creation":"false","jazoest":"' + jazoest + '","tos_version":"row","suggestedUsername":"","verification_code":"'+str(cood)+'","sn_result":"API_ERROR: class X.2mY:7: ","do_not_auto_login_if_credentials_match":"true","phone_id":"'+Family_ID+'","enc_password":"#PWD_INSTAGRAM:0:'+str(timpp)+':' + password + '","phone_number":"'+str(num)+'","username":"'+str(usname)+'","first_name":"'+usname+'","day":"' + birth[0] + '","adid":"'+adid+'","guid":"'+Device_ID+'","year":"' + birth[1] + '","device_id":"' + Android_ID + '","_uuid":"'+Device_ID+'","month":"' + birth[2] + '","sn_nonce":"","force_sign_up_code":"","waterfall_id":"'+water+'","qs_stamp":"","has_sms_consent":"true","one_tap_opt_in":"true"}',
}
response = requests.post(
    'https://i.instagram.com/api/v1/accounts/create_validated/', headers=headers, data=data)
print(response.text)
if 'account_created":true' in response.text:
    print('Account Created Done')
    toka = response.headers['ig-set-authorization']
    fun = f'{usname}:{toka}'
    with open('filter.txt', 'a')as xxx:
        xxx.write(f'{usname}:{toka}\n')
        
    with open('accounts.txt', 'a')as xxx:
        xxx.write(f'{usname}:{password}:{toka}\n')
    
else:
    print(response.text)
