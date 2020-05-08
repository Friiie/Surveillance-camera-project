<?php
$mysqli = new mysqli("localhost", "root", "", "userlogin");

//Check connection
if($mysqli -> connect_errno){
    echo "Failed to connect to MySQL" . $mysqli->connect_error;
    exit();

}

//Query
$query_str = "INSERT INTO users (pseudo, password, first_name, last_name)
VALUES('". $_POST['pseudo'] ."', '". $_POST['password'] ."', '". $_POST['firstname'] ."',
'". $_POST['lastname'] ."')";

echo "MySql will execute the query: " . $query_str;
$result = $mysqli->query($query_str);

if (!$result){
    echo("Error description: " . mysqli_error($mysqli));
    exit();
}
else{
    echo "<hr>Your account has been successfully created.<br>";
    echo "Click <a href='menu.php'>here</a> to get back to the menu and log in.";
}

//close connection
$mysqli->close();
?>