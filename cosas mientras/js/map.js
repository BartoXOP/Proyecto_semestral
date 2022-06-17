var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 43.5293101, lng: -5.6773233},
    zoom: 19
    });
}