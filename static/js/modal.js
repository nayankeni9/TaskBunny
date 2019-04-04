$("#signup").click(function() {
  $("#first").fadeOut("fast", function() {
    $("#second").fadeIn("fast");
  });
});
    
$("#signin").click(function() {
  $("#second").fadeOut("fast", function() {
    $("#first").fadeIn("fast");
  });
});

$("#tasker_signup").click(function() {
  $("#tasker_first").fadeOut("fast", function() {
    $("#tasker_second").fadeIn("fast");
  });
});
  
$("#tasker_signin").click(function() {
  $("#tasker_second").fadeOut("fast", function() {
    $("#tasker_first").fadeIn("fast");
  });
});