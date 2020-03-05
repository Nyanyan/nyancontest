function submitdata(){
    var data = new FormData;
    // data.append(name属性, 値);
    data.append("entry.1460875154", value);
    data.append("entry.39328532", value);
    data.append("entry.975282763", value);
    data.append("entry.673200780", value);
    data.append("entry.1826089930", value);
    data.append("entry.75959801", value);

    // フォームデータ送信
    $.ajax({
    　　　　　// Googleフォームへの送信先URL
        url: "https://docs.google.com/forms/d/e/1FAIpQLSdNs5H8dzfoZe0IWXMx4AujhDipY2MYe6LoJtdKusxlNN1QWA/viewform?usp=sf_link",
        data: data,
        processData: false,
        contentType: false,
        type: 'POST',
        statusCode: {
            0: function () {
                // 成功
            },
            200: function () {
                // エラー
            }
        }
    });
}