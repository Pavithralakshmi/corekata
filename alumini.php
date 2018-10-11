login.php:
<html>
<body>
<form method="POST">
<center>
<table  border="double black" width="90%" cellpadding="5" cellspacing="0">
<tr >
<td width="10%" valign="top">
<img src ="images/NEC_Logo.png" alt="img" width=100 height=200>
</td>
<td valign="top">
<h1 align="center">NANDHA</h1>
<h2 align="center">ENGINEERING COLLEGE (Autonomous)</h2>
<h3 align="center">Affiliated to Anna University, Chennai. Approved by AICTE, Accredited by NAAC &amp; NBA<br>Included under Sections 2(f) and 12(B) of the UGC Act</h3>
</td>
</tr></table><table width="50% ">
<h4>Alumini Database</h4>

<center><h2 style="color:Tomato;">Login Page</h2>
<table cellpadding="2" width="30%" height="30%" bgcolor="gray"  align="center" cellsspacing="2">
<tr><td style="color:DodgerBlue;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspUser name</td><td><input type="text" name="uname" id="uname"></td></tr>
<br><tr><td style="color:DodgerBlue;"> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspPassword</td><td><input type="password" name="pwd" id="pwd"></td></tr>
</br></table><br></br>
<center><input type="submit" name="Login" value="Login"></p></center>
</table></form>
<marquee direction="left" behavior="alternate"><p style="color:MediumSeaGreen;">Help Line:nec@help.edu Ph_no:2290784</p></marquee>

</body>
</html>

<?php
include("db_connect.php");
if(@$_POST['Login']!="")
{
@$uname=$_POST['uname'];
@$pwd=$_POST['pwd'];
//echo $uname."  ".$pwd;
$sql="SELECT * FROM login WHERE pwd=$pwd AND uname='$uname'"; 
$result=$conn->query($sql);
if($result->num_rows > 0)
{
 header("location:register.php");
}
else
{
echo "<script type='text/javascript'>alert('Invalid login...Please try again');
window.location='login.php' ; 
</script>";
}
}
?>

alumini.php
<?php 
include('db_connect.php');
include('html_files/menu.html');
?>
<html>
<head>
<title>ALUMINI DETAILS</title>
</head>
<body>
<form action="showd.php" method="GET">
<center>
<center><h2 style="color:Tomato;">SELECT ALUMNI BATCH & YEAR</h2>
<tr><td style="color:DodgerBlue;">&nbsp&nbsp&nbspDepartment&nbsp&nbsp&nbsp<select name="Dept">
    <option value="">--Select--</option>
    <option value="Civil">Civil</option>
    <option value="Mech">Mech</option>
    <option value="ECE">ECE</option>
    <option value="E&I">E&I</option>
    <option value="CSE">CSE</option>
    <option value="IT">IT</option>
    <option value="MCA">MCA</option>
    <option value="MBA">MBA</option>
</select>
&nbsp&nbsp&nbsp&nbspBatch&nbsp&nbsp&nbsp
<select name="Batch">
    <option value="">--Select--</option>
    <option value="2014">2014</option>
    <option value="2015">2015</option>
    <option value="2016">2016</option>
    <option value="2017">2017</option>
    <option value="2018">2018</option>
    <option value="2019">2019</option>
    <option value="2020">2020</option>
    <option value="2021">2021</option>
</select></td></tr>
<br></br>
<center><input type="submit" name="submit" value="View"></p></center>
</form>
<marquee direction="left" behavior="alternate"><p style="color:MediumSeaGreen;">Help Line:nec@help.edu Ph_no:2290784</p></marquee>
</body>
</html>

dbconnect.php:
<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "accounts";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
//echo "Connected successfully";
?>

reg.php:
<?php 
include("db_connect.php");
include('html_files/menu.html');
?>
<html>
<body>
<form method="POST">
<center><br><br><br><h1>User Registration</h1></br>
<table cellspading="5" width="40%"  height="100%" bgcolor="gray"  align="center" cellsspacing="5">
<tr>
<td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRoll_no</td><td><input type="text" name="Roll_no" id="Roll_no"></td></tr>
<tr><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspName</td><td><input type="text" name="Name" id="Name"></td></tr>
<tr><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspDept</td><td><select name="Dept">
    <option value="Select"Select</option>
    <option value="Civil">Civil</option>
    <option value="Mech">Mech</option>
    <option value="ECE">ECE</option>
    <option value="E&I">E&I</option>
    <option value="CSE">CSE</option>
    <option value="IT">IT</option>
    <option value="MCA">MCA</option>
    <option value="MBA">MBA</option>
</select></td></tr>
<tr><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspClass</td><td><select name="Class">
    <option value="Select"Select</option>
    <option value="A">A</option>
    <option value="B">B</option>
    <option value="C">C</option></select></td></tr>
<tr><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspBatch</td><td><select name="Batch">
    <option value="Select"Select</option>
    <option value="2014">2014</option>
    <option value="2015">2015</option>
    <option value="2016">2016</option>
    <option value="2017">2017</option>
    <option value="2018">2018</option>
    <option value="2019">2019</option>
    <option value="2020">2020</option>
    <option value="2021">2021</option>
</select></td></tr>
<tr><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspEmail_id</td><td><input type="text" name="Email_id" id="Email_id"></td></tr>
<tr><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspPhone_no</td><td><input type="text" name="Ph_no" id="Ph_no"></td></tr>
<tr><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspAddress</td><td><input type="text" name="Address" id="Address"></td></tr>

</table><br></br>
<center><input type="submit" name="Save" value="Save"></p></center>
</form>
</body>
</html>
<?php
if(@$_POST["Save"]!="")
{
	$Roll_no=@$_POST['Roll_no'];
	$Name=@$_POST['Name'];
	$Dept=@$_POST['Dept'];
	$Class=@$_POST['Class'];
	$Batch=@$_POST['Batch'];
	$Email_id=@$_POST['Email_id'];
	$Ph_no=@$_POST['Ph_no'];
	$Address=@$_POST['Address'];

	$sql="insert into register(Roll_no,Name,Dept,Class,Batch,Email_id,Ph_no,Address) values('$Roll_no','$Name','$Dept','$Class','$Batch','$Email_id',$Ph_no,'$Address') "; 
	if($conn->query($sql) === TRUE) {
		echo "<script type='text/javascript'>\n";
		echo "alert('Registration successful');\n";
		echo "</script>"; 
	} 
	else 
	{
		echo "Error: " . $sql . "<br>" . $conn->error;
	}
	$conn->close();
}
 ?>
