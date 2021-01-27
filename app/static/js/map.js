function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 53.350631935496004,
            lng: -6.2599891096804585 },
        zoom: 12
    });

    // Set bounds within Dublin, source https://developers.google.com/maps/documentation/javascript/places-autocomplete#set-the-bounds-on-creation-of-the-autocomplete-object
    var defaultBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(53.350631935496004, -6.2599891096804585),
        new google.maps.LatLng(53.350631935496004, -6.2599891096804585));
    var options = {
        bounds: defaultBounds,
        strictBounds: false,
        types: ['address']
    };

    // Auto complete address
    const input = document.getElementById("address_1");
    const autocomplete = new google.maps.places.Autocomplete(input, options);
}
