# full-stack-login

A simple login module with an API made under Python and HTML5 Login page for an SQL Database.

_Forked from Prisma Login API_

#### Features:
- Username
- Password

#### Notes:
- You just need to connect it to your own database.

## How it works?

The login-module works with a client-server architecture.

1) The Client-side of the module is in the 'client' folder, it contains an HTML5 web app.

2) The Server-side is in the 'api' folder, it contains a python flask app.

3) The SQL Database needs to have at least Username and Password columns.

## Instructions:

### 1. API Folder

In the api folder, Open "database.py" and change the **"mothercon"** objects with the tokens of your database:

    mothercon = pymysql.connect(host='yourhost',
                                user='youruser',
                                password='password1234',
                                db='dbname')

### 2. Client Folder

Second, in the client folder, open "login.js" and replace _"http://yourflaskapp.url.com/changethis"_ with your Flask App URL:

    xhttp.open("POST",
    "http://yourflaskapp.url.com/changethis", 
    true);

### 3. Run
Run requirements.txt

    pip install requirements.txt

Run the following code:

    python3 Login-app.py

Then, open "login.html" and try.

**Note:** *It is just a login module, To full testing you should register a user via SQL syntax. (for details on the form of the data expected by the API please continue reading).*


### How should I design my database?

The **most basic database** should run with this code.

The code expects a database like this:

User, Password.

*(Not exactly like this but if you have those columns the code should work.)*


### Production Environment Notes

I do not recommend the use of this code in a production environment, you could try but, this code is intended to work as an starting point for helping in app development and prototyping. 

The login app does not have any proven security implementation, or at least a hard one. 

The SSID subroutine works as an starting point for  replacement or improving and putting your own security implementation.

If you are going to use this in a production environment anyway, you should set up a **Virtual Environment** first.





