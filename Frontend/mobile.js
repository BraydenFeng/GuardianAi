
const dangerousMessages = [
  { content: "Sample alert 1", author: "System", timestamp: "2025-10-20" },
  { content: "Sample alert 2", author: "System", timestamp: "2025-10-20" },
  { content: "Sample alert 3", author: "System", timestamp: "2025-10-20" },
  { content: "Sample alert 4", author: "System", timestamp: "2025-10-20" },
  { content: "Sample alert 5", author: "System", timestamp: "2025-10-20" },
  { content: "Sample alert 6", author: "System", timestamp: "2025-10-20" },
  { content: "I hate you", author: "kenneth", timestamp: "2025-10-20" },
];

let Information = { Email: "", Password: "", Username: "" };
let notlogedin = document.getElementById("loginBox");
let login = document.getElementById("logedIn");
let expanded = false;

// 📨 Send login info to backend API
async function sendLoginData(userData) {
  try {
    const response = await fetch("http://127.0.0.1:8000/create-user", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: userData.Username,
        email: userData.Email,
        password: userData.Password,
        discord_token: "token",        // Replace with actual token if needed
        discord_username: "test1234",  // Replace with actual discord username
      }),
    });

    const result = await response.text();
    console.log("API Response:", result);
    return result;
  } catch (error) {
    console.error("Error sending data to API:", error);
  }
}


function renderMessages() {
  const container = document.getElementById("logedIn");


  container.querySelectorAll(".message-box").forEach(box => box.remove());

  // Use mock data until API connects
  const visibleMessages = expanded ? dangerousMessages : dangerousMessages.slice(0, 2);

  visibleMessages.forEach(msg => {
    const box = document.createElement("div");
    box.className = "message-box bg-[#1e1e24] m-4 p-4 rounded-lg";

    box.innerHTML = `
      <p class="text-gray-200 text-sm mb-1">"${msg.content}"</p>
      <p class="text-gray-400 text-xs">${msg.author}</p>
      <p class="text-gray-500 text-xs">${msg.timestamp}</p>
    `;

    container.appendChild(box);
  });

  const toggle = document.getElementById("toggle-button");
  if (toggle) toggle.innerText = expanded ? "Show Less" : "Show More";
}


document.getElementById("loginBtn").addEventListener("click", async function () {
  Information.Email = document.getElementById("emailInput").value;
  Information.Password = document.getElementById("passwordInput").value;
  Information.Username = document.getElementById("usernameInput").value;

  console.log(Information);

  if (Object.values(Information).every(value => value)) {
    await sendLoginData(Information);

    notlogedin.style.display = "none";
    login.style.display = "block";
    let protect = document.getElementById("protections_status");
    protect.innerHTML = "Active";
    protect.className = "text-green-500 font-bold";

    // Create toggle button if it doesn't exist
    if (!document.getElementById("toggle-button")) {
      const toggleButton = document.createElement("button");
      toggleButton.id = "toggle-button";
      toggleButton.className = "btn btn-sm m-4";
      toggleButton.textContent = "Show More";
      login.appendChild(toggleButton);

      // Toggle show more / show less
      toggleButton.addEventListener("click", () => {
        expanded = !expanded;
        renderMessages();
      });
    }

    // Initial render
    renderMessages();

  } else {
    notlogedin.style.display = "block";
    login.style.display = "none";
  }
});
