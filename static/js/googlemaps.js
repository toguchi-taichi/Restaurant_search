
const uluru = { lat: -25.344, lng: 131.036 };

var MyLatLng = new google.maps.LatLng(35.6811673, 139.7670516);
var Options = {
    zoom: 15,      //地図の縮尺値
    center: uluru,    //地図の中心座標
    mapTypeId: 'roadmap'   //地図の種類
};
var map = new google.maps.Map(document.getElementById('map'), Options);

const marker = new google.maps.Marker({
  position: uluru,
  map: map,
});

