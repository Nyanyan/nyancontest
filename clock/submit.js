function submitForm(){
    alert(document.getElementById('name') == "")
    alert(document.getElementById('1st') == "")
    alert(document.getElementById('2nd') == "")
    alert(document.getElementById('3rd') == "")
    alert(document.getElementById('4th') == "")
    alert(document.getElementById('5th') == "")
    if (document.getElementById('name') == "" || document.getElementById('1st') == "" || document.getElementById('2nd') == "" || document.getElementById('3rd') == "" || document.getElementById('4th') == "" || document.getElementById('5th') == "") {
        alert("入力漏れがあります");
        return false;
    } else {
        document.myForm.submit();
        document.getElementById('formWrapper').style.display = 'none';
        document.getElementById('thxMessage').style.display = 'block';
        return true;
    }
}