<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF00FF;}
</style>
</head>
<body> <center> 

<?php

$nameErr = $emailErr = "";
$name = $email =  "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = input($_POST["name"]);
    
    if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
      $nameErr = "Only letters and white space allowed"; 
    }
  }
  
  if (empty($_POST["email"])) {
    $emailErr = "Email is required";
  } else {
    $email = input($_POST["email"]);
 
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
      $emailErr = "Invalid email format"; 
    }
  }
}

function input($a) {
  $a = trim($a);
  $a = stripslashes($a);
  $a = htmlspecialchars($a);
  return $a;
}
?>
<p><span class="error">* required field</span></p>
<h2> Validation form</h2>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  Name: <input type="text" name="name">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>
  E-mail: <input type="text" name="email">
  <span class="error">* <?php echo $emailErr;?></span>
  <br><br>
  
  <center><input type="submit" name="submit" value="Submit">  </center>
</form>

<?php
echo "<h2>Input:</h2>";
echo $name;
echo "<br>";
echo $email;

?>
</center>
</body>
</html>
