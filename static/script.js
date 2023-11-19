$(document).ready(function() {
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
