$(document).ready(function() {
    $("#open_url").click(function() {
        uu = $("#thingspeak_url").val();
        window.open(uu);
    });

    let interval_time = 0;
    $("#btn_show").click(function() {
        interval_time = ($("#id_interval").val() * 1000);
        let ajax_calling_url = $('#id_interval').data('url');
        let jsonurl = $('#thingspeak_url').val();
        $("#sensor_content_body").empty(); //empty the table on each click   

        setInterval(function() {
                $.ajax({
                    type: "get",
                    url: ajax_calling_url,
                    data: {
                        'id': jsonurl
                    },
                    success: function(data1) {
                        $("#sensor_content_body").empty();
                        console.log(data1);
                        $("#sensor_content_body").html("<tr><td>" + data1.result.name + "</td><td>" + data1.result.email + "</td><td>" + data1.result.date + "</td><td>" + data1.result.temp + "</td><td>" + data1.result.humidity + "</td><td>" + data1.result.bodytemp + "</td></tr>");
                        return data1;
                    },
                    error: function() {
                        console.log("Something Went Wrong!");
                    }
                });
            },
            interval_time); //time in milliseconds  }); 
    })
});