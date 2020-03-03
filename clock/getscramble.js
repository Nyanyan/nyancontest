const outputElement2 = document.getElementById('scramble');

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
    let insertElement = '<tr><td>日時</td><td>名前</td><td>1st</td><td>3nd</td><td>3rd</td><td>4th</td><td>5th</td><td>avg</td></tr>';
    dataArray.forEach((element) => {
        insertElement += '<tr>';
        element.forEach((childElement) => {
            insertElement += `<td>${childElement}</td>`
        });
        insertElement += '</tr>';
    });
    //alert(insertElement)
    outputElement2.innerHTML = insertElement;
}

getCsvData('../scramble.csv');