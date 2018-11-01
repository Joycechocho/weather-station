//queueUrl = <queueUrl>
queueUrl = <queueUrl>

numberDataSent_data = [];
numberDataReceived_data = [];
timeData_data = [];

function queue(){
    append_sent_time = [];
    append_cur_temp = [];
    append_cur_hum = [];
    append_ave_temp = [];
    append_ave_hum = [];
    append_high_temp = [];
    append_high_hum = [];
    append_low_temp = [];
    append_low_hum = [];
    append_protocol_message = [];

    var time = new Date().toLocaleString();
    document.getElementById("timestamp").innerHTML = "You are requesting AWS SQS data at "+time;

    AWS.config.update({
//        accessKeyId: <ACCES KEY ID>,
//        secretAccessKey:  <SECRET KEY ID>,
        accessKeyId: <ACCES KEY ID>,
        secretAccessKey: <SECRET KEY ID>,
        region: 'us-west-2'
        });
    var sqs = new AWS.SQS();

    var params = {
        AttributeNames:[
                'SentTimestamp',
        ],
        MaxNumberOfMessages: 1,
        MessageAttributeNames: [
            "All"
        ],
        QueueUrl: queueUrl,
        VisibilityTimeout: 10,
        MaxNumberOfMessages : 10,
        WaitTimeSeconds: 10
    };

    sqs.receiveMessage(params, function (err, data) {
        if (err)
            console.log(err, err.stack);
        if (data.Messages) {
                if( data.Messages.length < 10) alert("Be patient! Waiting for more data in the Queue.");
                for (var i = 0; i < data.Messages.length; i++) {
                    sent_time = data.Messages[i].Attributes.SentTimestamp;
                    cur_temp = data.Messages[i].MessageAttributes.Current_temperature.StringValue;
                    cur_hum = data.Messages[i].MessageAttributes.Current_humidity.StringValue;
                    ave_temp = data.Messages[i].MessageAttributes.Average_temperature.StringValue;
                    ave_hum =  data.Messages[i].MessageAttributes.Average_humidity.StringValue;
                    high_temp = data.Messages[i].MessageAttributes.High_temperature.StringValue;
                    high_hum = data.Messages[i].MessageAttributes.High_humidity.StringValue;
                    low_temp = data.Messages[i].MessageAttributes.Low_temperature.StringValue;
                    low_hum = data.Messages[i].MessageAttributes.Low_humidity.StringValue;

                    displayData();

                    append_sent_time.push(timeConverter(sent_time));
                    append_cur_temp.push(cur_temp);
                    append_cur_hum.push(cur_hum);
                    append_ave_temp.push(ave_temp);
                    append_ave_hum.push(ave_hum);
                    append_high_temp.push(high_temp);
                    append_high_hum.push(high_hum);
                    append_low_temp.push(low_temp);
                    append_low_hum.push(low_hum);

                    append_protocol_message.push(cur_temp,cur_hum,ave_temp,ave_hum,high_temp,high_hum,low_temp,low_hum);

//                  var message = data.Messages[i]
//                  sqs.deleteMessage({
//                      QueueUrl : queueUrl,
//                      ReceiptHandle : message.ReceiptHandle
//                  }, function(err, data) {
//                      err && console.log(err);
//                      console.log(data+"has been deleted")
//                  });
                }
                appendForGraph();
        }
    });
}


function appendForGraph(){
    console.log(append_cur_temp);
    console.log(append_cur_hum);
    console.log(append_ave_temp);
    console.log(append_ave_hum);
    console.log(append_high_temp);
    console.log(append_high_hum);
    console.log(append_low_temp);
    console.log(append_low_hum);
    console.log(append_sent_time);

    graph_temperature();
    graph_humidity();
}

function displayData(){
    document.getElementById("current_temp").innerHTML = parseFloat(cur_temp).toFixed(2)+"°";
    document.getElementById("current_humid").innerHTML = parseFloat(cur_hum).toFixed(2)+"%";
    document.getElementById("Avg_Temp").innerHTML = parseFloat(ave_temp).toFixed(2)+"°";
    document.getElementById("Avg_Humid").innerHTML = parseFloat(ave_hum).toFixed(2)+"%";
    document.getElementById("High_Temp").innerHTML = parseFloat(high_temp).toFixed(2)+"°";
    document.getElementById("High_Humid").innerHTML = parseFloat(high_hum).toFixed(2)+"%";
    document.getElementById("Low_Temp").innerHTML = parseFloat(low_temp).toFixed(2)+"%";
    document.getElementById("Low_Humid").innerHTML = parseFloat(low_hum).toFixed(2)+"%";
}

function timeConverter(UNIX_timestamp){
    var a = new Date(UNIX_timestamp * 1);
    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    var year = a.getFullYear();
    var month = months[a.getMonth()];
    var date = a.getDate();
    var hour = a.getHours();
    var min = a.getMinutes();
    var sec = a.getSeconds();
    var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
    return time;
}

function convert(degree) {
    try {
        var x;
        console.log(degree);
        if (degree == "C") {
            document.getElementById("current_temp").innerHTML = parseFloat(cur_temp).toFixed(2)+"°";
            document.getElementById("Avg_Temp").innerHTML = parseFloat(ave_temp).toFixed(2)+"°";
            document.getElementById("High_Temp").innerHTML = parseFloat(high_temp).toFixed(2)+"°";
            document.getElementById("Low_Temp").innerHTML = parseFloat(low_temp).toFixed(2)+"%";
        } else {
            x = (cur_temp) * 9 / 5 + 32;
            x1 = (ave_temp) * 9 / 5 + 32;
            x2 = (high_temp) * 9 / 5 + 32;
            x3 = (low_temp) * 9 / 5 + 32;
            document.getElementById("current_temp").innerHTML = x.toFixed(2)+"°";
            document.getElementById("Avg_Temp").innerHTML = x1.toFixed(2)+"°";
            document.getElementById("High_Temp").innerHTML = x2.toFixed(2)+"°";
            document.getElementById("Low_Temp").innerHTML = x3.toFixed(2)+"°";
        }
    } catch (e) {
        if (e instanceof ReferenceError) {
            alert("Error! You need to connect to AWS first!");
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

 function graph_temperature(){
    var temperatureCanvas = document.getElementById("tempChart");

    Chart.defaults.global.defaultFontFamily = "Lato";
    Chart.defaults.global.defaultFontSize = 18;

    var cur_temp_data = {
        label: "Current-Temperature",
        data: append_cur_temp,
        fill: false,
        backgroundColor: 'transparent',
        borderColor: 'red'
    };

    var high_temp_data = {
        label: "Highest-Temperature",
        data: append_high_temp,
        fill: false,
        backgroundColor: 'transparent',
        borderColor: 'blue'
    };

    var low_temp_data = {
        label: "Lowest-Temperature",
        data: append_low_temp,
        fill: false,
        backgroundColor: 'transparent',
        borderColor: 'green'
    };

    var avg_temp_data = {
        label: "Average-Temperature",
        data: append_ave_temp,
        fill: false,
        backgroundColor: 'transparent',
        borderColor: 'purple'
    };

    var temperatureData = {
        labels: append_sent_time,
        datasets: [cur_temp_data, high_temp_data, low_temp_data, avg_temp_data]
    };

    var chartOptions = {
        legend: {
            display: true,
            position: 'top',
            labels: {
                boxWidth: 80,
                fontColor: 'black'
            }
        }
    };

    var lineChart = new Chart(temperatureCanvas, {
        type: 'line',
        data: temperatureData,
        options: chartOptions
    });
}



function graph_humidity(){
    var humidityCanvas = document.getElementById("humidChart");

    Chart.defaults.global.defaultFontFamily = "Lato";
    Chart.defaults.global.defaultFontSize = 18;

    var cur_hum_data = {
        label: "Current-Humidity",
        data: append_cur_hum,
        fill: false,
        backgroundColor: 'transparent',
        borderColor: 'red'
    };

    var high_hum_data = {
        label: "Highest-Humidity",
        data: append_high_hum,
        fill: false,
        backgroundColor: 'transparent',
        borderColor: 'blue'
    };

    var low_hum_data = {
        label: "Lowest-Humidity",
        data: append_low_hum,
        fill: false,
        backgroundColor: 'transparent',
        borderColor: 'green'
    };

    var avg_hum_data = {
        label: "Average-Humidity",
        data: append_ave_hum,
        fill: false,
        backgroundColor: 'transparent',
        borderColor: 'purple'
    };

    var humidityData = {
        labels: append_sent_time,
        datasets: [cur_hum_data, high_hum_data, low_hum_data, avg_hum_data]
    };

    var chartOptions = {
        legend: {
            display: true,
            position: 'top',
            labels: {
                boxWidth: 80,
                fontColor: 'black'
            }
        }
    };

    var lineChart = new Chart(humidityCanvas, {
        type: 'line',
        data: humidityData,
        options: chartOptions
    });
}
//append_protocol_message = '22,23,24,25,26';
function WebSocketTest(){
    appendForCalculate_timeSent = [];
    appendForCalculate_timeReceived = [];
    appendForCalculate_numberSent = [];
    appendForCalculate_numberReceived = [];

    if ("WebSocket" in window){
        //alert("WebSocket is supported by your Browser!");
        ws = new WebSocket("ws://10.0.0.24:8888/ws");

        ws.onopen = function(){
            for(i = 0; i <3; i++){
                ws.send(append_protocol_message); //send all the messages
                appendForCalculate_numberSent.push(append_protocol_message.length);
                start = performance.now();
                appendForCalculate_timeSent.push(start);
                console.log(append_protocol_message.length);
            }
            console.log(appendForCalculate_numberSent);
            console.log(Calculation(appendForCalculate_numberSent));

            document.getElementById("webSent").innerHTML = "# messages sent: "+Calculation(appendForCalculate_numberSent);
            numberDataSent_data[2] = Calculation(appendForCalculate_numberSent);
        };

        ws.onmessage = function (evt){
            var received_msg = evt.data;
            appendForCalculate_numberReceived.push(received_msg.split(',').length);

            end = performance.now();
            appendForCalculate_timeReceived.push(end);

            var x = appendForCalculate_timeReceived.map(function(item, index) {
                return item - appendForCalculate_timeSent[index];
            })
                console.log("time"+appendForCalculate_timeReceived);
                console.log("time"+appendForCalculate_timeSent);

            document.getElementById("webTime").innerHTML = "roundtrip time: "+Calculation(x).toFixed(2)+"ms";
            timeData_data[2] = Calculation(x).toFixed(2);

            document.getElementById("webReceived").innerHTML = "# messages received: "+Calculation(appendForCalculate_numberReceived);
            numberDataReceived_data[2] = Calculation(appendForCalculate_numberReceived);
        };

        ws.onclose = function(){
            // websocket is closed.
            //alert("Connection is closed...");
        };

        ws.onerror = function(){
            alert("There is something wrong...");
        };

    }else{
        // The browser doesn't support WebSocket
        alert("WebSocket NOT supported by your Browser!");
    }
}


function Calculation(array){
    var total = 0;
    for(var j = 0; j < array.length; j++) {
        total += array[j];
    }
    avg = total / array.length;
    return avg;
}

function ProtocolTest(){
    document.getElementById('img').style.visibility='visible';
    WebSocketTest();
    msg = append_protocol_message.join();
    document.getElementById("amqpSent").innerHTML = "# messages sent: "+append_protocol_message.length;
    document.getElementById("mqttSent").innerHTML = "# messages sent: "+append_protocol_message.length;
    document.getElementById("coapSent").innerHTML = "# messages sent: "+append_protocol_message.length;
    numberDataSent_data[3] = append_protocol_message.length;
    numberDataSent_data[0] = append_protocol_message.length;
    numberDataSent_data[1] = append_protocol_message.length;
    jQuery.ajax({
        url     : '/amqp',  
        type    : 'POST',
        data    : {
          msg
        },
        success : function(data){
            response = JSON.parse(data);
            //alert(data);
            mqtttime = response[0];
            mqttreceived = response[1];
            amqptime = response[2];
            amqpreceived = response[3];
            coaptime = response[4]

            document.getElementById("mqttReceived").innerHTML = "# messages received: "+mqttreceived;
            document.getElementById("mqttTime").innerHTML = "roundtrip time: "+mqtttime.toFixed(2)+"ms";
            document.getElementById("coapReceived").innerHTML = "# messages received: "+mqttreceived;
            document.getElementById("coapTime").innerHTML = "roundtrip time: "+coaptime.toFixed(2)+"ms";
            document.getElementById("amqpReceived").innerHTML = "# messages received: "+amqpreceived;
            document.getElementById("amqpTime").innerHTML = "roundtrip time: "+amqptime.toFixed(2)+"ms";

            numberDataReceived_data[0] =mqttreceived;
            timeData_data[0] = mqtttime.toFixed(2);
            numberDataReceived_data[3] =amqpreceived;
            timeData_data[3] = amqptime.toFixed(2);
            numberDataReceived_data[1] =mqttreceived;
            timeData_data[1] = coaptime.toFixed(2);
            document.getElementById('img').style.visibility='hidden';
            graph_protocol();
        }
    });
}

function graph_protocol(){
    var densityCanvas = document.getElementById("protocolChart");

    Chart.defaults.global.defaultFontFamily = "Lato";
    Chart.defaults.global.defaultFontSize = 18;

    var numberDataSent = {
        label: '# of messages sent',
        //data: [10, 10, 10, 10],
        data: numberDataSent_data,
        backgroundColor: 'rgba(0, 99, 132, 0.6)',
        borderWidth: 0,
        yAxisID: "y-axis-sent"
    };

    var numberDataReceived = {
        label: '# of messages received',
        //data: [10, 10, 10, 10],
        data: numberDataReceived_data,
        backgroundColor: 'rgba(99, 0, 132, 0.6)',
        borderWidth: 0,
        yAxisID: "y-axis-receive"
    };

    var timeData = {
        label: 'roundtrip time (milliseconds)',
        //data: [1.5, 1.3, 1.9, 1.6],
        data: timeData_data,
        backgroundColor: 'rgba(99, 132, 0, 0.6)',
        borderWidth: 0,
        yAxisID: "y-axis-time"
    };

    var planetData = {
        labels: ["MQTT", "CoAP", "WebSockets", "AMQP"],
        datasets: [numberDataSent, numberDataReceived, timeData]
    };

    var chartOptions = {
        scales: {
            xAxes: [{
                barPercentage: 1,
                categoryPercentage: 0.6
            }],
            yAxes: [{
                id: "y-axis-sent",
                ticks: {
                    beginAtZero: true,
                    min: 0
                }
            }, {
                id: "y-axis-receive",
                ticks: {
                    beginAtZero: true,
                    min: 0
                }
            }, {
                id: "y-axis-time",
                ticks: {
                    beginAtZero: true,
                    min: 0
                }
            }]
        }
    };

    var barChart = new Chart(densityCanvas, {
        type: 'bar',
        data: planetData,
        options: chartOptions
    });
}


window.onload = function () {
    var labeldata = [];
    var chrtdata = [];
    var ctx = document.getElementById("tempChart").getContext("2d");
    var tempChart = new Chart(ctx, {
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
    var ctx = document.getElementById("humidChart").getContext("2d");
    var tempChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labeldata,
            datasets: [{
                label: 'Humidity',
                data: chrtdata,
            }]
        }
    });
    var densityCanvas = document.getElementById("protocolChart");
    var barChart = new Chart(densityCanvas, {
        type: 'bar',
        data: {
            labels: labeldata,
            datasets: [{
                label: 'Protocol',
                data: chrtdata,
            }]
        }
    });
}





