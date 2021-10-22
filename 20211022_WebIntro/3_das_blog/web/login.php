<?php
require_once ('inc/common.php');
$output='';
if( array_key_exists('Username', $_POST) && array_key_exists('Password', $_POST) ){
    $name = mysqli_real_escape_string( $conn, $_POST['Username'] );
    // Never keep passwords in plain text is a real environment
    $pass = mysqli_real_escape_string( $conn, $_POST['Password'] );
    $sql = "SELECT `name`, `permissions` FROM `users` WHERE `name`='$name' AND `password`='$pass' LIMIT 1;";
    if( $data = mysqli_query($conn, $sql) ){
        if( mysqli_num_rows($data) > 0){
            $result = mysqli_fetch_assoc($data);
            $name = $result['name'];
            $perm = $result['permissions'];
            setcookie('user', $name); // expires on browser close
            setcookie('permissions', $perm);
            $output = "You are now logged in as $name with permissions $perm";
        }else{
            $output = 'Sorry, That Username / Password is incorrect.';
        }
    }else{
        $output = 'There was a problem accessing the database, please try again. And be nice.';
    }
}else if( array_key_exists('loggout', $_GET) || array_key_exists('logout', $_POST) ){
    setcookie('user', '', time() - 3600); // set timeout to yesterday to remove cookie
    setcookie('permissions', '', time() - 3600);
    $output = 'You have been logged out.';
}

// login user, set session data in cookie
// output comment with test user info, test user only has basic permissions

 ?>
<!-- Development test account: user: JohnsTestUser, pass: AT3stAccountForT3sting -->
<!DOCTYPE html>
<html>
    <head>
        <title>Das Blog Login page</title>
    </head>
    <body>
        <p><?php echo($output?$output:'Please login here');?></p>
        <form action="?" method="post">
            <label for="Username">Username</label>
            <input type="text" name="Username" />
            <br>
            <label for="Password">Password</label>
            <input type="password" name="Password" />
            <br>
            <input type="submit" name="submit" value="Login"/>
        </form>
    </body>
</html>
