<?php
    session_start();
    if(!empty($_SESSION['Username'])){
        header("Location: page1.php");
    } else{
        echo "you are not logged in";
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Surveillance Camera</title>
        <meta charset="utf-8">
        <link rel="stylesheet"
        href="https://www.w3schools.com/w3css/4/w3.css"/>
        <link rel = "stylesheet"
        type = "text/css"
        href = "mystyle.css" />
        <script>
            function displayLoginScreen(){
                var currentValue = document.getElementById('loginscreen').style.display;
                if(currentValue = "none"){
                    document.getElementById('loginscreen').style.display = "initial";
                }
            }
        </script>
    </head>
    
   <body>
       <div class="blue_gray_title">
           <h2>Surveillance camera</h2>
       </div>
        <div id="loginscreen" class="w3-animate-zoom">
            <form action="login.php" method="post">
                <h3>Login</h3>
                <label>Username</label><br>
                <input type="text" name="Username"><br>
                <label>Password</label><br>
                <input type="text" name="Password"><br><br>
                <input type="submit" value="Login"><br><br>
                <a href="create_user.html">Not registered yet?</a>
            </form>
        </div>
   </body> 
</html>