import sys

footer="""
<footer class="page-footer fixed-bottom">

  <!-- Copyright -->
  <div class="footer-copyright text-center card-footer ">© 2019
    Copyright: FEI - 31
  </div>
  <!-- Copyright -->

</footer> 
"""

header="""
<nav class="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
  <a class="navbar-brand col-sm-3 col-md-2 mr-0 " href="index.py">University Students <br> Testing Platform</a>
  <input class="form-control form-control-dark w-75 " type="text" placeholder="Search" aria-label="Search">
  <ul class="navbar-nav px-3">
    <li class="nav-item text-nowrap">
      <a class="nav-link" href="login.py">Sign in</a>
    </li>
  </ul>
</nav>

<div class="container-fluid">
  <div class="row">
    <nav class="col-md-2 d-none d-md-block bg-light sidebar">
      <div class="sidebar-sticky">
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link" href="index.py">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
              <span data-feather="home"></span>
              Головна<span class="sr-only">(current)</span>
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</div>
"""
ErorLogin="""
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

	%s
	<link rel="shortcut icon" href="https://moodle.oa.edu.ua/theme/image.php/boost/theme/1547721604/favicon">
	<title>University Students Testing Platform</title>
   <style type="text/css">
    .btncenter{
    float: none;
    margin: auto;
    margin-top:200px;
}
  </style>
</head>
	
<body>
      <div class="modal-body">
        <h3 id="error"></h3>
        <h3 id="error1"></h3>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
  </div>
</div>
</form>

<script type="text/javascript">

function check(){
  logins();
  pass();
}

function logins(login){
  var login =document.getElementById("usr").value;
var numeric = new RegExp("[0-9]{7}", "g")
var check=login.replace(numeric,"r")
if(true){
  document.getElementById("error").innerHTML = "Login is true";
}else{
    document.getElementById("error").innerHTML = "Login is incorect";
  return false;
}
}


function pass(Password){
  var pass =document.getElementById("pwd").value;
var numeric = new RegExp("[0-9]{7}", "g")
var check=pass.replace(numeric,"r")
if(true){
 document.getElementById("error1").innerHTML = "Pasword is true";
}else{
  document.getElementById("error1").innerHTML = "Pasword is incorect";
  return false;
}
}
</script>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
</body>
</html>
"""