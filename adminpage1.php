<?php
    session_start();
    if(!empty($_SESSION['Username'])){
        echo "You are logged in as <b>" . $_SESSION['Username'] . "</b>(<a href='destroy_session.php'>logout</a>)";
    } else{
        header("Location: index.php");
    }
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Surveillance camera</title>
        <meta charset="utf-8">
        <link rel = "stylesheet"
        type = "text/css"
        href = "mystyle.css" />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        
        <script>

            function get_raspi_data(first_value, second_value, camera_data)
            {
                if (first_value != second_value)
                {
                    get_camera_data(camera_data);
                    document.getElementById('raspi').style.color = "green";
                    document.getElementById('raspi').innerHTML = "Raspberry pie ONLINE";
                }
                else{
                    document.getElementById('raspi').style.color = "red";
                    document.getElementById('raspi').innerHTML = "Raspberry pie OFFLINE";
                    document.getElementById('camerastatus').style.color = "red";
                    document.getElementById('camerastatus').innerHTML = "Camera sensor OFFLINE";
                }
                
                
                return 0;
            }

            function get_camera_data(data)
            {
                if(data == 1)
                {
                    document.getElementById('camerastatus').style.color = "green";
                    document.getElementById('camerastatus').innerHTML = "Camera sensor ONLINE";
                }
                return 0;
            }

            function get_motion_data(data)
            {
                if(data == 1)
                {
                    document.getElementById('motionsensor').style.color = "green";
                    document.getElementById('motionsensor').innerHTML = "Motion sensor DETECTED";
                }
                else{
                    document.getElementById('motionsensor').style.color = "red";
                    document.getElementById('motionsensor').innerhtml = "Motion sensor IDLE";
                }
                return 0;
            }

            var check_raspberry = setInterval(function(){
                var first_value;
                var date = new Date();
               $.getJSON('get_rasp_info.php', function(data){
                        $("#responsecontainer").html(data.message);
                        first_value = data[3];
                        get_motion_data(data[1]);
                        setTimeout(check_raspberry2,2000,first_value);
                        });
                    }
               
             , 5000);

            function check_raspberry2(first_value){
                var second_value;
                var camera_data;
                $.getJSON('get_rasp_info.php', function(data){
                    $("#responsecontainer").html(data.message);
                    second_value = data[3];
                    camera_data = data[2];
                    get_raspi_data(first_value, second_value, camera_data);
                });
             }
             
             function getUsers(){
                $.getJSON('get_all_users.php', function(data){
                    $("#responsecontainer").html(data.message);
                    var names_length = data.length;
                    for (var i = 0; i < names_length; i++) {
                        show_name_in_list(data[i]);
                    }
                });
             }

             function show_name_in_list(name){
                 var list = document.getElementById('userlist')
                var entry = document.createElement('li');
                entry.appendChild(document.createTextNode(name));
                list.appendChild(entry);
             }

        </script>
    </head>
    <body>
       <div class="blue_gray_title">
           <h2>Surveillance Camera</h2>
       </div>
       <div class="central_part">
        <div id="contents">
        <h2>Camera feed:</h2>
        <img src="stream.php" height="500" width="670" ></img>
        </div>
        <div id="status">
            <br>
            <br>
            <br>
            <h2> System status: </h2>
            <br> 
            <div class="systemstatuses">
                <h3><label id="raspi"> Raspberry pie OFFLINE </label></h3> 
                <h3><label id="camerastatus"> Camera sensor OFFLINE </label></h3> 
                <h3><label id="motionsensor"> Motion sensor IDLE </label></h3>
            </div>
        </div>
        <div id="adminbox">
            <h2> List of users </h2>
            <button type="button" onclick="getUsers();"> See all users </button>
             <ul id="userlist">


             </ul>
        
        </div>
   </body> 
</html> 