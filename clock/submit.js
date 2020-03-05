function submitForm(){
    alert(document.getElementById('name').value)
    if (document.getElementById('name').value == "" || document.getElementById('1st').value == "" || document.getElementById('2nd').value == "" || document.getElementById('3rd').value == "" || document.getElementById('4th').value == "" || document.getElementById('5th').value == "") {
        alert("入力漏れがあります");
        return false;
    } else {
        document.myForm.submit();
        document.getElementById('formWrapper').style.display = 'none';
        document.getElementById('thxMessage').style.display = 'block';
        return true;
    }
}