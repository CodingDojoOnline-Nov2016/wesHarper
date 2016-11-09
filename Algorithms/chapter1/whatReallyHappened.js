// Page 24
// Kyle (smarter than Kenny) notes that the chance of one disaster is totally unrelated to the chance of
// another. Change whatHappensToday() function to create whatReallyHappensToday(). In this
// new function test for each disaster independently, instead of assuming exactly one disaster will happen.
// In other words, with this new function, all five might occur today - or none. Maybe Kenny will survive!

function whatReallyHappensToday() {
	var disasterList = [];
	var probV = Math.random();
	var probT = Math.random();
	var probE = Math.random();
	var probB = Math.random();
	var probM = Math.random();
	if(0 <= probV && probV < .09) {
		disasterList.push("volcano");
	}
	if(.09 < probV && probV < .24) {
		disasterList.push("tsunami");
	}
	if(.24 < probE && probE < .44) {
		disasterList.push("earthquake");
	}
	if(.44 < probB && probB < .69) {
		disasterList.push("blizzard");
	}
	if(.69 < probM && probM < 1) {
		disasterList.push("meteor strike");
	}
	console.log(disasterList);
	console.log("Today Kenny has died in the following accidents: " + disasterList + " ... bummer.");
}

whatReallyHappensToday();