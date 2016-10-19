/**
 * Created by priyanktrivedi on 15/10/16.
 */

console.log("I'm called.");


$("#btn_1_big").click(function() {
  alert( "First big button is clicked." );
});

$("#btn_2").click(function() {
  alert( "Button with id btn_2 is clicked." );
});

$("#btn_3").click(function() {
  alert( "Button with id btn_3 is clicked." );
});
var step = 0;
function next_steps(domain, tbl_scope, problem_type) {


  var url = '/next_step/';
  data = {'step': step, 'domain': domain, 'tbl_scope': tbl_scope, 'problem_type': problem_type };

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
          console.log("Success", data);
          $("#step_info").html("<p>"+data['step_info']+"</p>");
            step += 1;
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Failed");
        },
        complete: function(jqXHR, textStatus) {
            console.log("Completed")

        }
    });

}





// Making an ajax call to a view in python and then loading an html.