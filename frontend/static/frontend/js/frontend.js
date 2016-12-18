/**
 * Created by priyanktrivedi on 15/10/16.
 */

console.log("I'm called.");

function next_steps(domain, tbl_scope, problem_type) {


  var url = '/next_step/';

  data = { 'domain': domain, 'tbl_scope': tbl_scope, 'problem_type': problem_type};

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

            $("#rendered_content").html("");
            $("#content").html(data["context_info"]);

          $("#step_info").html("Step - " + data["current_step"]);

          $("#btn_"+String(parseInt(data["current_step"]-1))).html(String(parseInt(data["current_step"]-1)));

          $("#btn_"+data["current_step"]).css("background-color","#ff9933");
                $("#btn_"+String(parseInt(data["current_step"]-1))).css("background-color","#336666");

          $("#step_name").html(data["step_name"]);

        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Failed");
        },
        complete: function(jqXHR, textStatus) {
            console.log("Completed")

        }
    });

}


function lc_phase(domain, tbl_scope, problem_type, lc_phase ) {
    $('.selimg').removeClass("cliked");
    if(lc_phase=='Material'){
        $('#material').addClass('cliked');
    }
    if(lc_phase=='Production'){
        $('#production').addClass('cliked');
    }
    if(lc_phase=='Assembly'){
        $('#assembly').addClass('cliked');
    }
    if(lc_phase=='Use'){
        $('#use').addClass('cliked');
    }
    if(lc_phase=='After Use'){
        $('#after_use').addClass('cliked');
    }

  var url = '/fetch_lc_phase/';
    var step = $('#step_info').val();

  data = { 'domain': domain, 'tbl_scope': tbl_scope, 'problem_type': problem_type, 'lc_phase': lc_phase, 'step': step };

    $.ajax({
        url: url,
        crossDomain: true,
        type: 'GET',
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
        dataType: 'json',
        data: data,
        beforeSend: function(jqXHR, settings) {

        },
        success: function(data, textStatus, jqXHR) {
          console.log("Success", data["current_step"]);

            $("#content").html(data["html"]);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Failed");
        },
        complete: function(jqXHR, textStatus) {
            console.log("Completed")

        }
    });

}



    <!-- Initialize the plugin: -->

        // $(document).ready(function() {


            $("#save_system_boundary").click(function() {
                    console.log("Saving system");
                  var url = '/save_data/';
                  data = {'step': $(this).data("step"), 'changes_allowed': $("#changes_allowed").val(),
                      'changes_not_allowed': $("#changes_not_allowed").val()  };

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

                            if(data['success'] == 'True')
                            {
                                Messenger().post({
  message: "Data saved for System Boundary",
  type: "info"
})
                            }
                            else{
                                Messenger().post({
  message: "Some error occured in saving data for System Boundary",
  type: "error"
})
                            }
                        },
                        error: function(jqXHR, textStatus, errorThrown) {
                            console.log("Failed");
                        },
                        complete: function(jqXHR, textStatus) {
                            console.log("Completed")

                        }
                    });



    });



                        $("#save_sustainability_indicators").click(function() {

                  var url = '/save_data/';
                    var indicators_array = new Array();


            $("input:checkbox[name=ind]:checked").each(function(){
                indicators_array.push($(this).data("name"));
            });
                console.log(indicators_array);
                  data = {'step': $(this).data("step"), 'indicators[]': indicators_array};

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

                            if(data['success'] == 'True')
                            {
                                Messenger().post({
  message: "Data saved for Sustainability Indicators",
  type: "info"
})
                            }
                            else{
                                Messenger().post({
  message: "Some error occured in saving data for Sustainability Indicators",
  type: "error"
})
                            }
                        },
                        error: function(jqXHR, textStatus, errorThrown) {
                            console.log("Failed");
                        },
                        complete: function(jqXHR, textStatus) {
                            console.log("Completed")

                        }
                    });



    });




                        $("#save_generate_requirements").click(function() {

                  var url = '/save_data/';
                  data = {'step': $(this).data("step"), 'lc_phase': $("#lc_phase").val(),
                      'current_systems': $("#current_systems").val(), 'issues': $("#issues").val(),
                        'requirements': $("#requirements").val() };

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

                            if(data['success'] == 'True')
                            {
                                Messenger().post({
  message: "Data saved for Generate Requirements",
  type: "info"
})
                            }
                            else{
                                Messenger().post({
  message: "Some error occured in saving data for Generate Requirements",
  type: "error"
})
                            }
                        },
                        error: function(jqXHR, textStatus, errorThrown) {
                            console.log("Failed");
                        },
                        complete: function(jqXHR, textStatus) {
                            console.log("Completed")

                        }
                    });



    });


                        $("#save_sustainability_definitions").click(function() {

                  var url = '/save_data/';
                            var defs_array = new Array();


$("input:checkbox[name=type]:checked").each(function(){
    defs_array.push($(this).data("name"));
});
        console.log(defs_array);
                  data = {'step': $(this).data("step"), 'definitions[]': defs_array};

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

                            if(data['success'] == 'True')
                            {
                                Messenger().post({
  message: "Data saved for Sustainability Definitions",
  type: "info"
})
                            }
                            else{
                                Messenger().post({
  message: "Some error occured in saving data for Sustainability Definitions",
  type: "error"
})
                            }
                        },
                        error: function(jqXHR, textStatus, errorThrown) {
                            console.log("Failed");
                        },
                        complete: function(jqXHR, textStatus) {
                            console.log("Completed")

                        }
                    });



    });


                        $("#save_lc_phase").click(function() {
                alert("Will save lc phase");
//
//                   var url = '/save_data/';
//                             var defs_array = new Array();
//
//
// $("input:checkbox[name=type]:checked").each(function(){
//     defs_array.push($(this).data("name"));
// });
//         console.log(defs_array);
//                   data = {'step': $(this).data("step"), 'indicators[]': defs_array};
//
//                     $.ajax({
//                         url: url,
//                         crossDomain: true,
//                         type: 'POST',
//                         contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
//                         dataType: 'json',
//                         data: data,
//                         beforeSend: function(jqXHR, settings) {
//
//                         },
//                         success: function(data, textStatus, jqXHR) {
//                           console.log("Success", data);
//
//                             if(data['success'] == 'True')
//                             {
//                                 Messenger().post({
//   message: "Data saved for Sustainability Indicators",
//   type: "info"
// })
//                             }
//                             else{
//                                 Messenger().post({
//   message: "Some error occured in saving data for Sustainability Indicators",
//   type: "error"
// })
//                             }
//                         },
//                         error: function(jqXHR, textStatus, errorThrown) {
//                             console.log("Failed");
//                         },
//                         complete: function(jqXHR, textStatus) {
//                             console.log("Completed")
//
//                         }
//                     });
    //


    });



        // });






// Making an ajax call to a view in python and then loading an html.