AMAZONIANVOICES = {};

AMAZONIANVOICES.style = function(feature) {
    return {
            'color': '#000',
            'weight': 1,
            'opacity': 0.6,
            'fillOpacity': 0.3,
            'fillColor': feature.properties.fill
    }
};
AMAZONIANVOICES.map_with_taxa_on_init = function (map) {
    var pixel_ratio = parseInt(window.devicePixelRatio) || 1;
    var layers = {};
    var max_zoom = 16;
    var tile_size = 512;
    var index = 0;
    var color = 'classic';
    var url = 'https://api.gbif.org/v2/map/occurrence/density/{z}/{x}/{y}@{r}x.png?taxonKey={t}&style={c}.poly&bin=hex&hexPerTile=50&srs=EPSG%3A3857';

    if (taxa === undefined) {
        return;
    }
    //'classic.poly', 'green.poly'

    for (name in taxa) {
        color = index % 2 === 0 ? 'classic' : 'green'
        tl = L.tileLayer(
            url.replace('{r}', pixel_ratio).replace('{t}', taxa[name]).replace('{c}', color),
            {
                minZoom: 1,
                maxZoom: max_zoom + 1,
                zoomOffset: -1,
                tileSize: tile_size
            }).addTo(map.map);
        layers[name] = tl;
        index += 1;
    }
    L.control.layers(
        {},
        layers,
        {collapsed: false}).addTo(map.map);
}

CLLD.LayerOptions.polys = {
    style: AMAZONIANVOICES.style,
    onEachFeature: function(feature, layer) {
        layer.bindTooltip(feature.properties.title);
    }
};
