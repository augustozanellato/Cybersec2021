<?php
// see if username was given
if(array_key_exists('username', $_GET)){
  // get username
  $username= $_GET['username'];

  // get expected username
  ob_start(); // start reading of username file
  include 'get_username.php';
  $file = ob_get_clean(); // retrieve output from username file, stop buffering

  // see if username is correct (trim and preg_replace are used to remove newlines)
  if(md5($username) == trim(preg_replace('/\s\s+/', ' ', $file))){
    //flag{sd90J0dnLKJ1ls9HJed}
    echo "ZmxhZ3tzZDkwSjBkbkxLSjFsczlISmVkfQ==";// return flag if username is correct
  }else{
    echo "Username is incorrect";// if username is incorrect
  }

}else{
  echo "Username required";// if no username, say so
}
?>
