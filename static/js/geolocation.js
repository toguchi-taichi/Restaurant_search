
geoFindMe();


function geoFindMe() {

    var success = (position) => {
        console.log('成功')
        const latitude  = position.coords.latitude;
        const longitude = position.coords.longitude;

        current.value = latitude + '\n' + longitude
            
        /*var latlng = new google.maps.LatLng(latitude, longitude );
        var map = new google.maps.Map( document.getElementById('map'),{
                zoom: 15 ,// ズーム値
                center: latlng ,// 中心座標

            });

        new google.maps.Marker( {
            map: map ,
            position: latlng ,
        });*/
    }

    function error() {
        console.log('エラー')
        status.textContent = 'Unable to retrieve your location';
    }

    

    if(!navigator.geolocation) {
        console.log('失敗だな')
        status.textContent = 'Geolocation is not supported by your browser';
    } else {
        console.log('あああああ')
        status.textContent = 'Locating…';
        navigator.geolocation.getCurrentPosition(success, error);
    }

}

