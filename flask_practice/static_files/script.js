let loadCountryWinnersJSON = function (country) {
    d3.json("data/winners_by_country/" + country + ".json")
        .then(function (data) {
            d3.select("h2#data-title").text(
                "All the Nobel-winners from " + country
            );
            d3.select("div#data pre").html(JSON.stringify(data, null, 4));
        })
        .catch((error) => console.log(error));
};

loadCountryWinnersJSON('Australia');
