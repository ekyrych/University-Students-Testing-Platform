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
	%s
</head>
	
<body>
    %s
    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-4 pb-2 mb-3 border-bottom">
        <h1 class="h2">Dashboard</h1>
      </div>

        <!--  list of subjects -->
        <div class="container col-auto w-78">  
          <div class="row">
              %s
          </div>
        </div>

        <!-- Table -->
      <h2 class="border-bottom">Info</h2>
      <div class="table-responsive text-center w-78 centered">
        <table class="table table-striped table-sm">
			<thead>
				<tr>
					<th>#</th>
					<th>Name</th>
					<th>Groop</th>
					<th>Date</th>
          <th>Subject</th>
				</tr>
			</thead>
       <tbody>
        %s
        </tbody>
          </table>
      </div>
    </main>
    %s
</footer> 
</body>
</html>
"""
member="""
<tr>
    <td>%s</td>
    <td>Pavlo</td>
    <td>Fei-31</td>
    <td>09.03.19</td>
    <td>NAN</td>
</tr>
"""

subject="""
 <div class="bg-light rounded w-50 border-сustom">
        <a href="teach.html" class="active link nav-link pb-0 "><h2 class="col-form-legend">Subject Name</h2></a>
        <h5 class="pl-3 pb-2">Викладач: <a href="#">XIO</a></h5>
 </div>           
"""
membercontent=""""""
listofsubject=""""""
for number in range(5):
    membercontent+=member%(number+1)
for number in range(10):
    listofsubject+=subject
print('Content-type: text/html\n')
print(page%("University Students Testing Platform",Styles.style,Blocks.header,listofsubject, membercontent,Blocks.footer))
