function BST() {
	this.root = null;
	this.add = add;
	this.min = min;
	this.max = max;
	this.find = find;
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
	console.log(curr);
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
		console.log(curr.data);
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

var x = new BST()
x.add(6).add(3).add(8).add(7)
x.min()
x.max()
console.log(x.find(3));
console.log(x.find(100));
// console.log(node1) 