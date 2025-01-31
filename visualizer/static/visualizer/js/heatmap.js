var map;
var heatmap;

function initMap() {
    // Inicializa o mapa
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: { lat: -22.9068, lng: -43.1729 }, // Rio de Janeiro
        mapTypeId: 'roadmap',
        scrollwheel: true, // 🔹 Permite zoom com scroll
        styles: [
            {
                featureType: "poi",
                elementType: "all",
                stylers: [{ visibility: "off" }] // 🔹 Remove pontos de interesse irrelevantes
            },
            {
                featureType: "poi.attraction",
                elementType: "all",
                stylers: [{ visibility: "on" }] // 🔹 Mantém apenas atrações turísticas
            },
            {
                featureType: "transit",
                elementType: "all",
                stylers: [{ visibility: "on" }] // 🔹 Mantém informações de transporte
            },
            {
                featureType: "road",
                elementType: "geometry",
                stylers: [{ visibility: "simplified" }] // 🔹 Simplifica estradas
            },
            {
                featureType: "road",
                elementType: "labels",
                stylers: [{ visibility: "on" }] // 🔹 Mantém nomes das ruas
            },
            {
                featureType: "administrative.locality",
                elementType: "labels",
                stylers: [{ visibility: "on" }] // 🔹 Mantém nomes dos bairros
            }
        ]
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

    // Ajusta os limites de busca para a área visível do mapa
    map.addListener('bounds_changed', function () {
        searchBox.setBounds(map.getBounds());
    });

    // Quando o usuário seleciona um local na busca
    searchBox.addListener('places_changed', function () {
        var places = searchBox.getPlaces();
        if (places.length == 0) return;

        var bounds = new google.maps.LatLngBounds();
        var firstLocation = null;

        places.forEach(function (place, index) {
            if (!place.geometry) return;

            // Captura a primeira localização válida para centralizar o mapa
            if (index === 0) {
                firstLocation = place.geometry.location;
            }

            bounds.extend(place.geometry.location);
        });

        // Centraliza no local encontrado e ajusta o zoom
        if (firstLocation) {
            map.setCenter(firstLocation);
            map.setZoom(15); // 🔹 Ajusta o zoom para um nível adequado
        } else {
            map.fitBounds(bounds);
        }
    });
}

window.onload = initMap;
