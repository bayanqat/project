import webbrowser
import os
 
O = open('Untitled-1.html', 'w')
html_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>My Web Page</title>
        <style>
         body {
            
            height: 100vh; 
            background-color: #f1d5cf; 
        }
        .container {
            text-align:center;
        }
        </style>
    </head>
    <body>
        <h2 align="center">Welcome in my web page </h2>
        <div class="container">
            <img src="c:\\Users\\DELL\\OneDrive - Philadelphia University\\Desktop\\Desktop\\project pyweb bayan Qatanani\\WhatsApp Image 2024-02-10 at 20.12.54_50497411.jpg" alt="Your Image" width="600" height="400">
        </div>
        <p>My name is bayan , I`m 20 years old , I study software Engineering</p>
        <ul>
            
            <li>My Hobbies</li>
            <li>Drawing </li>
            <li>Reading </li>
       
        </ul>
        <textarea rows="5" cols="80">
           You can type text in here.
        </textarea>
        <div class="container" >
            <footer>
            &copy; 2024 
            </footer>
        </div>
        
    </body>

</html>
"""

O.write(html_template)
O.close()
filename = 'file:///'+os.getcwd()+'/' + 'Untitled-1.html'
webbrowser.open_new_tab(filename)
