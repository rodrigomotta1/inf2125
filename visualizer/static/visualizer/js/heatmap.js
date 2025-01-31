function initMap() {
    // Definição das coordenadas da Zona Sul do Rio de Janeiro
    var initialCenter = { lat: -22.970722, lng: -43.182365 }; // Próximo ao Leblon e Ipanema

    // Limites geográficos para restringir a movimentação
    var rioBounds = {
        north: -22.75,
        south: -23.10,
        west: -43.80,
        east: -43.05
    };

    // Inicializando o mapa com as configurações
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        minZoom: 10,
        center: initialCenter,
        restriction: {
            latLngBounds: rioBounds,
            strictBounds: true
        },
        mapTypeId: 'roadmap',
        styles: [
            {
                "featureType": "all",
                "elementType": "geometry",
                "stylers": [{ "color": "#e5e5e5" }]
            },
            {
                "featureType": "water",
                "elementType": "geometry",
                "stylers": [{ "color": "#c9c9c9" }]
            },
            {
                "featureType": "poi",
                "stylers": [{ "visibility": "off" }]
            },
            {
                "featureType": "road",
                "elementType": "geometry",
                "stylers": [{ "color": "#ffffff" }]
            },

            {
                "featureType": "road",
                "elementType": "labels.text.fill",
                "stylers": [{ "color": "#eeeeee" }]
            },
            {
                "featureType": "road.highway",
                "elementType": "geometry",
                "stylers": [{ "color": "#dadada" }]
            },
            {
                "featureType": "road.arterial",
                "elementType": "geometry",
                "stylers": [{ "color": "#f0f0f0" }]
            },
            {
                "featureType": "transit",
                "stylers": [{ "visibility": "off" }]
            }
        ]
    });

    // Criando o Heatmap Layer
    var heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData.map(function (point) {
            return {
                location: new google.maps.LatLng(point.lat, point.lng),
                weight: point.weight
            };
        }),
        radius: 40
    });

    heatmap.setMap(map);
}

window.onload = initMap;