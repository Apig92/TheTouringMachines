function myMap() {
    //produces map , creates markers for users specified route

    x = ReadCookie('route');
    xy = ReadCookie('start');
    xyz = ReadCookie('stop')
    
    $.getJSON('JSON/' + x + '.json', function (obj) {
        var out = "";
        var counter = 1;
        var half = Math.floor(obj.length / 2); // half of the json array
        var mapCanvas = document.getElementById("map");
        var mapOptions = {
            center: new google.maps.LatLng(obj[half].Latitude, obj[half].Longitude), //centre of map is centre of route
            zoom: 13
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);
        var infoWindow = new google.maps.InfoWindow();
        var bounds = new google.maps.LatLngBounds();
         var icon1 = {
                    url: "Images/icon (2).png",
                    scaledSize: new google.maps.Size(70, 70), // scaled size
                    origin: new google.maps.Point(0, 0), // origin
                    anchor: new google.maps.Point(30, 70) // anchor
                };

        for (var n in obj) {
            if (obj[n].StopID == xy) {
                var j = n;
                latLng = new google.maps.LatLng(obj[n].Latitude, obj[n].Longitude);
                bounds.extend(latLng);
                map.fitBounds(bounds);

                var marker = new google.maps.Marker({
                    position: latLng,
                    map: map,
                    icon: icon1

                });
            }
        }
        
        for (j; j <= obj.length; j++) {
            data = obj[j];
            counter ++;
            if (data.StopID == xyz) { //break at last one
                latLng = new google.maps.LatLng(data.Latitude, data.Longitude);7
                bounds.extend(latLng);
                map.fitBounds(bounds);
                var marker = new google.maps.Marker({
                    position: latLng,
                    map: map,
                    icon: icon1

                });
                break;
            }
            
            latLng = new google.maps.LatLng(data.Latitude, data.Longitude);
            bounds.extend(latLng);
                map.fitBounds(bounds);
            var iconImage = {
                url: "Images/rec.png",
                scaledSize: new google.maps.Size(15, 15), 
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(0, 0) 
            };

            var marker = new google.maps.Marker({
                position: latLng,
                map: map,
                icon: iconImage

            }); bounds.extend(marker.getPosition());


            (function (marker, data) {

                google.maps.event.addListener(marker, "mouseover", function (e) {
                    infoWindow.setContent("Bus Stop: " + data.StopID + "");
                    infoWindow.open(map, marker);

                });


            })(marker, data);
        } 
        document.getElementById("counter").innerHTML = "The number of stops is: " + counter;
    });

}

$(document).ready(function(){
    // routes dropdown
    var dir = 'JSON/routes.json';
$.getJSON(dir, function(data) {
    //var jsonStr = JSON.stringify(data.routes[2].code);
    for( var i in data.routes ) {
        $('#dropdownroutes').append('<option name = "route" value='+data.routes[i].code+'>'+data.routes[i].number
   +'</option>');
    }
  });
});


function Cookies(){
               // makes and stores cookies
               route= document.getElementById('dropdownroutes').value + ";";
               document.cookie="route=" + route;
               start = document.getElementById('dropdownstops').value + ";";
               document.cookie="start=" + start;
               stop = document.getElementById('dropdownstops1').value + ";";
               document.cookie="stop=" + stop;
               date = document.getElementById('dt').value + ";";
               document.cookie="date=" + date;
               time = document.getElementById('time').value + ";";
               document.cookie="time=" + time;
               
                           }

function ReadCookie(cookiename){
    //gets cookiename
var name = cookiename + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}


function stopselect(){
    //dropdown for starting stop
    x = ReadCookie('route');
    $.getJSON('JSON/'+x+'.json', function(obj) {
    for( var i in obj ) {
        $('#dropdownstops').append('<option name = "stop1" value='+obj[i].StopID+'>'+obj[i].StopID
   +'</option>');
   }
    });

 } 

function endstopselect(){
    //dropdown for destination
   x = ReadCookie('route');
   xy = ReadCookie('start');
    $.getJSON('JSON/'+x+'.json', function(obj) {
    for( var n in obj ) {
        if (obj[n].StopID == xy){
           var j = n;
        }
     for (j; j <= obj.length; j++) {
    $('#dropdownstops1').append('<option name = "stop1" value='+obj[j].StopID+'>'+obj[j].StopID
    +'</option>');
                } }
    
   });

 } 

function gettime() {

    d = new Date();
    //alert('hi');
    alert(d);
    $('#dropdowntime').append('<option name = "Time" value=' + d + '>' + d +
        '</option>');
}

function reloadpage() {
    location.reload();
}


function getdate(){
    //display todays date in correct format - needs to be default value
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();

if(dd<10) {
    dd = '0'+dd
} 

if(mm<10) {
    mm = '0'+mm
} 

today = mm + '/' + dd + '/' + yyyy;
return today;
}


