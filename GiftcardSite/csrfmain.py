import requests

s = requests.session()
cookie = s.cookies.get_dict()
get_token = s.get("http://127.0.0.1/gift.html")
if ('<input type="hidden" name="csrfmiddlewaretoken' in (get_token.text)):
	print("Not vulnerable to CSRF!")
else:
	print ("Vulnerable to CSRF!")