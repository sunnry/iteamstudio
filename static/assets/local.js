var transparent = true;

$(document).ready(function(){
});


$(window).on('scroll',function(){
	local.checkScrollForTransparentNavbar();
});


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
