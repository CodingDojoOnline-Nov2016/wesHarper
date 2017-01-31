// Page 108

// Get an int and return all permutations of that number of brace pairings
// 1 returns ()
// 2 returns [(()), ()()]

function validBraces(init, subStr='', opensRem=init, closesRem=init, results=[]) {
	if(opensRem == 0 && closesRem == 0) {
		results.push(subStr);
	} else if(opensRem >= closesRem) {
		subStr += "("
		validBraces(init, subStr)
	}
}

console.log(validBraces(3))