// The base endpoint to receive data from Flask
var URL_BASE = "http://127.0.0.1:5000";
var rectW = rectH = 30; // Size of the squares
var lettersToRequest = 20;
var probabilitiesToShow = 10;

// SVG and D3 stuff
var margin = {
    top: 5,
    right: 5,
    bottom: 5,
    left: 5
};
var width = lettersToRequest*rectW - margin.left - margin.right;
var height = probabilitiesToShow*rectH - margin.top - margin.bottom;

var svg = d3.select("#graph").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .attr("class", "center-block")
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

var char_indices, indices_char;
d3.json(URL_BASE + "/indices/", function (error, data) {
    char_indices = data.char_indices;
    indices_char = data.indices_char;
});

// Return url to recieve csv data with query filled in from input fields
function update_url() {
    return URL_BASE + "/ramon/"+
    "?diversity=" + document.getElementById("temperature").value +
        "&chars="+lettersToRequest+
        "&text=" + document.getElementById("question").value;
}

var colorScale = d3.scale.linear().domain([0, 1]).range(["white", "#b935e0"]);

function update_graph() {
    url = update_url();
    console.log(url);
    d3.json(url, function (error, rawdata) {
        var data = [{
                "step": 0,
                "probability": 0,
                "rank": 0,
                "char": url[url.length-1]
            }];
        for (var step = 0; step < rawdata.text.length; step++) {
            var char = rawdata.text[step];
            data.push({
                "step": step+1,
                "probability": 0,
                "rank": 0,
                "char": char
            });
            var probs = [];
            rawdata.probabilities[step].forEach(function (d, i) {
                probs.push({
                    "idx": i,
                    "probability": d
                });
            });
            sortedProbs = probs.sort(function (a, b) {
                return b.probability - a.probability
            });
            sortedProbs.forEach(function (p, j) {
                if (j < 10) {
                    data.push({
                        "step": step,
                        "probability": p.probability,
                        "rank": j + 1,
                        "char": indices_char[p.idx]
                    })
                }
            });
        }
        d3.selectAll("rect").remove();
        d3.selectAll("text").remove();
        var rectangles = svg.selectAll("rect")
            .data(data)
            .enter().append("g")
            .attr("transform", function (d) {
                return "translate(" + (d.step * rectW) + "," + (d.rank * rectH) + ")";
            });
        rectangles.append("rect")
            .attr("width", rectW - 1)
            .attr("height", rectH - 1)
            .style("fill", function (d) {
                return colorScale(d.probability);
            });
        rectangles.append("text")
            .attr("x", rectW / 2)
            .attr("y", rectH / 2)
            .attr("dx", 0)
            .attr("dy", "0.35em")
            .style("text-anchor", "center")
            .text(function (d) {
                return d.char;
            });
    });
}

function update_slider(temperature) {
    d3.select("#prettyTemp")
        .text(temperature);
}

var idleTime = 0;
var somethingChanged = false;

// Any update resets the timer to zero, we wait until idle time to reload
d3.select("#question").on("input", function (e) {
    idleTime = 0;
    somethingChanged = true;
});
d3.select("#temperature").on("input", function (e) {
    update_slider(+document.getElementById("temperature").value);
    idleTime = 0;
    somethingChanged = true;
});
d3.select("#question").on("change", function (e) {
    idleTime = 0;
    somethingChanged = true;
});
d3.select("#temperature").on("change", function (e) {
    update_slider(+document.getElementById("temperature").value);    
    idleTime = 0;
    somethingChanged = true;
});


//Increment the idle time counter every quarter of a second.
var idleInterval = setInterval(timerIncrement, 1000); 

function timerIncrement() {
    idleTime = idleTime + 1;
    if (idleTime > 3 && somethingChanged) { // 2 seconds inactive
        idleTime=0;
        somethingChanged=false;
        update_graph();
    }
}