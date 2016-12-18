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

$('.btnsel').on('click',function(){
    $('.btnsel').removeClass('btn-warning');
    $(this).addClass('btn-warning');
    var num = Number($(this).text());
    if(num==7||num==12||num==17);
    else fetch_data(num);

});
