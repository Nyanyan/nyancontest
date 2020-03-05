function submitForm(){
    if (myForm.getElementById('name') == "" || myForm.getElementById('1st') == "" || myForm.getElementById('2nd') == "" || myForm.getElementById('3rd') == "" || myForm.getElementById('4th') == "" || myForm.getElementById('5th') == "") {
        alert("入力漏れがあります");
        return false;
    } else {
    document.myForm.submit();
    document.getElementById('formWrapper').style.display = 'none';
    document.getElementById('thxMessage').style.display = 'block';
    return true;
    }
}