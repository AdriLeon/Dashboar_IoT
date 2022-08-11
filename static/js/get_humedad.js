function getHumedad() {
    // Establece la ruta del archivo JSON
    var firebase = "https://iotplatform-11dca-default-rtdb.firebaseio.com/users/";
        var json = "/data_widget/sensor/humedad/humedad.json";
        var cookies = document.cookie.split(';').map(cookie => cookie.split('=')).reduce((accumulator, [key, value]) => ({...accumulator, [key.trim()]: decodeURIComponent(value) }), {});
        var id = cookies.localId;
        var sensores = new EventSource(firebase+id+json);
        sensores.addEventListener('put', function (e) {
            var json = JSON.parse(e.data);
            console.log(json);
            if (json.path == "/") {
                tbody = document.getElementById("tbody_humedad");
                for (var key in json.data) {
                    var tr = document.createElement("tr");
                    var td_sensor = document.createElement("td");
                    var td_hum = document.createElement("td");
                    var input_hum = document.createElement("input");
                    var td_ruta = document.createElement("td");
                    var td_button = document.createElement("td");
                    
                    input_hum.type = "number";
                    input_hum.id = key;
                    input_hum.readOnly = true;
                    input_hum.disabled = true;
                    td_ruta.innerHTML = "/"+key+"/humedad";
                    td_sensor.innerHTML = json.data[key].name;
                    td_button.innerHTML = '<button class="btn btn-danger" id="sensor/humedad/humedad/'+key+'" type="button" onclick="reply_click(this.id)">Borrar</button>';

                    td_hum.appendChild(input_hum);
                    tr.appendChild(td_sensor);
                    tr.appendChild(td_hum);
                    tr.appendChild(td_ruta);
                    tr.appendChild(td_button);
                    tbody.appendChild(tr);

                    // console.log(json.data[key].temperatura);
                    document.getElementById(key).value = json.data[key].humedad;
                }
            } else {
                s = json.path.split("/");
                console.log(s[1]);
                console.log(json.data);
                document.getElementById(s[1]).value = json.data;
            }
        });
};