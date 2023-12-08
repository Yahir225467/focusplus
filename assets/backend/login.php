<?php

$correo = $_POST['exampleInputEmail1'];
$pass = $_POST['exampleInputPassword1'];

include 'conexion.php';

$sql = "SELECT correo FROM usuarios WHERE correo = '".$correo."'";
$resultado = $pdo->query($sql);
$sql2 = "SELECT pass FROM usuarios WHERE pass = '".$pass."' AND correo = '".$correo."'";
$resultado2 = $pdo->query($sql2);

if ($resultado->rowCount() < 1) {
	$data = "No existe un usuario con ese correo";
	Autentificacion($data);
}
if ($resultado2->rowCount() < 1) {
	$data = "La contraseña que se a puesto es incorrecta";
	Autentificacion($data);
}
else{
	$data = "Bienvenido";
	Autentificacion($data);
}

function Autentificacion($data){
	echo $data;
	exit();
}
?>