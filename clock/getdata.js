$.when(
    $.ajax({
        url: 'data.csv',
        cache: false,
        dataType: "text",
        beforeSend : function(xhr) {
            xhr.overrideMimeType('text/plain;charset=Shift_JIS');
        },
    })
)
.done(function(data) {
    data=$.csv()(data[0]);
})
.fail(function() {
    alert("データベースの読み込みエラーが発生しました。");
});