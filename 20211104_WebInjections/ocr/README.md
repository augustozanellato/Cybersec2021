## Solution
* after some trial and error it looks like the application is running an ocr on the input string and then `eval()`ing the text
* while scanning endpoints using ffuf (`ffuf -w SecLists/Discovery/Web-Content/common.txt -u http://localhost:5000/FUZZ`) a `/debug` endpoint appeared, it just dumps the app source code
* looks like the flag is in a string var named `x`
* we can't exfiltrate it directly because the output is casted to int before being sent back
* we can get the string length and then iterate on the string contents and get them character by character
(See `solution.py`)
## Flag
```
INSA{0cr_L0ng}
```
