function hidebox() 
{
	$(".page-filter" ).on( "click", function() {
		$(".login-box").css({"display": "none"});
		$(".page-filter").css({"display": "none"});
		$(".register-box").css({"display": "none"});
		$(".contact-box").css({"display": "none"});
	});
}

function showbox(id)
{
	if ($("."+id).css("display") == "none")
	{
		$("."+id).css({"display": "block"});
		$(".page-filter").css({"display": "block"});
	}
	hidebox();
}