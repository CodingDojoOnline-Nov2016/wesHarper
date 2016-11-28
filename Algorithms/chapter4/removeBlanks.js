// Page 50
// Create a function that, given a string, returns all of that string's contents, but without blanks. If given the
// string " Pl     ayTha   tF     u      nkyM      usi      c    ", return "PlayThatFunkyMusic"

function removeBlanks(str) {
	var newString = "";
	for(var i = 0; i < str.length; i++) {
		if(str[i] != " " && str[i].charCodeAt() != 09 && str[i].charCodeAt() != 11) {
			newString += str[i];
		}
	}
	return newString;
}

var string = " Pl     ayTha   tF     u      nkyM      us	i      c    \
";
removeBlanks(string);