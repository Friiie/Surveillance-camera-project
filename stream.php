<?php
    set_time_limit(0);
    $fp = fsockopen ("10.0.1.28", 8000, $errno, $errstr, 30);
    if (!$fp) {
        echo "$errstr ($errno)<br>\n";
    } else {
        fputs ($fp, "GET / HTTP/1.0\r\n\r\n");
        while ($str = trim(fgets($fp, 4096)))
                header($str);
                fpassthru($fp);
                fclose($fp);
    }

?>

