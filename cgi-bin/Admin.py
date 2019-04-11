import Styles
import sys
import Blocks
page="""
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">

    <title>University Students Testing Platform</title>

  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

	%s
	<link rel="shortcut icon" href="https://moodle.oa.edu.ua/theme/image.php/boost/theme/1547721604/favicon">

  <!-- TABLE -->
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/select/1.3.0/css/select.dataTables.min.css">
    
  <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.3.1.js"></script>
  <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
  <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/select/1.3.0/js/dataTables.select.min.js"></script>

  <script type="text/javascript" class="init">
  $(document).ready(function() {
  $('#example td:nth-child(5)').addClass('password');
  $('#example').DataTable( {
    columnDefs: [ {
      orderable: false,
      className: 'select-checkbox',
      targets:   0
    } ],
    select: {
      style:    'multi+shift',
      selector: 'td'
    },
    order: [[ 1, 'asc' ]]
  } );
} );
  </script>
<style type="text/css">
  #example{
    font-stretch: extra-condensed;
  }
.password{ -webkit-text-security: disc;}
</style>

</head>
	
<body>
<nav class="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
  <a class="navbar-brand col-sm-3 col-md-2 mr-0 " href="index.html">University Students <br> Testing Platform</a>
  <input class="form-control form-control-dark w-75 " type="text" placeholder="Search" aria-label="Search">
  <ul class="navbar-nav px-3">
    <li class="nav-item text-nowrap">
      <a class="nav-link" href="login.html">Sign out</a>
    </li>
  </ul>
</nav>

<div class="container-fluid">
  <div class="row">
    <nav class="col-md-2 d-none d-md-block bg-light sidebar">
      <div class="sidebar-sticky">
        <ul class="nav flex-column">
          <li class="nav-item">
          	<a class="nav-link" href="index.html">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
              <span data-feather="home"></span>
              Головна<span class="sr-only">(current)</span>
            </a>
          </li>
			    <li class="nav-item">
                <a class="nav-link active" href="#" style="">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                  Customers
                </a>
          </li>
        </ul>
      </div>
    </nav>
</div>
</div>
    
    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-4 pb-2 mb-3 border-bottom">
        <h2>Students database</h2>
          <div class="btn-toolbar mb-2 mb-md-0">
              <div class="btn-group mr-2">
                <div class="btn-group" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-outline-secondary " data-toggle="modal" data-target="#teachModal">Add teach</button>
  <button type="button" class="btn btn-outline-secondary" data-toggle="modal" data-target="#studentModal">Add student</button>
</div>
</div>
</div>
<!-- Modal -->
<div class="modal fade" id="teachModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add teacher</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="">
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Прізвице:</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Ім'я:</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Вчене звання:</label>
            <select class="form-control border-primary" id="exampleSelect1">
            <option disabled selected></option>
            <option>Доцент</option>
            <option>Професор</option>
            <option>Асистент</option>
            </select>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Login:</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Password:</label>
            <input type="text" class="form-control" required>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <input type="submit" class="btn btn-primary"/>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="studentModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add student</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="">
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Прізвице:</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Ім'я:</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Група:</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Login:</label>
            <input type="text" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Password:</label>
            <input type="text" class="form-control" required>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <input type="submit" class="btn btn-primary"/>
      </div>
    </div>
  </div>
</div>
              </div>
            </div>
        </div>
              <div class="table-responsive table-sm wide comments example pb-5">
       
        <table id="example" class="display">
          <thead>
            <tr>
              <th></th>
              <th>ПІ</th>
              <th style="width: 300px">Група</th>
              <th>Логін</th>
              <th>Пароль</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td></td>
              <td>Tiger Nixon</td>
              <td>System Architect</td>
              <td>Edinburgh</td>
              <td>61</td>
            </tr>
            <tr>
              <td></td>
              <td>Garrett Winters</td>
              <td>Accountant</td>
              <td>Tokyo</td>
              <td>63</td>
            </tr>
            <tr>
              <td></td>
              <td>Ashton Cox</td>
              <td>Junior Technical Author</td>
              <td>San Francisco</td>
              <td>66</td>
            </tr>
            <tr>
              <td></td>
              <td>Cedric Kelly</td>
              <td>Senior Javascript Developer</td>
              <td>Edinburgh</td>
              <td>22</td>
            </tr>
            <tr>
              <td></td>
              <td>Airi Satou</td>
              <td>Accountant</td>
              <td>Tokyo</td>
              <td>33</td>
            </tr>
            <tr>
              <td></td>
              <td>Brielle Williamson</td>
              <td>Integration Specialist</td>
              <td>New York</td>
              <td>61</td>
            </tr>
            <tr>
              <td></td>
              <td>Herrod Chandler</td>
              <td>Sales Assistant</td>
              <td>San Francisco</td>
              <td>59</td>
            </tr>
            <tr>
              <td></td>
              <td>Rhona Davidson</td>
              <td>Integration Specialist</td>
              <td>Tokyo</td>
              <td>55</td>
            </tr>
            <tr>
              <td></td>
              <td>Colleen Hurst</td>
              <td>Javascript Developer</td>
              <td>San Francisco</td>
              <td>39</td>
            </tr>
            <tr>
              <td></td>
              <td>Sonya Frost</td>
              <td>Software Engineer</td>
              <td>Edinburgh</td>
              <td>23</td>
            </tr>
            <tr>
              <td></td>
              <td>Jena Gaines</td>
              <td>Office Manager</td>
              <td>London</td>
              <td>30</td>
            </tr>
            <tr>
              <td></td>
              <td>Quinn Flynn</td>
              <td>Support Lead</td>
              <td>Edinburgh</td>
              <td>22</td>
            </tr>
            <tr>
              <td></td>
              <td>Charde Marshall</td>
              <td>Regional Director</td>
              <td>San Francisco</td>
              <td>36</td>
            </tr>
            <tr>
              <td></td>
              <td>Haley Kennedy</td>
              <td>Senior Marketing Designer</td>
              <td>London</td>
              <td>43</td>
            </tr>
            <tr>
              <td></td>
              <td>Tatyana Fitzpatrick</td>
              <td>Regional Director</td>
              <td>London</td>
              <td>19</td>
            </tr>
            <tr>
              <td></td>
              <td>Michael Silva</td>
              <td>Marketing Designer</td>
              <td>London</td>
              <td>66</td>
            </tr>
            <tr>
              <td></td>
              <td>Paul Byrd</td>
              <td>Chief Financial Officer (CFO)</td>
              <td>New York</td>
              <td>64</td>
            </tr>
            <tr>
              <td></td>
              <td>Gloria Little</td>
              <td>Systems Administrator</td>
              <td>New York</td>
              <td>59</td>
            </tr>
            <tr>
              <td></td>
              <td>Bradley Greer</td>
              <td>Software Engineer</td>
              <td>London</td>
              <td>41</td>
            </tr>
            <tr>
              <td></td>
              <td>Dai Rios</td>
              <td>Personnel Lead</td>
              <td>Edinburgh</td>
              <td>35</td>
            </tr>            
          </tbody>
          <tfoot>
            <tr>
              <th></th>
              <th>ПІ</th>
              <th>Група</th>
              <th>Логін</th>
              <th>Пароль</th>
            </tr>
          </tfoot>
        </table>
</div>
</main>
<footer class="page-footer fixed-bottom">

  <!-- Copyright -->
  <div class="footer-copyright text-center card-footer ">© 2019
    Copyright: FEI - 31
  </div>
  <!-- Copyright -->

</footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>	
</body>
</html>
"""
print('Content-type: text/html\n')
print(page%(Styles.style))