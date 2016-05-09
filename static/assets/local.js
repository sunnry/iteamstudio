var transparent = true;

var stick1Enable = false;

$(document).ready(function(){
});


$(window).on('scroll',function(){
	local.checkScrollForTransparentNavbar();
});


whandler =new WOW();
whandler.init();


$('.ddl').on({
	mouseenter:function(event){
	   $sub = $(this).children('.dd');
	   $sub.addClass('dd-visible');
	},
	mouseleave:function(event){
	   $sub = $(this).children('.dd');
	   $sub.removeClass('dd-visible');
	}
});

$('.dd').on({
	mouseleave:function(event){
		$(this).removeClass('dd-visible');
	}
});

$('#avatar-file-upload').on({
	click:function(event){
		$('#avatar-input').trigger('click')
	}
});

$('#avatar-input').on({
	change:function(event){
		value = $(this).val()
		$('#avatar-display').val(value)
	}
})

/*I add a random digital behand src new request, this will let server side
 * treat it as a whole new request and will perform new response, also you 
 * can add expire time in you response header like following:
 * "Content-Type: image/jpeg"
 * "Cache-Control: no-cache, must-revalidate"
 * "Expires: Sat, 26 Jul 1997 05:00:00 GMT"*/
$('.signinImgVerify').on({
	click:function(event){
	var url = "/accounts/captcha/"
		$(this).attr("src",url + '?rand=' + Math.random())
	}
});

var local = {
		checkScrollForTransparentNavbar:function(){
			var delayfunc = debounce(function(){
				if($(document).scrollTop() > 350){
					if(transparent){
						transparent = false;
						$('nav[role="navigation"]').removeClass('navbar-transparent');
					}
				}else{
					if(!transparent){
						transparent = true;
						$('nav[role="navigation"]').addClass('navbar-transparent');
					}
				}

				if($(document).scrollTop() > 450){
					if(!stick1Enable){
						stick1Enable = true;
						$('#stick1fgimg').addClass('active');
						$('#stick2fgimg').addClass('active');
						$('#stick3fgimg').addClass('active');
					}
				}else{
					if(stick1Enable){
						stick1Enable = false;
						$('#stick1fgimg').removeClass('active');
						$('#stick2fgimg').removeClass('active');
						$('#stick3fgimg').removeClass('active');
					}
				}

			},17);
			delayfunc();
		}
};


function debounce(func,wait,immediate){
	var timeout;
	return function(){
		var context = this, args = arguments;
		clearTimeout(timeout);
		timeout = setTimeout(function(){
			timeout = null;
			if(!immediate) func.apply(context,args);
		},wait);
		if(immediate && !timeout) func.apply(context,args);
	};
};
