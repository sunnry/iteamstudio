var playerInstance = jwplayer("introduce1");
playerInstance.setup({
	file:"http://192.168.0.103/public/index/introduce1.mp4",
	image:"/public/index/introduce1_cover.jpg",
	width:500,
	height:500,
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

