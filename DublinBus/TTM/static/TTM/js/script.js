function myMap() {
    //produces map , creates markers for users specified route

    x = ReadCookie('route');
    xy = ReadCookie('start');
    xyz = ReadCookie('stop');
    routename  = ReadCookie('nameroute');
    //alert(routename);
    $.getJSON('../static/TTM/JSON/routeinfo.json', function (json) {
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
                    url: "../static/TTM/images/icon_circle.png",
                    scaledSize: new google.maps.Size(70, 70), // scaled size
                    origin: new google.maps.Point(0, 0), // origin
                    anchor: new google.maps.Point(30, 70) // anchor
                };
        var trafficLayer = new google.maps.TrafficLayer();
                trafficLayer.setMap(map);
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
                url: "../static/TTM/images/icon_rec.png",
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
        document.getElementById("counter").innerHTML = "Stops: " + (counter - 1);
        document.getElementById("nameofroute").innerHTML = "Route: " + routename;
        document.getElementById("firststop").innerHTML = "First stop: " + xy;
        document.getElementById("endstop").innerHTML = "Last Stop: "+ xyz;
    });

}




$(document).ready(function(){
    // routes dropdown
$.getJSON('../static/TTM/JSON/routes.json', function(data) {
    var data = data.routes;
    for( var i in data ) {
        $('#dropdownroutes').append('<option value='+ [data[i].code, data[i].number] +'>'+data[i].number
   +'</option>');

    }
  });
});

function Cookies(){
               // makes and stores cookies
    routestr = document.getElementById('dropdownroutes').value; //split the string of value for name and code
    route = routestr.split(',')[0] + ";";
    nameroute = routestr.split(',')[1] + ";";
    document.cookie = "route=" + route;
    document.cookie = "nameroute=" + nameroute;
    line = nameroute.match(/\d+/)[0];
    document.cookie = "line=" + line;
    start = document.getElementById('dropdownstops').value + ";";
    document.cookie = "start=" + start;
    stop = document.getElementById('dropdownstops1').value + ";";
    document.cookie = "stop=" + stop;
}
function Cookies1(){
               // makes and stores cookies

    routestr = document.getElementById('dropdownroutes').value; //split the string of value for name and code
    route = routestr.split(',')[0] + ";";
    nameroute = routestr.split(',')[1] + ";";
    document.cookie = "userroute=" + route;
    document.cookie = "usernameroute=" + nameroute;
    line = nameroute.match(/\d+/)[0];
    document.cookie = "userline=" + line;
    start = document.getElementById('dropdownstops').value + ";";
    document.cookie = "userstart=" + start;
    stop = document.getElementById('dropdownstops1').value + ";";
    document.cookie = "userstop=" + stop;
}

function timedate(){
    date = document.getElementById('dt').value + ";";
    document.cookie = "date=" + date;
    time = document.getElementById('time').value + ";";
    document.cookie = "time=" + time;}

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


function stopselect() {
    //dropdown for starting stop
    x = ReadCookie('route');
    $.getJSON('../static/TTM/JSON/routeinfo.json', function(json) {
        obj = json[x];
        for (var i in obj) {
            $('#dropdownstops').append('<option name = "start" value=' + obj[i].StopID + '>' + obj[i].Stop_name+ " "+ obj[i].StopID +                '</option>');
        }
    });

}

function endstopselect() {
    //dropdown for destination
    x = ReadCookie('route');
    xy = ReadCookie('start');
    $.getJSON('../static/TTM/JSON/routeinfo.json', function(json) {
        obj = json[x];
        for (var n in obj) {
            if (obj[n].StopID == xy) {
                var j = n;
            }
            for (j; j <= obj.length; j++) {
                $('#dropdownstops1').append('<option name = "stop" value=' + obj[j].StopID + '>'+ obj[j].Stop_name+ " "+ obj[j].StopID +
                    '</option>');
            }
        }

    });

}

function gettime() {
    var time_loop = "";
    var d = new Date();
    var n = d.getTime();
    var hour = d.getHours();
    time = hour + ";";
    document.cookie = "time=" + time;
    var min = d.getMinutes();
    var j = parseInt(ReadCookie('date'));
    if (min < 10) {
       min= '0' + min;}
    if (min < 30) {
        newhour = hour;
    } else {
        newhour = hour + 1;
    }

    if (j == 6) {
        var thisday = 0; //change to javascript
    } else {
        var thisday = (j + 1);
    }
    //alert(thisday);
     var option = $('<option name = "time" value=' + newhour + '>' + hour + ':' + min + '</option>');
    $("#time").empty().append(option);//delete options and replace with current time
    if (thisday == d.getDay()) {
        for (var i = newhour; i < 24; i++) {
        var value =i;
        if (i > 0) {
        time_loop = ""+value+":00";
        }

        $('#time').append('<option name = "time" value=' +value+ '>' + time_loop + '</option>');
    }

    }
    else {
         for (var i = 6; i < 24; i++) {
        var value =i;
        time_loop = ""+value+":00";
        $('#time').append('<option name = "time" value=' +value+ '>' + time_loop + '</option>');
    }}


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


function weatherJSON() {
    //takes in current day and displays 7 day forecast
    var out = "";
    var out1 = "";
    var today = new Date();
    var weekday = today.getDay();
    var i;
    var x = 1 + parseInt(ReadCookie('date'));
    if ( x >= weekday){
        i = x - weekday;}
    else {
       i = (x + 7) - weekday; //keep it within mod 7
    }



    $.getJSON("../static/TTM/JSON/weather.json", function (json) {

                    var list = json.list[i];
                    var temp = (list.temp.day - 273).toFixed(2);
                    var main = list.main;
                    var weather = list.weather[0];
                    var clouds = list.clouds;
                    var wind = list.speed;
                    var rain = list.rain;
                    if (rain == undefined){
                        rain = 0;
                    }
                    var time = parseInt(list.dt);
                    var x = time * 1000;
                    var n = String(new Date(x));
                    n = n.substring(0, 15);
                    var Icon = "<img src='http://www.openweathermap.org/img/w/" + weather.icon + ".png'>";

                    temperature = temp + ";";
                    document.cookie = "temp=" + temp;
                    windspeed = wind + ";";
                    document.cookie = "wind=" + wind;
                    rainfall = rain + ";";
                    document.cookie = "rain=" + rain;

out1 = "<div class='date1'>"+n+","+Icon+"</div>";
out = "<div class='table2'><table>";
out += "<tr><td>" + Icon + "</td><td>Temp: " + temp + "°C</td>";
out += "</table></div>";
document.getElementById("weather").innerHTML = out1;
document.getElementById("detailedweather").innerHTML = out;


    }

    );

    }

function todaysweather() {
    var out = "";
    var out1= "";
    $.getJSON("../static/TTM/JSON/weather.json", function (json) {

                    var list = json.list[0];
                    var temp = (list.temp.day - 273).toFixed(2);
                    var main = list.main;
                    var weather = list.weather[0];
                    var clouds = list.clouds;
                    var wind = list.speed;
                    var rain = list.rain;
                    if (rain == undefined){
                        rain = 0;
                    }
                    var time = parseInt(list.dt);
                    var x = time * 1000;
                    var n = String(new Date(x));
                    n = n.substring(0, 15);
                    var Icon = "<img src='http://www.openweathermap.org/img/w/" + weather.icon + ".png'>";

                    temperature = temp + ";";
                    document.cookie = "temp=" + temp;
                    windspeed = wind + ";";
                    document.cookie = "wind=" + wind;
                    rainfall = rain + ";";
                    document.cookie = "rain=" + rain;

out1 = "<div class='date1'>"+n+","+Icon+"</div>";
out = "<div class='table1'><table>";
//out += "<tr><td>" + Icon + "</td><td>Temp: " + temp + "°C</td><td> Wind: " + wind + "m/s</td><td> Clouds: " + clouds + "%</td><td> Rain: " + rain + "mm</td>";
out += "<tr><td>" + Icon + "</td>";
out += "</table></div>";
document.getElementById("weather1").innerHTML = out1;


    }

    );
}

function convertroute(){
 $.getJSON('../static/TTM/JSON/indexes.json', function(json) {
    jpid = ReadCookie('route')
    var routeindex = json[jpid];
    indexroute = routeindex + ";";
    document.cookie = "routeindex=" + indexroute;

   });
}

function convertroute1(){
 $.getJSON('../static/TTM/JSON/indexes.json', function(json) {
    jpid = ReadCookie('route')
    var routeindex = json[jpid];
    indexroute = routeindex + ";";
    document.cookie = "userrouteindex=" + indexroute;

   });
}

//get the last two tweets from AA
function AAtweets() {
    var out = "";
    $.getJSON("../static/TTM/JSON/AAtweets.json", function (data) {
        var data0 = data["tweets"];
        var last1 = data0.slice(-1)[0];
        var last2 = data0.slice(-2)[0];
    out = last2 + "<br>" + last1;
    document.getElementById("AAtweet").innerHTML = out;
    });
}

//get the last four tweets from DublinBus
function DBtweets() {
    var out = "";
    $.getJSON("../static/TTM/JSON/DBtweets.json", function (data) {
        var data0 = data["tweets"];
        var last1 = data0.slice(-1)[0];
        var last2 = data0.slice(-2)[0];
        var last3 = data0.slice(-3)[0];
        var last4 = data0.slice(-4)[0];
    out = last4 + "<br>" + last3 + "<br>" + last2 + "<br>" + last1;
    document.getElementById("DBtweet").innerHTML = out;
    });
}
