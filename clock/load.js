$(document).ready(function() {
    $.ajaxSetup({cache:false});
    $('#body').load('competition.html');
    $('#body').CreateElement('<script src="getdata.js"></script>');
    $('#body').CreateElement('<script src="getscramble.js"></script>');
    $('#body').CreateElement('<script src="getdate.js"></script>');
    $('#body').CreateElement('<script src="getdata_yesterday.js"></script>');
});