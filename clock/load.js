$(document).ready(function() {
    $.ajaxSetup({cache:false});
    $('#body').load('competition.html');
    $('#body').append('<script src="getdata.js"></script>');
    $('#body').append('<script src="getscramble.js"></script>');
    $('#body').append('<script src="getdate.js"></script>');
    $('#body').append('<script src="getdata_yesterday.js"></script>');
});