// The base endpoint to receive data from. See update_url()
var URL_BASE = "http://127.0.0.1:5000";

// Update graph in response to inputs
d3.select("#question").on("input", make_graph);
d3.select("#temperature").on("input", make_graph);
d3.select("#question").on("change", make_graph);
d3.select("#temperature").on("change", make_graph);

var margin = {
    top: 20,
    right: 20,
    bottom: 20,
    left: 20
};
var width = 800 - margin.left - margin.right;
var height = 800 - margin.top - margin.bottom;

var lastRequestTime = new Date();
/*
var x = d3.scale.linear()
    .range([0,  width])
    .domain([0, 25]);
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .ticks(6);
var y = d3.scale.linear()
    .range([height, 0]);
var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10);
*/

var svg = d3.select("#graph").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

var char_indices,indices_char;
d3.json(URL_BASE+"/indices/",function(error,data){
    char_indices = data.char_indices;
    indices_char = data.indices_char;
});
// Update the time displayed (XX:XX) next to the time slider
function update_slider(temperature) {
    d3.select("#prettyTemp")
        .text(temperature);
}

// Return url to recieve csv data with query filled in from input fields
function update_url() {
    return URL_BASE + "/ramon/"
        "?diversity=" + document.getElementById("temperature").value +
        "&text=" + document.getElementById("question").value;
}

var waitTime = 5; //In seconds
function make_graph() {
    update_slider(+document.getElementById("temperature").value);
    url = update_url();
    var now = new Date();
    if (parseInt((now - lastRequestTime) / 1000) > waitTime) {
        console.log("Ahora si, pidiendo");
        lastRequestTime = new Date();
        d3.json(url, function(error, data) {
            console.log(data);
            return;
        });
    } else {
        console.log("Espere "+parseInt(5-(now - lastRequestTime) / 1000)+" segundos");
    }
}

make_graph();



// x axis
/*svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .append("text")
      .text("ETD (minutes)")
      .attr("dy", "3em")
      .attr("text-align", "center")
      .attr("x", width / 2 - margin.right - margin.left);

// y axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
  .append("text")
    .attr("transform", "rotate(-90)")
    .attr("x", -height / 2)
    .attr("dy", "-2em")
    .text("Count");




       y.domain([0, d3.max(data, function(d) { return d.count; })]);

    svg.selectAll("g.y.axis")
      .call(yAxis);

    var bars = svg.selectAll(".bar")
      .data(data, function(d) { return d.etd; });

    bars.transition(1000)
      .attr("y", function(d) { return  y(d.count); } )
      .attr("height", function(d) { return height - y(d.count); } );

    bars.enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.etd); })
      .attr("width", x(1 - 2 * binMargin))
      .attr("y", height)
      .attr("height", 0)
      .transition(1000)
        .attr("y", function(d) { return y(d.count); })
        .attr("height", function(d) { return height - y(d.count); });

    bars.exit()
      .transition(1000)
        .attr("y", height)
        .attr("height", 0)
      .remove();



    */
