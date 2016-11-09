// Page 24
// Mr. Cerise teaches high school math. Write a function that assigns and prints a letter grade, given an
// integer representing a score from 0 to 100. Those getting 90+ get an 'A', 80-89 'B', 70-79 'C',
// 60-69 is a 'D', and lower than 60 receive 'F'. For example, given 88, you should log "Score: 88.
// Grade: B". Given the score 61, log the score "Score: 61. Grade: D".

function letterGrade(score) {
	if (score >= 0 && score < 60) {
		console.log("Score: " + score + ". Grade: F");
	} else if(score >= 60 && score < 70) {
		console.log("Score: " + score + ". Grade: D");
	} else if(score >= 70 && score < 80) {
		console.log("Score: " + score + ". Grade: C");
	} else if(score >= 80 && score < 90) {
		console.log("Score: " + score + ". Grade: B");
	} else if(score >= 90 && score < 100) {
		console.log("Score: " + score + ". Grade: A");
	} else if(score >= 100) {
		console.log("Woah, you got a score of " + score + "!? You're such an overachiever.");
	} else {
		console.log("Either you did so poorly in this class you managed to get less than a 0, or I've accidentally logged your grade as something other than a number!");
	}
}

letterGrade(61);
letterGrade(88);
letterGrade(125);
letterGrade("beer");