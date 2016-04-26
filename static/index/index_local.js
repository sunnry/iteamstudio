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
           $('.g1-view').addClass("g1-view-active");
        },
        mouseleave:function(event){
           $('.g1-view').removeClass("g1-view-active");
        }
});

