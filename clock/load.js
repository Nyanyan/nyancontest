$(document).ready(function() {
    $.ajaxSetup({cache:false});
    $('#body').load('competition.html');
    $('#body').replace('DATE', 'REPLACED');
});