console.log(React, ReactDOM);
var styles = {
	row: {height: "20px"},
	cell: {height: "20px", width: "20px", display: "inline-block"},
	colorA: {backgroundColor: "black"},
	colorB: {backgroundColor: "red"}
}

function Checkerboard(props) {
	const { number } = props;
	console.log("checkerboard number", number);

	let children = [];
	for(let i = 0; i < number; i++) {
		children.push(React.createElement(Row, {key: i, idx: i, number}, null));
	}

	return React.createElement("div", null, children);
}

function Row(props) {
	const { number } = props;
	const {row} = styles;
	const {colorA} = styles;
	const {colorB} = styles;
	const {cell} = styles;
	const {idx} = props;

	let children = [];
	let stop = number;
	let start = 0;
	if (idx % 2 !== 0) {
		stop += 1;
		start += 1;
	}
	for(let i = start; i < stop; i++) {
		console.log(i);
		children.push(React.createElement(Cell, {key: i, cell, color: i % 2 === 0 ? colorA : colorB}, null));
	};

	return React.createElement("div", {style: row}, children);
}

function Cell(props) {
	const { cell } = props;
	const { color } = props;
	return React.createElement("div", {style: {height: cell.height, width: cell.width, display: cell.display, backgroundColor: color.backgroundColor}});
}


ReactDOM.render(Checkerboard({number: 12}), document.getElementById("root"));
