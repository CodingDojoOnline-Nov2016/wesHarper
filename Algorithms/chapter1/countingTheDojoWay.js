//Page 16
//Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

function dojoWay(){
	for(var num = 1; num < 101; num++) {
		if(num % 5 === 0 && num % 10 === 0) {
			console.log("Coding Dojo");
		} else if(num % 5 === 0) {
			console.log("Coding");
		} else {
			console.log(num);
		}
	}
}

dojoWay();

//shoot for solving problem in 1 line
function dojoWay2(){
	for(var num = 1; num < 101; num++) {
		var value = num % 5 === 0 && num % 10 === 0 ? "Coding Dojo" : value = num % 5 === 0 ? "Coding" : num;
		console.log(value);
	}
}

dojoWay2();
