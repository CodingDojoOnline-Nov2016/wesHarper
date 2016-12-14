function Node(data) {
	this.data = data;
	this.next = null;
}

function SList() {
	this.head = null;
	this.isEmpty = isEmpty;
	this.addFront = addFront;
	this.length = length;
	this.addBack = addBack;
	this.removeFront = removeFront;
	this.removeBack = removeBack;
	this.contains = contains;
	this.show = show;
	this.removeValue = removeValue;
}

function isEmpty() {
	return !this.head;
}

function addFront(data) {
	var n = new Node(data)
	if(this.isEmpty()) {
		this.head = n;
	} else {
		n.next = this.head;
		this.head = n;
	}
	return this;
}

function length() {
	var count = 0;
	if(!this.isEmpty()){
		var cur = this.head;
		while(cur) {
			count++;
			cur = cur.next;
		}
	}
	return count;
}

function addBack(data) {
	var n = new Node(data)
	if(!this.isEmpty()){
		var cur = this.head;
		while(cur.next) {
			cur = cur.next;
		}
		cur.next = n;
	} else {
		this.head = n;
	}
	return this;
}

function removeFront() {
	if(this.head) {
		var temp = this.head.next;
		this.head.next = null;
		this.head = temp;
	}
	return this;
}

function removeBack() {
	if(this.head && this.head.next) {
		var cur = this.head;
		while(cur.next.next) {
			cur = cur.next;
		}
		cur.next = null;
	} else {
		this.head = null;
	}
	return this;
}

function contains(val) {
	if(this.head) {
		var cur = this.head;
		while(cur) {
			if(cur.data === val) {
				return true;
			}
			cur = cur.next;
		}
	}
	return false;
}

function show() {
	var array = [];
	var cur = this.head;
	while(cur) {
		array.push(cur.data);
		cur = cur.next;
	}
	console.log(array);
	return this;
}

function removeValue(value, int) { //optional int defines how many removals to do
	if(!int) {
		int = 1;
	}
	if(this.head) {
		var cur = this.head;
		while(cur && int > 0) {
			if(cur.next && cur.next.data == value) {
				var temp = cur.next;
				cur.next = temp.next;
				temp.next = null;
				int--;
			} else {
			cur = cur.next;
			}
		}
	}
	return this;
}

var myList = new SList();
myList.addBack('z').addFront('a').addBack('b').addBack(1).addBack(1).addBack(1).show();
myList.removeValue(1).show();