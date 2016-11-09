// Page 24
// Kenny Tries to stay safe, but somehow every day something happens.
// If there is a 10% chance of volcano, 15% chance of tsunami, 20% chance of earthquake,
// 25% chance of blizzard, and 30% chance of meteor strike, 
// write function whatHappensToday() to print the outcome.

function whatHappensToday() {
	var disaster;
	var randNum = Math.random();
	if(0 <= randNum && randNum < .09) {
		disaster = "volcano";
	} else if(.09 < randNum && randNum < .24) {
		disaster = "tsunami";
	} else if(.24 < randNum && randNum < .44) {
		disaster = "earthquake";
	} else if(.44 < randNum && randNum < .69) {
		disaster = "blizzard";
	} else if(.69 < randNum && randNum < 1) {
		disaster = "meteor strike";
	}
	console.log("Today Kenny has died in a " + disaster + " ... bummer.");
}

whatHappensToday();