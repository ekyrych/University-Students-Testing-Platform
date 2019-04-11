import sys
import Styles
import Blocks

page="""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="shortcut icon" href="https://moodle.oa.edu.ua/theme/image.php/boost/theme/1547721604/favicon">
  <title>%s</title>
  <style type="text/css">
    .btncenter{
    float: none;
    margin: auto;
    margin-top:200px;
}
  </style>
  %s
</head>
  
<body>
%s
<form action="auntification.py" method="post" class="col-md-9 ml-sm-auto col-lg-10 px-4">
    <div class="d-md-table pt-3 btncenter ">
        <div class="form-group ">
          <label for="usr">Name:</label>
          <input type="text" class="form-control" name="user">
        </div>
        <div class="form-group">
          <label for="pwd">Password:</label>
          <input type="password" class="form-control" name="password">
        </div>
        <div class="form-group text-center ">
            <br>
            <button class="btn btn-outline-primary ">Sing in </button>
        </div>  
    </div>
    
</form>
    %s
</body>
</html>
"""
print('Content-type: text/html\n')
print(page%("USTP Sing in",Styles.style,Blocks.header,Blocks.footer))

