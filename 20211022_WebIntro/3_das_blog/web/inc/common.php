<?php
session_start();
include_once('db_init.php');
function cleanData($str) {
    $str = urldecode ($str );
    $str = filter_var($str, FILTER_SANITIZE_STRING);
    $str = filter_var($str, FILTER_SANITIZE_SPECIAL_CHARS);
    return $str ;
}
?>
