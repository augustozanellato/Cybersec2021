<?php
    $flag = "encryptCTF{4lwa4y5_Ch3ck_7h3_c00ki3s}";
    if(!isset($_COOKIE["UID"]))
        setcookie("UID", md5("100"),time()+60*60*24*2);
    else {
        if(strtolower($_COOKIE["UID"])==md5("0"))
            setcookie("FLAG", $flag);
        else
            setcookie("FLAG","encryptCTF{y0u_c4nt_U53_m3}");
    }
?>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hidden</title>
</head>

<body>
    <h2>Hey You, yes you!<br>are you looking for a flag, well it's not here bruh!<br>Try someplace else<h2>
</body>

</html>
