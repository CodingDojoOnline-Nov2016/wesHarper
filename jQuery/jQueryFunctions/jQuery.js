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
})