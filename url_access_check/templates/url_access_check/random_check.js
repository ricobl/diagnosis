var csrf_token = "{{ csrf_token }}";

var urls = new Array();

{% for url in urls_browser %}
    urls.push(['{{ url.id }}', '{{ url.address }}']);
{% endfor %}

$(function() {

    $.each(urls, function(idx, url){
        var new_iframe = document.createElement('iframe');
        new_iframe.setAttribute('id','url_' + url[0]);
        new_iframe.setAttribute('src', url[1]);
        new_iframe.setAttribute('data_reachable', 'false');
        new_iframe.setAttribute('class','hidden_iframe');
        $('body').append(new_iframe);
    });

    $(".hidden_iframe").load(function(event) {
        $(this).attr("data_reachable", true);
    });

    $(window).load(function(event){
        $.each( $(".hidden_iframe"), function(idx, iframe){
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