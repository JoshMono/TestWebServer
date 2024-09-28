from http.server import BaseHTTPRequestHandler, HTTPServer
from re import L
from urllib.parse import urlparse, parse_qs
import sql_database

class Views:
    @staticmethod
    def home(handler, query_params):
        file_path = "index.html"
        with open(file_path, 'r') as f:
            html = f.read()

        table_html = """
                <table class="table">
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Age</th>
            <th>Email</th>
          </tr>
        """

        users = sql_database.FetchRecords()
        for user in users:
            user_id = user[0]
            f_name = user[1]
            l_name = user[2]
            age = user[3]
            email = user[4]
            table_html += f"""
                
                <tr>
                    
                        <td>{f_name}</td>
                        <td>{l_name}</td>
                        <td>{age}</td>
                        <td>{email}</td>
                        <td>
                        
                        <input user_id={user_id} style="margin-right: 10px;" type="submit" updateButton type="button" class="btn btn-warning updateButton" value="Update">
                        <input user_id={user_id} type="submit" deleteButton type="button" class="btn btn-danger deleteButton" value="Delete">
                        </td>
                        
                </tr>
                
            """
        table_html += "</table>"
        html = html.replace("{{user_table}}", table_html)
        handler.send_response(200)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(bytes(html, "utf8"))

    @ staticmethod
    def create_get_form(handler, query_params):
        html = """
        <div class="modal fade" id="createModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Create Record</h5>
      </div>
      <div class="modal-body">
        <form id="create_form" action="/create_post_data" method="POST">    
            <table>        
                    <tr>
                        <td><label for="f_name">First Name</label></td>
                        <td><input type="text" class="form-control" placeholder="First Name" name="f_name"></td>
                    </tr>
                    <tr>
                        <td><label for="l_name">Last Name</label></td>
                        <td><input type="text" class="form-control" placeholder="Last Name" name="l_name"></td>
                    </tr>
                    <tr>
                        <td><label for="age">Age</label></td>
                        <td><input type="text" class="form-control" placeholder="Age" name="age"></td>
                    </tr>
                    <tr>
                        <td><label for="Email">Email</label></td>
                        <td><input type="text" class="form-control" placeholder="Email" name="email"></td>
                        <input type="hidden" name="id" value="{user[0]}"></td>
                    </tr>
            </table>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="submit" form="create_form" class="btn btn-primary">Create</button>
      </div>
    </div>
  </div>
</div>
        
        
        
        """
        
        
        
        html1 = """
            <form action="/create_post_data" method="POST">
                <table>
                    <tr>
                        <td><label for="f_name">First Name</label></td>
                        <td><input type="text" class="form-control" placeholder="First Name" name="f_name"></td>
                    </tr>
                    <tr>
                        <td><label for="l_name">Last Name</label></td>
                        <td><input type="text" class="form-control" placeholder="Last Name" name="l_name"></td>
                    </tr>
                    <tr>
                        <td><label for="age">Age</label></td>
                        <td><input type="text" class="form-control" placeholder="Age" name="age"></td>
                    </tr>
                    <tr>
                        <td><label for="Email">Email</label></td>
                        <td><input type="text" class="form-control" placeholder="Email" name="email"></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type="submit" type="button" class="btn btn-dark" value="Create"></td>
                    </tr>
                </table>
            </form>
   
        """
        handler.send_response(200)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(bytes(html, "utf8"))

    def create_post_data(handler, parsed_data):
        age = int(parsed_data.get("age")[0])
        a = sql_database.AddRecord(parsed_data.get("f_name")[0], 
                            parsed_data.get("l_name")[0], 
                            age, 
                            parsed_data.get("email")[0])

        handler.send_response(302)
        handler.send_header('Location', '/')
        handler.end_headers()

        
            #handler.send_response(200)
            #.send_header('Content-type', 'text/html')
            #handler.end_headers()
            #handler.wfile.write(bytes(html, "utf8"))

    def update_get_form(handler, query_params):
        user = sql_database.GetRecordFromID(query_params.get("id")[0])
        
        html = F"""
        <div class="modal fade" id="updateModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Update Record</h5>
      </div>
      <div class="modal-body">
        <form id="update_form" action="/update_post_data" method="POST">    
            <table>        
                    <tr>
                        <td><label for="f_name">First Name</label></td>
                        <td><input type="text" value="{user[1]}" class="form-control" placeholder="First Name" name="f_name"></td>
                    </tr>
                    <tr>
                        <td><label for="l_name">Last Name</label></td>
                        <td><input type="text" value="{user[2]}" class="form-control" placeholder="Last Name" name="l_name"></td>
                    </tr>
                    <tr>
                        <td><label for="age">Age</label></td>
                        <td><input type="text" value="{user[3]}" class="form-control" placeholder="Age" name="age"></td>
                    </tr>
                    <tr>
                        <td><label for="Email">Email</label></td>
                        <td><input type="text" value="{user[4]}" class="form-control" placeholder="Email" name="email"></td>
                        <input type="hidden" name="id" value="{user[0]}"></td>
                    </tr>
            </table>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="submit" form="update_form" class="btn btn-primary">Create</button>
      </div>
    </div>
  </div>
</div>
        """
        
        handler.send_response(200)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(bytes(html, "utf8"))

    def update_post_data(handler, parsed_data):
        sql_database.UpdateRecord(parsed_data.get("id")[0], 
                            parsed_data.get("f_name")[0], 
                            parsed_data.get("l_name")[0], 
                            parsed_data.get("age")[0], 
                            parsed_data.get("email")[0])

        handler.send_response(302)
        handler.send_header('Location', '/')
        handler.end_headers()

    def delete_get_form(handler, query_params):
        user = sql_database.GetRecordFromID(query_params.get("id")[0])
        
        html = F"""
        <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Confirm Delete</h5>
      </div>
      
      <div class="modal-footer">
        <form id="delete_form" action="/delete_post_data" method="POST">    
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-danger">Delete</button>
            <input type="hidden" name="id" value="{user[0]}">

        </form>
      </div>
    </div>
  </div>
</div>
        """
        handler.send_response(200)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(bytes(html, "utf8"))

    def delete_post_data(handler, parsed_data):
        sql_database.DeleteRecord(parsed_data.get("id")[0])
        handler.send_response(302)
        handler.send_header('Location', '/')
        handler.end_headers()


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_string = parsed_url.query
        query_params = parse_qs(query_string)
        if path == "/":
            Views.home(self, query_params)
        elif path == "/create_get_form":
            Views.create_get_form(self, query_params)
        elif path == "/update_get_form":
            Views.update_get_form(self, query_params)
        elif path == "/delete_get_form":
            Views.delete_get_form(self, query_params)


    def do_POST(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        parsed_data = parse_qs(post_data.decode('utf-8'))
        if path == "/create_post_data":
            Views.create_post_data(self, parsed_data)
        elif path == "/update_post_data":
            Views.update_post_data(self, parsed_data)
        elif path == "/delete_post_data":
            Views.delete_post_data(self, parsed_data)



def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(F"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()