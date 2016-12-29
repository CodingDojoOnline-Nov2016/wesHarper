// Page 84
// Here, a balance point is ON an index, not BETWEEN incices. Return the balace index where sums are
// equal on either side (exclude its own value). Return -1 if none exist. Ex: [-2,5,7,0,3] --> 2,
// but [9,9] --> -1.

function balanceIndex(arr) {
	if(arr.length < 3){ //check if array is too short
		return -1;
	}

	var sumRight = arr[arr.length - 1]; //start with right-most value
	var sumLeft = arr[arr.length - 3]; //start with 2nd to last index
	var idx = arr.length - 2; //track current index

	for(var i = 0; i < idx; i++) { //calculate sumLeft
		sumLeft += arr[len - 1];
	}

	while(idx){ //decrement index fulcrum and run conditional checks
		//run conditional checks
		if(sumLeft === sumRight) {
			return idx;
		}
		if(sumRight > sumLeft) {
			return idx;
		}
		//decrement fulcrum
		sumLeft -= arr[idx - 1];
		sumRight += arr[idx];
		//continue loop
		idx--;
	}
	return -1;
}

var array1 = [-2,5,7,0,3] //2
var array2 = [9,9] //-1
var array3 = [1, 2, 3, 4, 10] //-1
var array4 = [9, 1, 9] //1
console.log(balanceIndex(array1))
console.log(balanceIndex(array2))
console.log(balanceIndex(array3))
console.log(balanceIndex(array4))