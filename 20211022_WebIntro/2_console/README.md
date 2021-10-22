* The MD5ed string isn't checked on the server side
* `/1/key.php` checks if the request originated from XHR or something like that
Flag can thus be obtained by executing
```js
   $.ajax({
        type: 'GET',
        url: '1/key.php',
        success: function (file_html) {
            foo.innerHTML=(file_html)
        }
    });
```
## Flag
```
flag{console_controls_js}
```
