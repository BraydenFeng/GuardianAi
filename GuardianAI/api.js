//request from api and sends data to console
fetch("apiUrl/hello")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));





function fetchData(){
    fetch("url")
    .then(response => response.json)
    .then(newData => {

        checkChange(newData);

    })
    .catch(error => console.log("There was an error checking for data"))
}

setInterval(fetchData , 5000);  


//This is to store the Or change the data
let oldData = null;

function checkChange(newData){

    if (oldData == null){
        oldData = newData;
        console.log("data has been fetched")
        return;
    }
    
    if (JSON.stringify(newData) !==  JSON.strinfy(oldData)){
        console.log('data has been changed/added');
    
    oldData = newData;

    }else{
        console.log("no changes have been detected");
    
    }
}


function updateUI(data){
    console.log("UI has been changed",data);
}
