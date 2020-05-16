<?php
header('Content-Type: image/jpeg');

$im = imagecreatefromjpeg('image.jpg');
imagejpeg($img);
imagedestroy($img);


?>