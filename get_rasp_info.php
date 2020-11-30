<?php

    $mysqli = new mysqli("localhost","Fria","Hej","project");
    // Check connection
    if ($mysqli -> connect_errno) {
    echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
    exit();
    }
    $query_str = "SELECT * FROM systabell WHERE id = '1'";
    $result = $mysqli->query($query_str);
    $raspi = mysqli_fetch_array($result);
    mysqli_free_result($result);
    echo json_encode($raspi);
        

?>