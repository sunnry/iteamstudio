var playerInstance = jwplayer("introduce1");
playerInstance.setup({
	file:"http://192.168.0.103/public/index/introduce1.mp4",
	image:"/public/index/introduce1_cover.jpg",
	width:500,
	height:500,
	title:"test",
	description:'show small cover',
});
