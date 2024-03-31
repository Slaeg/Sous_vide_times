//The javascript uses jQuery to handle interaction with the Flask backend:
//The document ready funtion ensures that the code inside it only runs after the entire page (DOM) is fully loaded:
$(document).ready(function() {
    // Autocomplete feature for the food type input
    $("#food_type").autocomplete({
        source: function(request, response) {
            // Fetching food types matching the current input
            $.getJSON("/food_types?query=" + encodeURIComponent(request.term), function(data) {
                response(data);
            });
        },
        minLength: 1, // Minimum length of input to start showing suggestions
        select: function(event, ui) {
            // Optionally do something when a suggestion is selected
            $("#food_type").val(ui.item.value);
            return false;
        }
    });

    // Existing search form submission handling
    $("#search-form").submit(function(event) {
        event.preventDefault();
        var foodType = $("#food_type").val();
        $.get("/times?food_type=" + encodeURIComponent(foodType), function(data) {
            $("#result").empty();
    
            data.forEach(function(item) {
                $("#result").append("<p>Food Type: " + item.food_type + "<br>Temperature: " + item.temperature + "<br>Cooking Time: " + item.cooking_time + "</p>");
            });
        });
    });    
});
