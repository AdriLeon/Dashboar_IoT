function getDistancia() {
    // Establece la ruta del archivo JSON
    var firebase = "https://iotplatform-11dca-default-rtdb.firebaseio.com/users/";
        var json = "/data_widget/sensor/distancia.json";
        var cookies = document.cookie.split(';').map(cookie => cookie.split('=')).reduce((accumulator, [key, value]) => ({...accumulator, [key.trim()]: decodeURIComponent(value) }), {});
        var id = cookies.localId;
        var sensores = new EventSource(firebase+id+json);
        sensores.addEventListener('put', function (e) {
            var json = JSON.parse(e.data);
            console.log(json);
            if (json.path == "/") {
                tbody = document.getElementById("tbody_distancia");
                for (var key in json.data) {
                    var tr = document.createElement("tr");
                    var td_sensor = document.createElement("td");
                    var td_dist = document.createElement("td");
                    var input_dist = document.createElement("input");
                    var td_ruta = document.createElement("td");
                    var td_button = document.createElement("td");
                    var dist = "dist"+key;

                    input_dist.type = "number";
                    input_dist.id = dist;
                    input_dist.readOnly = true;
                    input_dist.disabled = true;
                    td_sensor.innerHTML = json.data[key].name;
                    td_ruta.innerHTML = "/"+key+"/distancia";
                    td_button.innerHTML = '<button class="btn btn-danger" type="button">Borrar</button>';

                    td_dist.appendChild(input_dist);
                    tr.appendChild(td_sensor);
                    tr.appendChild(td_dist);
                    tr.appendChild(td_ruta);
                    tr.appendChild(td_button);
                    tbody.appendChild(tr);

                    document.getElementById(dist).value = json.data[key].distancia;
                }
            } else {
                s = json.path.split("/");
                console.log(s[1]);
                console.log(json.data);
                document.getElementById(s[1]).value = json.data;
            }
        });
};