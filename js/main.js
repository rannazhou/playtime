$(document).ready(function($) {
	$(".panel-heading").hide();
	$(".panel-body").click(function(){
		$(this).parent(".panel").find(".panel-heading").slideToggle();
	})

	$(".join-btn").click(function() {
		$(this).toggleClass("btn-success");
		$(this).text(function(i, text){
      		return text === "Join" ? "Joined" : "Join";
  		});
  		// this stops the click from propogating to the parent
  		return false;
	});
});