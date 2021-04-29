function login() {
    var x , y;

    // Get the value of the input field with id="numb"
    x = document.getElementById("user").value;
    y = document.getElementById("pass").value;


    document.getElementById("demo").innerHTML = y + x;

    var token = "user=%&pass=$"
    var credentialx = token.replace('%',x);
    var credential = credentialx.replace('$',y);


    document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;

      var res = JSON.parse(this.responseText);

      document.getElementById("demo").innerHTML = res;

      if (res == 'fail'){
        document.getElementById("demo").innerHTML = 'Failed to Log in'

      } else {
        document.getElementById("demo").innerHTML = 'Succesfully Logged in'
        /* Here you can continue the implementation */
        /* Maybe you can try redirecting to your main app */
      }

      }
    };
    xhttp.open("POST", "http://yourflaskapp.url.com/changethis", true);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send(credential);

}

/*    <!-- made by Alexis Wong @dyphen12 -->    */
