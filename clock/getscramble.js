const outputElement2 = document.getElementById('scramble');

function getCsvData2(dataPath) {
    const request = new XMLHttpRequest();
    request.addEventListener('load', (event) => {
        const response = event.target.responseText;
        convertArray2(response);
    });
    request.open('GET', dataPath, true);
    request.send();
}

function convertArray2(data) {
    const dataArray = [];
    const dataString = data.split('\n');
    for (let i = 0; i < dataString.length; i++) {
        dataArray[i] = dataString[i].split(',');
    }
    let insertElement = '';
    dataArray.forEach((element) => {
        element.forEach((childElement) => {
            insertElement += `<tr><td>${childElement}</td></tr>`
        });
    });
    //alert(insertElement)
    outputElement2.innerHTML = insertElement;
}

getCsvData2('../scramble.csv');