const outputElement3 = document.getElementById('ranking_yesterday');

function getCsvData3(dataPath) {
    const request = new XMLHttpRequest();
    request.addEventListener('load', (event) => {
        const response = event.target.responseText;
        convertArray1(response);
    });
    request.open('GET', dataPath, true);
    request.send();
}

function convertArray3(data) {
    const dataArray = [];
    const dataString = data.split('\n');
    for (let i = 0; i < dataString.length; i++) {
        dataArray[i] = dataString[i].split(',');
    }
    let insertElement = '<tr><td>順位</td><td>日時</td><td>名前</td><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td><td>5th</td><td>avg</td></tr>';
    let i = 1;
    dataArray.forEach((element) => {
        insertElement += '<tr><td>';
        insertElement += String(i);
        insertElement += '</td>'
        element.forEach((childElement) => {
            insertElement += `<td>${childElement}</td>`
        });
        insertElement += '</tr>';
        i += 1;
    });
    outputElement3.innerHTML = insertElement;
}

getCsvData3('data_yesterday.csv');
