function myMap() {
    //produces map , creates markers for users specified route

    x = ReadCookie('route');
    xy = ReadCookie('start');
    xyz = ReadCookie('stop')
    routename  = ReadCookie('nameroute')
    $.getJSON('JSON/routeinfo.json', function (json) {
        obj = json[x];
        var counter = 0;
        var half = Math.floor(obj.length / 2); // half of the json array
        var mapCanvas = document.getElementById("map");
        var mapOptions = {
            center: new google.maps.LatLng(obj[half].Latitude, obj[half].Longitude), //centre of map is centre of route if no stops are picked
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
                latLng = new google.maps.LatLng(data.Latitude, data.Longitude);
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
        document.getElementById("counter").innerHTML = "The number of stops is: " + (counter - 1);
        document.getElementById("nameofroute").innerHTML = "Route: " + routename;
        document.getElementById("stops").innerHTML = "First stop: " + xy +"<br/> Destination Stop: "+xyz;
        
    });

}




$(document).ready(function(){
    // routes dropdown
$.getJSON('routes.json', function(data) {
    for( var i in data ) {
        $('#dropdownroutes').append('<option value='+ [data[i].code, data[i].number] +'>'+data[i].number
   +'</option>');
        
    }
  });
});


function Cookies(){
               // makes and stores cookies
               routestr= document.getElementById('dropdownroutes').value; //split the string of value for name and code
               route =routestr.split(',')[0] + ";";
               nameroute = routestr.split(',')[1]+ ";";
               document.cookie="route=" + route;
               document.cookie="nameroute=" + nameroute;
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
    //gets cookiename reference this
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
    $.getJSON('JSON/routeinfo.json', function(json) {
    obj = json[x];
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
    $.getJSON('JSON/routeinfo.json', function(json) {
    obj = json[x];
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
    //need to add if statements for bank holidays and christmas - future work :)
var today = new Date();
var weekday = today.getDay();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();
var day = new Array(7);
day[0] = "Sunday";
day[1] = "Monday";
day[2] = "Tuesday";
day[3] = "Wednesday";
day[4] = "Thursday";
day[5] = "Friday";
day[6] = "Saturday";
var week_day_loop = ""; //Week day loop to generate Today, Tomorrow and the correct following days depending on the day the user is viewing the site.
    
if(dd<10) {
dd = '0'+dd
} 

if(mm<10) {
    mm = '0'+mm
} 

for (var i = 0; i < 7; i++) {
    var value = weekday + i;
    if (value < 7) {
        var j = value;
    } else {
        var j = value - 7;
    }
    if (j==0){
        var pythonvalue = 6; //in python 0 is Monday and 6 is Sunday
    }
    else {
        var pythonvalue = j - 1;
    }


    if (i == 0) {
        week_day_loop = "Today";
    } else if (i > 1) {
        week_day_loop = day[j];
    } else {
        week_day_loop = "Tomorrow";
    }

    $('#dt').append('<option name = "date" value=' +pythonvalue+ '>' + week_day_loop + '</option>');
}
}

function weatherJSON(){
        $.getJSON("http://api.openweathermap.org/data/2.5/forecast?id=2964574&APPID=e9da13ccf40ebb756a8680b64650d626",function(json){
            document.write(JSON.stringify(json));
        });
    }