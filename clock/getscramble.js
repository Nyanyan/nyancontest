const outputElement = document.getElementById('scramble');

function getCsvData(dataPath) {
    const request = new XMLHttpRequest();
    request.addEventListener('load', (event) => {
        const response = event.target.responseText;
        convertArray(response);
    });
    request.open('GET', dataPath, true);
    request.send();
}

function convertArray(data) {
    const dataArray = [];
    const dataString = data.split('\n');
    for (let i = 0; i < dataString.length; i++) {
        dataArray[i] = dataString[i].split(',');
    }
    let insertElement = '';
    dataArray.forEach((element) => {
        insertElement += '<tr>';
        element.forEach((childElement) => {
            insertElement += `<td>${childElement}</td>`
        });
        insertElement += '</tr>';
    });
    //alert(insertElement)
    outputElement.innerHTML = insertElement;
}

getCsvData('data.csv');