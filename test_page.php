<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $surname = $_POST["surname"];
}
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Moja webstranka</title>
</head>
<body>
    <h1>Welcome to my webpage!</h1>
    <p>My name is Artemii Kaliadin</p>
    <p>I am studying 2AIN1</p>
    <p>My email is: kaliadin1@uniba.sk</p>
    <p>My photo:</p>
    <img src="images/me.jpeg" alt="my photo" width="231" height="309">
    <?php phpinfo(); ?>
</body>
</html>