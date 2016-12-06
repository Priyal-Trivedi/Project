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

    fetch_data(3);
});
$("#btn_4").click(function() {
  alert( "Fetched and display saved data for Selected Sustainability Definitions");
    fetch_data(4);

});
$("#btn_5").click(function() {
  alert( "Fetched and display saved data for Selected Sustainability Definitions");
});
$("#btn_6").click(function() {
  alert( "Fetched and display saved data for Selected Sustainability Definitions");
});

$("#btn_8").click(function() {
    fetch_data(8);

});
$("#btn_9").click(function() {
     fetch_data(9);
});


$("#btn_10").click(function() {

    fetch_data(10);
});


$("#btn_11").click(function() {
       fetch_data(11);

});

$("#btn_13").click(function() {

         fetch_data(13);

});
$("#btn_14").click(function() {

         fetch_data(14);

});
$("#btn_15").click(function() {

         fetch_data(15);

});
$("#btn_16").click(function() {

         fetch_data(16);

});




