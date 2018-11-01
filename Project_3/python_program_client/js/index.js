

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

    var time = new Date().toLocaleString();
    document.getElementById("timestamp").innerHTML = "You are requesting AWS SQS data at "+time;

    AWS.config.update({

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

//                  var message = data.Messages[i]
//                  sqs.deleteMessage({
//                      QueueUrl : queueUrl,
//                      ReceiptHandle : message.ReceiptHandle
//                  }, function(err, data) {
//                      err && console.log(err);
//                      console.log(data+"has been deleted")
//                  });
                }appendForGraph();
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
    document.getElementById("current_temp").innerHTML = cur_temp+"°";
    document.getElementById("current_humid").innerHTML = cur_hum+"%";
    document.getElementById("Avg_Temp").innerHTML = ave_temp+"°";
    document.getElementById("Avg_Humid").innerHTML = ave_hum+"%";
    document.getElementById("High_Temp").innerHTML = high_temp+"°";
    document.getElementById("High_Humid").innerHTML = high_hum+"%";
    document.getElementById("Low_Temp").innerHTML = low_temp+"%";
    document.getElementById("Low_Humid").innerHTML = low_hum+"%";
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
            document.getElementById("current_temp").innerHTML = cur_temp+"°";
            document.getElementById("Avg_Temp").innerHTML = ave_temp+"°";
            document.getElementById("High_Temp").innerHTML = high_temp+"°";
            document.getElementById("Low_Temp").innerHTML = low_temp+"°";
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
}





