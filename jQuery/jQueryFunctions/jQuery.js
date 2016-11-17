$(document).ready(function() {
	$('#addClass').click(function() {
		$('#addClassP').addClass('bermuda');
	});
	$('input:radio[name="valRadio"]').click(function displayVal() {
		var radioVal = $('input:radio[name="valRadio"]:checked').val();
		$('#radioValue').html(radioVal);
		// console.log(radioVal);
	});
	$('#text').click(function() {
		var newText = $('#textP').text();
		$('#newText').html(newText);
	});
	$('#attr').click(function() {
		var attrName = $('#attr').attr('name');
		$('#attrName').html(attrName);
	});
	$('#html').click(function() {
		$('#htmlStr').html("Boo!");
	});
	$('#focus').click(function() {
		$('#html').focus();
	});
	$('#data').click(function() {
		$("#dataP").data("test", "Yo Mamma!");
		// console.log($("#dataP").data("test"));
		$('#dataVal').append($("#dataP").data("test"));
	});
	$("#before").click(function() {
		$("#beforeP").before("<span>Big Bang</span>");
	});
	$("#after").click(function() {
		$("#afterP").after("<span>Black Hole</span>");
	});
	$("#append").click(function() {
		$("#appendP").append("tail");
	});
	$("#show").click(function() {
		$("#showMe").show();
	});
	$("#hide").click(function() {
		$("#hideMe").hide();
	});
	$("#toggle").click(function() {
		$("#option1").toggle();
		$("#option2").toggle();
	});
	$("#fadeIn").click(function() {
		$("#fadingIn").fadeIn(1200);
	});
	$("#fadeOut").click(function() {
		$("#fadingOut").fadeOut(1200);
	});
	$("#slideDown").click(function() {
		$("#slidingDown").slideDown();
	});
	$("#slideUp").click(function() {
		$("#slidingUp").slideUp();
	});
	$("#slideToggle").click(function() {
		$("#slidingToggle").slideToggle();
	})
})