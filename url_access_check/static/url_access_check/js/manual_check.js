$(function() {
    $(".hidden_iframe").load(function(event) {
        $(this).attr("data_reachable", true);
    });

    $(window).load(function(event){
        $.each( $(".hidden_iframe"), function(idx, iframe){
            $("#tests").append("<li><div class=\"disc " + iframe.attributes['data_reachable'].value + "\">&nbsp;</div>" + iframe.src + "</li>");

            if (iframe.attributes['data_reachable'].value == "false"){
                $.ajax({
                    url:'/diagnosis/url/failed',
                    type:'POST',
                    data: {
                        url_id: iframe.id.replace("url_","")
                    },
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader("X-CSRFToken", csrf_token);
                    }
                });
            }
        });
    });
});