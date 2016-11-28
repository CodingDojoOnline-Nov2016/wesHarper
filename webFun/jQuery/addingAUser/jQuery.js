$(document).ready(function(){
	$("#add-user").click( function(){	
		var first = $("input[name='first-name']").val();
		var last = $("input[name='last-name']").val();
		var email = $("input[name='email']").val();
		var phone = $("input[name='contact-num'").val();
		console.log(first);
		$("tbody").append("<tr>" + "<td>" + first + "</td>" + "<td>" + last + "</td>" + "<td>" + email + "</td>" + "<td>" + phone + "</td>" + "</tr>");
	});
});