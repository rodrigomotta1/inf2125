var map;
var heatmap;

function initMap() {
    // Inicializa o mapa
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: { lat: -22.9068, lng: -43.1729 }, // Padrão: Rio de Janeiro
        mapTypeId: 'roadmap'
    });

    // Criando o Heatmap Layer
    heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData.map(function (point) {
            return {
                location: new google.maps.LatLng(point.lat, point.lng),
                weight: point.weight
            };
        }),
        radius: 40
    });

    heatmap.setMap(map);

    // Configurar a busca de locais
    setupSearchBox();
}

function setupSearchBox() {
    var input = document.getElementById('searchBox');
    var searchBox = new google.maps.places.SearchBox(input);

    // Quando o usuário seleciona um local na lista de sugestões
    searchBox.addListener('places_changed', function () {
        var places = searchBox.getPlaces();
        if (places.length == 0) return;

        var bounds = new google.maps.LatLngBounds();

        places.forEach(function (place) {
            if (!place.geometry) return;

            // Ajusta os limites do mapa para centralizar no local encontrado
            bounds.extend(place.geometry.location);
        });

        map.fitBounds(bounds);
        map.setZoom(15); // Ajusta o zoom para visualizar melhor o local
    });
}

window.onload = initMap;