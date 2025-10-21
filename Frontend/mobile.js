let Information = {Email: "", Password: "", Username: ""};
let notlogedin = document.getElementById("loginBox");
let login = document.getElementById("logedIn");
let expanded = false;



async function sendLoginData(userData) {
  try {
    const response = await fetch("http://127.0.0.1:8000/create-user", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: userData.Username,
        email: userData.Email,
        password: userData.Password,
        discord_token: "token",  // Replace with actual token if needed
        discord_username: "test1234",  // Replace with actual discord username
      })
    });

    const result = await response.text();
    console.log("API Response:", result);
    return result;
  } catch (error) {
    console.error("Error sending data to API:", error);
  }
}


document.getElementById("loginBtn").addEventListener("click",function() {
  Information.Email = document.getElementById("emailInput").value;
  Information.Password = document.getElementById("passwordInput").value; // ✅ fixed: was getElementByIdd
  Information.Username = document.getElementById("usernameInput").value;
  
  console.log(Information);

  function renderMessages(){
    const container = document.getElementById("logedIn");
    container.innerHTML = "";

    // change dangerousmessages to the real data from the api
    const visibleMessages  = expanded ? dangerousMessages : dangerousMessages.slice(0,3); // ✅ fixed spacing/typo

    visibleMessages.forEach(msg => { // ✅ fixed: was visivbleMessage

        const box = document.createElement("div");
        //fix the stuff inside to make it look better later
        box.className = "bg-[#1e1e24] m-4 p-4 rounded-lg";

        box.innerHTML = `
        <p class="text-gray-200 text-sm mb-1">"${msg.content}"</p>
        <p class="text-gray-400 text-xs">${msg.author}</p>
        <p class="text-gray-500 text-xs">${msg.timestamp}</p>
        `;

        container.appendChild(box);

    });

    document.getElementById('toggle-button').innerText = expanded ? 'Show Less' : 'Show More';  
  } 

  document.getElementById('toggle-button').addEventListener('click', () => {
    expanded = !expanded;
    renderMessages();
  });

  // Initial render
  renderMessages();

  if (Object.values(Information).every(value => value)) {

    await sendLoginData(Information);
    
    notlogedin.style.display = "none";
    login.style.display = "block";
    const toggleButton = document.createElement("button"); 
    toggleButton.className = "btn btn-sm m-4";
    toggleButton.textContent = "Toggle"; 
    login.appendChild(toggleButton);

  } else {
    notlogedin.style.display = "block";
    login.style.display = "none";
  }
});
