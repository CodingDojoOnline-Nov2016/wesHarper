// Page 24
// For an additional challenge, add '-' signs to scores in the bottom two percent of A, B, C, and D scores,
// and '+' signs to the top two percent of B, C and D scores (sorry, Mr.Cerise never gives an A+). Given
// 88, console.log "Score: 88. Grade: B+". Given 61 log "Score: 61. Grade: D-". 

function accLetterGrade(score) {
	if (score >= 0 && score < 60) {
		console.log("Score: " + score + ". Grade: F");
	} else if(score >= 60 && score < 70) {
		if(score >= 60 && score <= 62) {
			console.log("Score: " + score + ". Grade: D-");
		} else if(score >= 68 && score < 70) {
			console.log("Score: " + score + ". Grade: D+");
		} else {
			console.log("Score: " + score + ". Grade: D");
		}
	} else if(score >= 70 && score < 80) {
		if(score >= 70 && score <= 72) {
			console.log("Score: " + score + ". Grade: C-");
		} else if(score >= 78 && score < 80) {
			console.log("Score: " + score + ". Grade: C+");
		} else {
			console.log("Score: " + score + ". Grade: C");
		}
	} else if(score >= 80 && score < 90) {
		if(score >= 80 && score <= 82) {
			console.log("Score: " + score + ". Grade: B-");
		} else if(score >= 88 && score < 90) {
			console.log("Score: " + score + ". Grade: B+");
		} else {
			console.log("Score: " + score + ". Grade: B");
		}
	} else if(score >= 90 && score < 100) {
		if(score >= 90 && score <= 92) {
			console.log("Score: " + score + ". Grade: A-");
		} else {
			console.log("Score: " + score + ". Grade: A");
		}
	} else if(score >= 100) {
		console.log("Woah, you got a score of " + score + "!? You're such an overachiever. Still no A+");
	} else {
		console.log("Either you did so poorly in this class you managed to get less than a 0, or I've accidentally logged your grade as something other than a number!");
	}
}

accLetterGrade(61);
accLetterGrade(88);
accLetterGrade(125);
accLetterGrade("beer");