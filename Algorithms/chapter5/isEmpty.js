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

var myList = new SList();
myList.addBack('z').addFront('a');
myList.addFront('a');
console.log(myList);