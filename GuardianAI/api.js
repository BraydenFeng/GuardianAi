
//request from api and sends data to console
fetch("apiUrl/hello")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));

