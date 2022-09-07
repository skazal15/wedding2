<?php
include_once("config.php");
$postdata = file_get_contents("php://input");
$request = json_decode($postdata);
if(isset($postdata) && !empty($postdata)){
    $nama = mysqli_real_escape_string($mysqli,trim($request->nama));
    $doa = mysqli_real_escape_string($mysqli,trim($request->doa));
    $hadir = mysqli_real_escape_string($mysqli,trim($request->hadir));
    $sql = "INSERT INTO wish (nama,doa,hadir) 
    VALUES ('$nama','$doa','$hadir')";

    if($mysqli->query($sql)==TRUE){
        $authdata = [
            'nama'=>$nama,
            'doa'=>$doa,
            'hadir'=>$hadir,
            'id'=>mysqli_insert_id($mysqli)
        ];
    }
}
