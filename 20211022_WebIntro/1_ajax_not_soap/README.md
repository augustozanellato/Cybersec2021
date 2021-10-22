# Ajax Not Soap

## Description
Javascript is checking the login password off of an ajax call, The verification is being done on the client side.
making a direct call to the ajax page will return the expected password

RULES = you don't have access to the 'web' folder.

Be sure that the the entire folder has the right permissions.
To do it, open the terminal and write
    chmod -R +rx ./

REMEMBER: do this operation for every exercise.

To execute the exercise, do the following on the terminal

  sudo ./docker_build.sh

and then

  sudo ./docker_run.sh

Check inside docker_run the ip:port to use (in this case 127.0.0.1:8085)


## Solution
Both username and password are checked client side so the authentication can
be defeated by looking at server responses in the network tab of the browsers devtools

## Flag
```
flag{hj38dsjk324nkeasd9}
```
