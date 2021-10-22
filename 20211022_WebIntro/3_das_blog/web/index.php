<?php
    include_once('inc/common.php');
    if(array_key_exists('Permissions', $_COOKIE)){
        // if user is logged in
    }
?>
<!DOCTYPE html>
<html>
    <head>
    <link rel="style.css" type="text/css"/>
	<title>Das Blog</title>
	<style>
	    body{
		text-align:center;
	    }
	    .post{
		border:1px solid black;
		background-color:grey;
		color:white;
	    }
	    .post_title{
		text-decoration:underline;
	    }
	</style>
    </head>
    <body>
        <header>
            <h1>You have stumbled upon Das Blog</h1>
        </header>
        <div class="container">
	<?php
	    $POSTS = [];
	    if(array_key_exists('permissions', $_COOKIE) && array_key_exists('user', $_COOKIE) ){

            echo("<h3 class='welcome'>Welcome ".cleanData($_COOKIE['user'])."</h3>");

            if(preg_match('/\badmin\b/i', $_COOKIE['permissions'])){

              echo("<h4 class='welcome'>You have ADMIN permissions</h4><hr>");

              $query = "SELECT * FROM `posts`;";
              $data = mysqli_query($conn, $query);
              while($result = mysqli_fetch_assoc($data)){
                  echo( "
                    <div class='post'>
                        <h3>".$result['title']."</h3>
                        <div style='post_body'>
                            ".$result['content']."
                        </div>
                    </div>
                  ");
                }
            }else{
                echo("<h4 class='welcome'>You have DEFAULT permissions</h4><hr>");
                $query = "SELECT * FROM `posts` WHERE `permissions`='OPEN';";
                $data = mysqli_query($conn, $query);
                while($result = mysqli_fetch_assoc($data)){
                    echo("
                        <div class='post'>
                            <h3>".$result['title']."</h3>
                            <div style='post_body'>
                            ".$result['content']."
                            </div>
                        </div>
                    ");
                }
            }
        }else{
            echo("<h4 class='welcome'>You must <a href='login.php'>login</a> to view posts</h4>");
        }
	?>
        </div>
        <footer>

        </footer>
    </body>
</html>
