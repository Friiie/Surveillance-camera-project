<?php

    $mysqli = new mysqli("localhost","Fria","Hej","project");
    // Check connection
    if ($mysqli -> connect_errno) {
    echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
    exit();
    }

    $names = array();

    $query_str = "SELECT first_name, last_name FROM users";
    $result = $mysqli->query($query_str);
    while($row = $result->fetch_assoc()) {
        array_push($names, $row["first_name"] . " " . $row["last_name"]);
	}
    echo json_encode($names);

?>