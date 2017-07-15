function myMap(arr) {
//    function to populate map need to ament with loop through current stops
    var out = "";
    var mapCanvas = document.getElementById("map");
    var mapOptions = {
            center: new google.maps.LatLng(53.3498, -6.2603),
            zoom: 12
        }
        
    var map = new google.maps.Map(mapCanvas, mapOptions);
    var infoWindow = new google.maps.InfoWindow();
    for (var i = 0, length = arr.length; i < length; i++) {
        var data = arr[i],
            latLng = new google.maps.LatLng(data.Latitude, data.Longitude);


        var marker = new google.maps.Marker({
            position: latLng,
            map: map

        });


        (function (marker, data) {


            google.maps.event.addListener(marker, "mouseover", function (e) {
                infoWindow.setContent("Number: " + data.StopID + "<br/>Hello guys!!");
                infoWindow.open(map, marker);

            });
           

        })(marker, data);
    }
}

function load(code) {
    var xmlhttp = new XMLHttpRequest();
    var url = 'JSON/'+code+'.json';



    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var arr = JSON.parse(xmlhttp.responseText);
            myMap(arr);

        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();


}

$(document).ready(function(){
    // routes dropdown
$.getJSON('routes.json', function(data) {
    var jsonStr = JSON.stringify(data.routes[2].code); 
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
    //alert(obj.length);
     for (j; j <= obj.length; j++) {
    $('#dropdownstops1').append('<option name = "stop1" value='+obj[j].StopID+'>'+obj[j].StopID
    +'</option>');
                } }
    
   });

 } 

function gettime(){
    
   d = new Date();
    alert('hi');
    alert (d);
    $('#dropdowntime').append('<option name = "Time" value='+d+'>'+d
    +'</option>');}


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
document.getElementById('dt').innerHTML=today;
}


