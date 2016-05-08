var playerInstance = jwplayer("g12-video");
playerInstance.setup({
	file:"http://192.168.0.103/public/index/introduce1.mp4",
	image:"/public/index/introduce1_cover.jpg",
	width:"100%",
	height:"100%",
	title:"",
	description:'',
});


 whandler =new WOW();
 whandler.init();


$('.grid').packery({
  itemSelector:'.grid-item',
  gutter:0
});


$('.grid1').on({
        mouseenter:function(event){
           $('.g1-view').addClass("active_t1");
        },
        mouseleave:function(event){
           $('.g1-view').removeClass("active_t1");
        }
});

$('.grid2').on({
        mouseenter:function(event){
           $('.g2-view').addClass("active_t5");
        },
        mouseleave:function(event){
           $('.g2-view').removeClass("active_t5");
        }
});


$('.grid6').on({
        mouseenter:function(event){
           $('.g6-view').addClass("active_t5");
        },
        mouseleave:function(event){
           $('.g6-view').removeClass("active_t5");
        }
});


var g7_orgin_height = $('.g7-bg-img').height();

$('.grid7').on({
        mouseenter:function(event){
	   if(g7_orgin_height == $('.g7-bg-img').height()){
	   	$('.g7-bg-img').animate({ 
				height:$('.g7-bg-img').height()*2,
				width:$('.g7-bg-img').width()*2,
				marginLeft:'-50%',
				marginTop:'-38%',
				}, 50);
	   }
        },
        mouseleave:function(event){
	   if((g7_orgin_height*2) == $('.g7-bg-img').height()){
	   	$('.g7-bg-img').animate({ 
				height:$('.g7-bg-img').height()*0.5,
				width:$('.g7-bg-img').width()*0.5,
				marginLeft:'0px',
				marginTop:'0px',
				}, 50);
	   }
        }
});

var g8_orgin_height = $('.g8-bg-img').height();

$('.grid8').on({
        mouseenter:function(event){
	   if(g8_orgin_height == $('.g8-bg-img').height()){
	   	$('.g8-bg-img').animate({ 
				height:$('.g8-bg-img').height()*2,
				width:$('.g8-bg-img').width()*2,
				marginLeft:'-50%',
				marginTop:'-38%',
				}, 50);
	   }
        },
        mouseleave:function(event){
	   if((g8_orgin_height*2) == $('.g8-bg-img').height()){
	   	$('.g8-bg-img').animate({ 
				height:$('.g8-bg-img').height()*0.5,
				width:$('.g8-bg-img').width()*0.5,
				marginLeft:'0px',
				marginTop:'0px',
				}, 50);
	   }
        }
});



$('.grid9').on({
        mouseenter:function(event){
           $('.g9-view').addClass("active_t2");

	   $('.g9-notes').removeClass("inactive_t3");
	   $('.g9-notes').addClass("active_t3");
        },
        mouseleave:function(event){
           $('.g9-view').removeClass("active_t2");

	   $('.g9-notes').removeClass("active_t3");
	   $('.g9-notes').addClass("inactive_t3");
        }
});

$('.grid10').on({
        mouseenter:function(event){
           $('.g10-view').addClass("active_t5");
        },
        mouseleave:function(event){
           $('.g10-view').removeClass("active_t5");
        }
});

$('.grid11').on({
        mouseenter:function(event){
           $('.g11-view').addClass("active_t2");

	   $('.g11-notes').removeClass("inactive_t4");
	   $('.g11-notes').addClass("active_t4");
        },
        mouseleave:function(event){
           $('.g11-view').removeClass("active_t2");

	   $('.g11-notes').removeClass("active_t4");
	   $('.g11-notes').addClass("inactive_t4");
        }
});

$('.grid13').on({
        mouseenter:function(event){
           $('.g13-view').addClass("active_t5");
        },
        mouseleave:function(event){
           $('.g13-view').removeClass("active_t5");
        }
});

$('.grid15').on({
        mouseenter:function(event){
           $('.g15-view').addClass("active_t5");
        },
        mouseleave:function(event){
           $('.g15-view').removeClass("active_t5");
        }
});

$('.grid17').on({
        mouseenter:function(event){
           $('.g17-view').addClass("active_t5");
        },
        mouseleave:function(event){
           $('.g17-view').removeClass("active_t5");
        }
});


$(window).on('resize',function(){
/*here we use g2-bg-img as standard, because g2 do not have scale effect,but the size is save
 * with others, we use it height and width as standard	*/
	g7_orgin_height = $('.g2-bg-img').height();
	g7_orgin_width = $('.g2-bg-img').width();
	$('.g7-bg-img').animate({
                                height:g7_orgin_height,
                                width:g7_orgin_width
                                },0);

	g8_orgin_height = $('.g2-bg-img').height();
	g8_orgin_width = $('.g2-bg-img').width();
	$('.g8-bg-img').animate({
                                height:g8_orgin_height,
                                width:g8_orgin_width
                                },0);

});

