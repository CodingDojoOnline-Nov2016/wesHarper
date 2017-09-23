function tick() {
    const timeElement = React.createElement("h2", null, new Date().toLocaleTimeString());
    ReactDOM.render(timeElement, document.getElementById("app"));
}

setInterval(tick, 1000)
