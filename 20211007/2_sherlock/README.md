Solution for this challenge is provided as a [CyberChef](https://gchq.github.io/CyberChef/) recipe:
```
Find_/_Replace({'option':'Regex','string':'[^A-Z]'},'',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'ZERO'},'0',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'ONE'},'1',true,false,true,false)
From_Binary('Space',8)
```
