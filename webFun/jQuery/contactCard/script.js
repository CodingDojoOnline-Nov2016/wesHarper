$(document).ready(function(){
	$('form').submit(function(e){
		e.preventDefault();

		var entry = {
			"firstName": $('input[name="first-name"]').val(),
			"lastName": $('input[name="last-name"]').val(),
			"description": $('textarea[name="description"]').val()
		}

		var $ele = $('<div class="card"></div>');

		$ele.html('<h2>' + entry.firstName + ' ' + entry.lastName + '</h2>' + '<p>' + entry.description + '</p>');

		$('.card-box').append($ele);
		$(this).children().children('input:first-child, input:nth-child(2), textarea').val(null);
		$('.card-box :last-child').children('p').hide();
	});

	$('.card-box').on("click", 'h2', function(){
		console.log("clicked");
		$(this).siblings().toggle("slow");
	});
})