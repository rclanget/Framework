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

function show_sscat(id)
{
	if ($("#"+id).css("display") == "block")
	{
		$("#"+id).css({"display": "none"});
	}
	else
	{
		if ($(".forum_nav__sscat").css("display") == "block")
		{
			$(".forum_nav__sscat").css({"display": "none"});
		}
		$("#"+id).css({"display": "block"});
	}
}

function showInput(id)
{
	if ($("#post"+id).css("display") == "none")
	{
		$("#post"+id).css({"display": "block"});
		$("#but"+id).css({"display": "none"});
	}
}