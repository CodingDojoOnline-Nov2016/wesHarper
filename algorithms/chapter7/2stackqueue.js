var Stack = require("../chapter6/stacks.js").Stack
var Node = require("../chapter6/stackNode.js").Node

function SlinQy() {
	this.storage = new Stack();
	this.tempStorage = new Stack();
	this.enqueue = enqueue;
	this.dequeue = dequeue;
	this.front = front;
}

function enqueue(data) {
	var n = new Node(data);
	this.storage.push(n).show();
	return this;
}

function dequeue() {
	
}

function front() {

}

var s = new SlinQy();
console.log(s.enqueue('a'))