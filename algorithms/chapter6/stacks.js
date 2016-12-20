function Node(data) {
	var _data = data; //hides data because var _data is locally scoped, it only exists inside the function
	var _next = null;
	this.getData = function() {
		return _data;
	}
	this.setNext = function(next) {
		_next = next;
		return this;
	}
	this.getNext = function() {
		return _next;
	}
}


function Stack() {
	var _head = null;
	this.push = function(data) {
		if (!(data instanceof Node)) {
			var n = new Node(data);
			n.setNext(_head);
			_head = n;
			return this;
		} else {
			data.setNext(_head);
			_head = data;
			return this;
		}
	}
	this.pop = function() { //pop from front and return the whole node that's been popped
		if(_head) {
			var temp = _head;
			_head = temp.getNext();
			temp.setNext(null);
			return temp.getData();
		}
	}
	this.top = function() { //remove and add to front of list
		if(_head) {
			return _head.getData();
		}
		return null;
	}
	this.isEmpty = function() {
		return !_head;
	}
	this.show = function() {
		var array = [];
		var cur = _head;
		while(cur) {
			array.push(cur.getData());
			cur = cur.getNext();
		}
		console.log(array);
		return this;
	}
	// this.contains = function() {}
	// this.size = function() {}
}


var s = new Stack();

s.push('a').push('b').push('c').show()
console.log(s.pop())
s.show()