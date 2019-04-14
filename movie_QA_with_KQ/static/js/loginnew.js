$(function() {
	var i = 0;
	var timer;
	//需求一：第一张图片显示，其余的图片隐藏
	$(".bxback").children(".item").eq(i).show().siblings().hide();
	PicLunbo();
})

function PicLunbo() {
	var i = 0;
	timer = setInterval(function() {
		i++; //i自增
		if(i == 4) {
			i = 0;
		}
		$(".bxback").children(".item").eq(i).stop(true, true).fadeIn(2000).siblings().fadeOut(2000);
	}, 4000);
}