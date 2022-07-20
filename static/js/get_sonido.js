function getSonido() {
    // Establece la ruta del archivo JSON
    var firebase = "https://iotplatform-11dca-default-rtdb.firebaseio.com/users/";
        var json = "/data_widget/sensor/sonido.json";
        var cookies = document.cookie.split(';').map(cookie => cookie.split('=')).reduce((accumulator, [key, value]) => ({...accumulator, [key.trim()]: decodeURIComponent(value) }), {});
        var id = cookies.localId;
        var sensores = new EventSource(firebase+id+json);
        sensores.addEventListener('put', function (e) {
            var json = JSON.parse(e.data);
            console.log(json);
            if (json.path == "/") {
                tbody = document.getElementById("tbody_sonido");
                for (var key in json.data) {
                    var tr = document.createElement("tr");
                    var td_sensor = document.createElement("td");
                    var td_sonido = document.createElement("td");
                    var input_sonido = document.createElement("input");
                    var td_ruta = document.createElement("td");
                    var td_button = document.createElement("td");

                    input_sonido.type = "number";
                    input_sonido.id = key;
                    input_sonido.readOnly = true;
                    input_sonido.disabled = true;
                    td_sensor.innerHTML = json.data[key].name;
                    td_ruta.innerHTML = "/"+key+"/sonido";
                    td_button.innerHTML = '<button class="btn btn-danger" type="button">Borrar</button>';

                    td_sonido.appendChild(input_sonido);
                    tr.appendChild(td_sensor);
                    tr.appendChild(td_sonido);
                    tr.appendChild(td_ruta);
                    tr.appendChild(td_button);
                    tbody.appendChild(tr);

                    document.getElementById(key).value = json.data[key].sonido;
                }
            } else {
                s = json.path.split("/");
                console.log(s[1]);
                console.log(json.data);
                document.getElementById(s[1]).value = json.data;
            }
        });
};