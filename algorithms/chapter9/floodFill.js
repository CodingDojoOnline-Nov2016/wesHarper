// Page 101
// Given x,y coordinates for a target value, every value that is adjacent to that
// value and shares the same value will change to new value, cascading through
// continually adjacent blocks(no diagonal adjacency)
function rFloodFill(start, matrix, char) {
	var x = start[0];	
	var y = start[1];
	var curVal = matrix[x][y]
	matrix[x][y] = char
	console.log("x", x, "y", y, "curVal", curVal, "char", char);
	if(x + 1 < matrix[0].length && matrix[x + 1][y] == curVal) {
		console.log("x + 1:", matrix[x + 1][y]);
		return rFloodFill([y, x + 1], matrix, char);
	}
	if(x - 1 >= 0 && matrix[x - 1][y] == curVal) {
		console.log("x - 1:", matrix[x - 1][y]);
		return rFloodFill([y, x - 1], matrix, char);
	}
	if(y + 1 < matrix.length && matrix[x][y + 1] == curVal) {
		console.log("y + 1:", matrix[x][y + 1]);
		return rFloodFill([y + 1, x], matrix, char);
	}
	if(y - 1 >= 0 && matrix[x][y - 1] == curVal) {
		console.log("y - 1:", matrix[x][y - 1]);
		return rFloodFill([y - 1, x], matrix, char);
	}
	return matrix;
}


var mat = [
	[1,2],
	[1,2]
];

var start = [0,0];
console.log(rFloodFill(start, mat, 0))