$(document).ready(function() {
    $.ajaxSetup({cache:false});
    $('#body').load('competition.html');
    $('#body').writeln('<script src="getdata.js"></script>');
    $('#body').writeln('<script src="getscramble.js"></script>');
    $('#body').writeln('<script src="getdate.js"></script>');
    $('#body').writeln('<script src="getdata_yesterday.js"></script>');
});