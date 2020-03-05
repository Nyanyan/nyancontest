$(document).ready(function() {
    $.ajaxSetup({cache:false});
    $('#body').load('competition.html');
    $('#body').insertAdjacentHTML('beforeend','<script src="getdata.js"></script>');
    $('#body').insertAdjacentHTML('beforeend','<script src="getscramble.js"></script>');
    $('#body').insertAdjacentHTML('beforeend','<script src="getdate.js"></script>');
    $('#body').insertAdjacentHTML('beforeend','<script src="getdata_yesterday.js"></script>');
});