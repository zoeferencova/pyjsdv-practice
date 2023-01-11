// RUN THIS USING python3 -m http.server DUE TO CORS ISSUE

window.d3 = d3;
d3.json("data/nobel_winners.json").then((data) => {
    console.log(data);
    makeChart(data);
});

function makeChart(data) {
    // rollup groups by gender, then category, and gives 
    // the array length of resulting groups as JS Map
    let cat_groups = d3.rollup(
        data,
        (v) => v.length,
        (d) => d.gender,
        (d) => d.category
    );
    let male = cat_groups.get("male");
    let female = cat_groups.get("female");
    let categories = [...male.keys()].sort();
    let traceM = {
        y: categories,
        // Map sorted categories to group values for bar chart heights
        x: categories.map((c) => male.get(c)),
        name: "male prize total",
        type: "bar",
        orientation: "h",
    };
    let traceF = {
        y: categories,
        x: categories.map((c) => female.get(c)),
        name: "female prize total",
        type: "bar",
        orientation: "h",
    };

    let traces = [traceM, traceF];

    // Increase left margin to accommodate long labels
    let layout = { barmode: "group", margin: { l: 160 } };

    Plotly.newPlot("gender-category", traces, layout);
}