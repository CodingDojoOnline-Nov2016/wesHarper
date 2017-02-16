function BST() {
	this.root = null;
	this.add = add;
	this.min = min;
	this.max = max;
	this.find = find;
	this.size = size;
	this.height = function(node=this.root) {
		if(node) {
			var left = this.height(node.left);
			var right = this.height(node.right);
			if(left > right) {
				return 1 + left;
			} else {
				return 1 + right;
			}
		} else {
			return 0;
		}
	};
	this.isBalanced = function(node=this.root) {
		if(node) {
			if(Math.abs(this.height(node.left) - this.height(node.right)) > 1) {
				return false;
			} else {
				return(this.isBalanced(node.left) && this.isBalanced(node.right))
			}
		}
		return true;
	}
	this.arrayToBST = function(arr, left=0, right=arr.length-1) {
		console.log("left", left, "right", right)
		if(left === right) {
			console.log("adding L ONLY, array val:", arr[left]);
			this.add(arr[left]);
			return;
		} else if(right - left === 1) {
			console.log("adding L and R, array val L:", arr[left], "val R:", arr[right]);
			this.add(arr[left]);
			this.add(arr[right]);
			return;
		} else {
			var mid = Math.ceil((left + right) / 2);
			console.log("mid is:", mid, "adding MID:", arr[mid], "length is greater than 2")
			this.add(arr[mid]);
			this.arrayToBST(arr, left, mid - 1);
			this.arrayToBST(arr, mid + 1, right);
		}
		return this;
	}
}

function BSTNode(arg) {
	this.data = arg;
	this.right = null;
	this.left = null;
}

function add(data) {
	var n = new BSTNode(data);
	if(!this.root) {
		this.root = n;
		var curr = this.root;
	} else {
		var curr = this.root
		while(curr) {
			if(n.data >= curr.data) {
				if(curr.right) {
					curr = curr.right;
				} else {
					curr.right = n;
					break;
				}
			} else if(n.data < curr.data) {
				if(curr.left) {
					curr = curr.left;
				} else {
					curr.left = n;
					break;
				}
			}
		}
	}
	// console.log(curr);
	return this;
}

function min() {
	if(!this.root) {
		return null;
	} else {
		var curr = this.root;
		while(curr.left) {
			curr = curr.left;
		}
		console.log(curr.data);
		return curr;
	}
}

function max() {
	if(!this.root) {
		return null;
	} else {
		var curr = this.root;
		while(curr.right) {
			curr = curr.right;
		}
		// console.log(curr.data);
		return curr;
	}
}

function find(data) {
	if(this.root) {
		var curr = this.root;
		while(curr) {
			if(curr.data === data) {
				console.log(curr);
				return true;
			} else if(data < curr.data) {
				curr = curr.left;
			} else if(data > curr.data) {
				curr = curr.right;
			}
		}
	}
	return false;
}

function size(node=this.root) {
	if(node) {
		return 1 + this.size(node.left) + this.size(node.right);
	} else {
		return 0;
	}
}

function height(curr=this.root) {
	var heightTree = new BST();
	function subHeight(node=curr, sub=0, results=heightTree) {
		// console.log("sub", sub)
		if(node) {
			// console.log("node.data", node.data)
			sub += 1;
			subHeight(node.left, sub, results);
			subHeight(node.right, sub, results);
		} else {
			results.add(sub);
			// console.log(results);
		}
		return results;
	}
	// console.log(subHeight(), "subHeight()");
	return subHeight().max().data;
}

BST.prototype.BSTtoArray = function(node=this.root, arr=[]) {
	if(node) {
		if(node.left) {
			this.BSTtoArray(node.left, arr);
		}
		arr.push(node.data);
		if(node.right) {
			this.BSTtoArray(node.right, arr);
		}
	}
	return arr;
};

var x = new BST()
x.add(5).add(6).add(3).add(8).add(7).add(100).add(1).add(-1).add(-5).add(-7)
var bal = new BST()
// bal.add(5).add(3).add(7)
// x.min()
// x.max()
// console.log(x.find(3));
// console.log(x.find(100));
// console.log(x.size());
// console.log(x.height());
// console.log(bal.isBalanced());
var sorted = [0,1,2,3,4,5,6,7,8];
// console.log(bal.arrayToBST(sorted).isBalanced())
// console.log(bal.isBalanced(), "arrayToBST")
console.log(x.BSTtoArray())
