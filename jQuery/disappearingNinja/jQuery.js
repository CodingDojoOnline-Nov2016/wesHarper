$(document).ready(function() {
	$("img").click(function() {
		$(this).fadeOut(1000);
	});
	$("button").click(function() {
		$("img").show();
	});
});