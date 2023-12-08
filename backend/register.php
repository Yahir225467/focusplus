<?php
$correo = $_POST['exampleInputEmail1'];
$pass = $_POST['exampleInputPassword1'];
$name = $_POST['nombre'];
$lastname = $_POST['apellidos'];

include 'conexion.php';

$sql = "SELECT correo FROM usuarios WHERE correo = '".$correo."'";
$resultado = $pdo->query($sql);

if ($resultado->rowCount() > 0) {
	$data = "Ya existe un usuario con ese correo, registre otro correo";
	Autentificacion($data);
}
else{
    $sql = "INSERT INTO usuarios (nombre, apellido, correo, pass) 
	VALUES ('".$name."', '".$lastname."','".$correo."', '".$pass."')";
	$r = $pdo->query($sql);
	$data = "Bienvenido";
	Autentificacion($data);
}

function Autentificacion($data){
	echo $data;
	exit();
}

?>