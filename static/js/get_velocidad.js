function getVelocidad() {
    // Establece la ruta del archivo JSON
    var firebase = "https://iotplatform-11dca-default-rtdb.firebaseio.com/users/";
        var json = "/data_widget/sensor/velocidad.json";
        var cookies = document.cookie.split(';').map(cookie => cookie.split('=')).reduce((accumulator, [key, value]) => ({...accumulator, [key.trim()]: decodeURIComponent(value) }), {});
        var id = cookies.localId;
        var sensores = new EventSource(firebase+id+json);
        sensores.addEventListener('put', function (e) {
            var json = JSON.parse(e.data);
            console.log(json);
            if (json.path == "/") {
                tbody = document.getElementById("tbody_velocidad");
                for (var key in json.data) {
                    var tr = document.createElement("tr");
                    var td_sensor = document.createElement("td");
                    var td_veloc = document.createElement("td");
                    var input_veloc = document.createElement("input");
                    var td_ruta = document.createElement("td");
                    var td_button = document.createElement("td");

                    input_veloc.type = "number";
                    input_veloc.id = key;
                    input_veloc.readOnly = true;
                    input_veloc.disabled = true;
                    td_sensor.innerHTML = json.data[key].name;
                    td_ruta.innerHTML = "/"+key+"/velocidad";
                    td_button.innerHTML = '<button class="btn btn-danger" id="velocidad/'+key+'" type="button" onclick="reply_click(this.id)">Borrar</button>';

                    td_veloc.appendChild(input_veloc);
                    tr.appendChild(td_sensor);
                    tr.appendChild(td_veloc);
                    tr.appendChild(td_ruta);
                    tr.appendChild(td_button);
                    tbody.appendChild(tr);

                    document.getElementById(key).value = json.data[key].velocidad;
                }
            } else {
                s = json.path.split("/");
                console.log(s[1]);
                console.log(json.data);
                document.getElementById(s[1]).value = json.data;
            }
        });
};