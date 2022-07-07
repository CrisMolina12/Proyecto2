var currentTime = new Date();
var year = currentTime.getFullYear();
var month = currentTime.getMonth() + 1;
const root = document.getElementById("root");

fetch(`https://apis.digital.gob.cl/fl/feriados/${year}/${month}`)
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        root.innerText = data[0].nombre;
    });