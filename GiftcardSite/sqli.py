import requests, re
files = open('sqli.gftcrd', 'rb').read()
password = "000000000000000000000000000078d2$18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3"

s = requests.session()
payload = {'username': 'sl4506@nyu.edu', 'password': 'password'}
r = s.get("http://127.0.0.1:8000/login.html")
s.post('http://127.0.0.1:8000/login.html', data = payload)
cookie = s.cookies.get_dict()
r = s.post('http://127.0.0.1:8000/use.html', cookies = cookie, files = {'card_data' : files}, data = {'card_fname' : 'test', 'card_supplied' : True})
print(r.text)
if (password in r.text):
	print ("Vulnerable to SQLi!")
else:
	print ("Not Vulnerable to SQLi!")