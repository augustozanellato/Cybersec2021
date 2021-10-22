<?php
if(array_key_exists('HTTP_REFERER', $_SERVER)&&preg_match('/(\/%23console.html)+/', $_SERVER['HTTP_REFERER'])){
    echo('Password: flag{console_controls_js}');
}else{
    echo("It's not that easy, but nice try. <br/><b> Go back and try again</b>");
}
?>
