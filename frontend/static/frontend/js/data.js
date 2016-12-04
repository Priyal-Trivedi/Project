/**
 * Created by priyanktrivedi on 15/10/16.
 */

function fetch_data(step)
{

      var url = '/fetch_data/';

  data = { 'step': step};

    $.ajax({
        url: url,
        crossDomain: true,
        type: 'POST',
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
        dataType: 'json',
        data: data,
        beforeSend: function(jqXHR, settings) {

        },
        success: function(data, textStatus, jqXHR) {

            $("#data_content").html(data['html']);

        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Failed");
        },
        complete: function(jqXHR, textStatus) {
            console.log("Completed")

        }
    });


}



$("#btn_1_big").click(function() {
  // alert( "Fetched and display saved data for Select System Boundary");

    var step = 1;

    fetch_data(step);


});

$("#btn_2").click(function() {
  // alert( "Fetched and display saved data for Generate Requirements");

    var step=2;

    fetch_data(step);


});

$("#btn_3").click(function() {
  alert( "Fetched and display saved data for Selected Sustainability Definitions");
});
$("#btn_4").click(function() {
  alert( "Fetched and display saved data for Selected Sustainability Definitions");
});
$("#btn_5").click(function() {
  alert( "Fetched and display saved data for Selected Sustainability Definitions");
});
$("#btn_6").click(function() {
  alert( "Fetched and display saved data for Selected Sustainability Definitions");
});



