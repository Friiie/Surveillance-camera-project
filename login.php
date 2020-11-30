<?php
$mysqli = new mysqli("localhost","Fria","Hej","project");
// Check connection
if ($mysqli -> connect_errno) {
 echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
 exit();
}
// Query
$query_str = "SELECT * FROM users WHERE Username = '". $_POST['Username'] ."' AND password = '". $_POST['Password'] ."'";

$result = $mysqli->query($query_str);
if ($result->num_rows != 0)
{    
    if(mysqli_fetch_array($result)[8] == 1)
    {
        session_start();
        $_SESSION['Username'] = $_POST['Username'];
        header("Location: adminpage1.php");
    }
    else
    {
        session_start();
        $_SESSION['Username'] = $_POST['Username'];
        header("Location: page1.php");
    }
}

else
    header("Location: index.php");
// close connection
$mysqli->close();
?>