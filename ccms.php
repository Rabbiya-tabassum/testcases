<?php
 
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "ccms";
 
// Create connection
$conn = new mysqli($servername,$username, $password, $dbname);
 
// Check connection
if ($conn->connect_error) {
    die("Connection failed: ". $conn->connect_error);
}
	$password=filter_input(INPUT_POST,'password');
	$psw_confirm=filter_input(INPUT_POST,'psw_confirm');

	if($password==$psw_confirm){

	$username=filter_input(INPUT_POST,'username');
	$email=filter_input(INPUT_POST,'email');
	$phonenumber=filter_input(INPUT_POST,'phonenumber');
        

    $sql = "INSERT INTO user (username,email,password,psw_confirm,phonenumber) VAlUES ('$username','$email','$password','$psw_confirm','$phonenumber')";
    }
if ($conn->query($sql) === TRUE) {
    //echo "record inserted successfully";
	header("Location:login.html");
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
?>