let Information = {Email: "", Password: "", Username: ""};
let notlogedin = document.getElementById("loginBox");
let login = document.getElementById("logedIn");
document.getElementById("loginBtn").addEventListener("click", function() {
  Information.Email = document.getElementById("emailInput").value;
  Information.Password = document.getElementById("passwordInput").value;
  Information.Username = document.getElementById("usernameInput").value;
  
  console.log(Information);

  if (Object.values(Information).every(value => value)) {
    notlogedin.style.display = "none";
    login.style.display = "block";
  } else {
    notlogedin.style.display = "block";
    login.style.display = "none";
  }
});

if 
