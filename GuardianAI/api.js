const uid = "X25w7WKC3GuqdBM0mzQk"

//request from api and sends data to console
fetch(`http://127.0.0.1:8000/read-dangerous?=${uid}`)
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));





function fetchData(){
    fetch("http://127.0.0.1:8000")
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
