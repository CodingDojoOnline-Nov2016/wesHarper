console.log(React ? "React found" : "React not found", ReactDOM ? "ReactDOM found" : "Can't find ReactDOM");

const header = React.createElement("h1", null, "Hello Dojo!");
const secondary = React.createElement("h2", null, "Things I need to do:");
const listItem = React.createElement("a", null, "Learn React");
const listItem2 = React.createElement("a", null, "Another thing");

let doc = document;
ReactDOM.render(header, doc.getElementById("header"));
ReactDOM.render(secondary, doc.getElementById("secondary"));
ReactDOM.render(listItem, doc.getElementById("list1"));
ReactDOM.render(listItem2, doc.getElementById("list2"));
