//Page 20
//Write a function that accepts any array and returns a new array with the array values that are greater
//than its 2nd value. Print how many values this is.
//What will you do if the array is only one element long?

function greaterThanSecondGen(arr) {
	var newArr = [];
	var count = 0;
	for(var i = 0; i < arr.length; i++) {
		if(arr[i] > arr[1]) {
			newArr.push(arr[i]);
			count++;
		}
	}
	console.log(newArr);
	console.log(count);
}

var arr1 = [2,1,3,4,5,6,7,8,9,10];
greaterThanSecondGen(arr1);

//if the array is one element long

function greaterThanSecondGen2(arr) {
	if(arr.length > 1) {
		var newArr = [];
		var count = 0;
		for(var i = 0; i < arr.length; i++) {
			if(arr[i] > arr[1]) {
				newArr.push(arr[i]);
				count++;
			}
		}
		console.log(newArr);
		console.log(count);
	} else {
		console.log("Way to go dumbass, you tried to pass an array with only one value.")
	}
}

var arr2 = [10];
greaterThanSecondGen2(arr2);