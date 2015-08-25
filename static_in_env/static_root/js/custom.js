function showFlashMessage(message) {
	var template = "{% include 'alert.html' with message='" + message + "' %}"
	$("body").append(template);
	$(".container-alert-flash").fadeIn();
	setTimeout(function(){ 
		$(".container-alert-flash").fadeOut();
	}, 1800);

}