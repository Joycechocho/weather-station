function WebSocketTest(){
    if ("WebSocket" in window){
        //alert("WebSocket is supported by your Browser!");
        ws = new WebSocket("ws://10.201.26.81:8888/ws");

        ws.onopen = function(){
            ws.send("7"); //send 7 to request data for chart
            alert("Congrats: Successful Connection !");
            var time = new Date().toLocaleString();
            document.getElementById("timestamp").innerHTML = "You are connecting to server at "+time;
        };


        ws.onmessage = function (evt){
            var received_msg = evt.data;
            //alert("Message is received: " + evt.data);
            obj_time = JSON.parse(evt.data);
            graph();
        };

        ws.onclose = function(){
            // websocket is closed.
            alert("Connection is closed...");
        };

        ws.onerror = function(){
            alert("There is something wrong...");
        };

        window.onbeforeunload = function(event) {
            socket.close();
        };

    }else{
        // The browser doesn't support WebSocket
        alert("WebSocket NOT supported by your Browser!");
    }
}

function Refresh(){
    try {
        ws.send("0"); //send 0 to request current data

        var time = new Date().toLocaleString();
        document.getElementById("timestamp").innerHTML = "You are requesting current temperature/humidity at "+time;

        ws.onmessage = function (evt){
            var received_msg = evt.data;
            obj_0 = JSON.parse(evt.data);
            document.getElementById("current_temp").innerHTML = (obj_0.current_temperature).toFixed(2)+"°";
            document.getElementById("current_humid").innerHTML =(obj_0.current_humidity).toFixed(1)+"%";
        };
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error: You must connect to the server first");
        }
    }
}

function Avg_Temp(){
    try {
        ws.send("1");

        var time = new Date().toLocaleString();
        document.getElementById("timestamp").innerHTML = "You are requesting average temperature at "+time;

        ws.onmessage = function (evt){
            var received_msg = evt.data;
            obj_1 = JSON.parse(evt.data);
            document.getElementById("Avg_Temp").innerHTML = (obj_1.average_temperature).toFixed(2)+"°";
        };
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error: You must connect to the server first");
        }
    }
}

function High_Temp(){
    try {
        ws.send("2");

        var time = new Date().toLocaleString();
        document.getElementById("timestamp").innerHTML = "You are requesting highest temperature at "+time;

        ws.onmessage = function (evt){
            var received_msg = evt.data;
            obj_2 = JSON.parse(evt.data);
            document.getElementById("High_Temp").innerHTML = (obj_2.high_temperature).toFixed(2)+"°";
        };
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error: You must connect to the server first");
        }
    }
}

function Low_Temp(){
    try {
        ws.send("3");

        var time = new Date().toLocaleString();
        document.getElementById("timestamp").innerHTML = "You are requesting lowest temperature at "+time;

        ws.onmessage = function (evt){
            var received_msg = evt.data;
            obj_3 = JSON.parse(evt.data);
            document.getElementById("Low_Temp").innerHTML = (obj_3.low_temperature).toFixed(2)+"°";
        };
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error: You must connect to the server first");
        }
    }
}

function Avg_Humid(){
    try {
        ws.send("4");

        var time = new Date().toLocaleString();
        document.getElementById("timestamp").innerHTML = "You are requesting average humidity at "+time;

        ws.onmessage = function (evt){
            var received_msg = evt.data;
            obj_4 = JSON.parse(evt.data);
            document.getElementById("Avg_Humid").innerHTML = (obj_4.average_humidity).toFixed(1)+"%";
        };
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error: You must connect to the server first");
        }
    }
}

function High_Humid(){
    try {
        ws.send("5");

        var time = new Date().toLocaleString();
        document.getElementById("timestamp").innerHTML = "You are requesting highest humidity at "+time;

        ws.onmessage = function (evt){
            received_msg = evt.data;
            obj_5 = JSON.parse(evt.data);
            document.getElementById("High_Humid").innerHTML = (obj_5.high_humidity).toFixed(1)+"%";
        };
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error: You must connect to the server first");
        }
    }
}

function Low_Humid(){
    try {
        ws.send("6");

        var time = new Date().toLocaleString();
        document.getElementById("timestamp").innerHTML = "You are requesting lowest humidity at "+time;

        ws.onmessage = function (evt){
            var received_msg = evt.data;
            obj_6 = JSON.parse(evt.data);
            document.getElementById("Low_Humid").innerHTML = (obj_6.low_humidity).toFixed(1)+"%";
        };
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error: You must connect to the server first");
        }
    }
}

function convert(degree) {
    try {
        var x;
        console.log(degree);
        if (degree == "C") {
            console.log("change to C..."+obj_0.current_temperature);
            document.getElementById("current_temp").innerHTML = (obj_0.current_temperature).toFixed(2)+"°";
            document.getElementById("Avg_Temp").innerHTML = (obj_1.average_temperature).toFixed(2)+"°";
            document.getElementById("High_Temp").innerHTML = (obj_2.high_temperature).toFixed(2)+"°";
            document.getElementById("Low_Temp").innerHTML = (obj_3.low_temperature).toFixed(2)+"°";
        } else {
            x = (obj_0.current_temperature) * 9 / 5 + 32;
            x1 = (obj_1.average_temperature) * 9 / 5 + 32;
            x2 = (obj_2.high_temperature) * 9 / 5 + 32;
            x3 = (obj_3.low_temperature) * 9 / 5 + 32;
            document.getElementById("current_temp").innerHTML = x.toFixed(2)+"°";
            document.getElementById("Avg_Temp").innerHTML = x1.toFixed(2)+"°";
            document.getElementById("High_Temp").innerHTML = x2.toFixed(2)+"°";
            document.getElementById("Low_Temp").innerHTML = x3.toFixed(2)+"°";
        }
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error: You must request all the temperature data first");
        }
    }
}

function date_time(id){
    date = new Date;
    year = date.getFullYear();
    month = date.getMonth();
    months = new Array('January', 'February', 'March', 'April', 'May', 'June', 'Jully', 'August', 'September', 'October', 'November', 'December');
    d = date.getDate();
    day = date.getDay();
    days = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');
    h = date.getHours();
    if(h<10){
        h = "0"+h;
    }
    m = date.getMinutes();
    if(m<10){
    m = "0"+m;
    }
    s = date.getSeconds();
    if(s<10){
    s = "0"+s;
    }
    result = ''+days[day]+' '+months[month]+' '+d+' '+year+' '+h+':'+m+':'+s;
    document.getElementById(id).innerHTML = result;
    setTimeout('date_time("'+id+'");','1000');
    return true;
}

function graph(){
    var labeldata = [];
    var chrtdata = [];

    for(var i =1; i < Object.keys(obj_time).length+1; i++){
        labeldata.push(i+":00");
        chrtdata.push(obj_time[i])
    }

    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labeldata,
            datasets: [{
                label: 'Temperature',
                data: chrtdata,
                backgroundColor: "rgba(192,192,192,0.3)"
            }]
        }
    });
 }


window.onload = function () {
    var labeldata = [];
    var chrtdata = [];
    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labeldata,
            datasets: [{
                label: 'Temperature',
                data: chrtdata,
                backgroundColor: "rgba(192,192,192,0.3)"
            }]
        }
    });
}




