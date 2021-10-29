When you see a docker-compose file, use the following command to run the exercise:

	sudo docker-compose up

If your machine does not provide docker-compose, you can install it by following this guide [link](https://docs.docker.com/compose/install/).

To solve the exercise, you need first to inspect the app with the browser’s debugger, and then, once you understood what you need to solve it, we suggest you write a Python script.

Some useful Python libraries:
```py
import hashlib
import codecs
import numpy as np
import requests

# A request example:

#IP
ip = "127.0.0.1"
port= "8080"

#we first check that our MD5 works by comparing Md5(100) with
#the one in the webpage
control = "f899139df5e1059396431415e770c6dd"
tester = 100
tester_b = str.encode(str(tester))
tester_md5 = hashlib.md5(tester_b).hexdigest()
print(f"tester={tester_md5 == control}")
```


## Solution
* a cookie with the name `UID` gets set on page load
* contents are `md5("100")`
* after trying to alter the cookie value to be `md5("0")` a `FLAG` cookie gets set

## Flag
```
encryptCTF%7B4lwa4y5_Ch3ck_7h3_c00ki3s%7D
```
Which after url decode becomes
```
encryptCTF{4lwa4y5_Ch3ck_7h3_c00ki3s}
```
