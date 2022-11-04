import requests
vul= "<script> alert('Vulnerable to XSS!') </script>"

s = requests.session()
payload = {'uname': 'sl4506@nyu.edu', 'pword': 'password123!'}
s.post('http://127.0.0.1/login.html', data = payload)
cookie = s.cookies.get_dict()
r = s.get('http://127.0.0.1/gift.html', cookies = cookie)
r = s.post('http://127.0.0.1/gift/0', data={'amount': '10', 'username': vul}, cookies = cookie)
if (r.text == "ERROR: <script> alert('Vulnerable to XSS!') </script> IS NOT A VALID RECIPIENT."):
	print("Vulnerable to XSS!")
else:
	print ("Not Vulnerable to XSS!")

#127.0.0.1:8000/gift.html?director=<a href="https://www.w3schools.com">Visit W3Schools</a>