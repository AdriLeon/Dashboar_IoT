function getControlador() {
    // Establece la ruta del archivo JSON
    var firebase = "https://iotplatform-11dca-default-rtdb.firebaseio.com/users/";
        var json = "/data_widget/controlador/power.json";
        var cookies = document.cookie.split(';').map(cookie => cookie.split('=')).reduce((accumulator, [key, value]) => ({...accumulator, [key.trim()]: decodeURIComponent(value) }), {});
        var id = cookies.localId;
        var sensores = new EventSource(firebase+id+json);
        sensores.addEventListener('put', function (e) {
            var json = JSON.parse(e.data);
            console.log(json);
            if (json.path == "/") {
                tbody = document.getElementById("tbody_controlador");
                for (var key in json.data) {
                    var tr = document.createElement("tr");
                    var td_controller = document.createElement("td");
                    var td_power = document.createElement("td");
                    var input_power = document.createElement("input");
                    var td_ruta = document.createElement("td");
                    var td_power_on = document.createElement("td");
                    var td_power_off = document.createElement("td");
                    var td_button = document.createElement("td");

                    input_power.type = "text";
                    input_power.id = key;
                    input_power.readOnly = true;
                    input_power.disabled = true;
                    td_controller.innerHTML = json.data[key].name;
                    td_ruta.innerHTML = "/"+key+"/value";
                    td_power_on.innerHTML = '<button class="btn btn-success" id="'+key+'" type="button" onclick="click_reply(this.id)">Encender</button>';
                    td_power_off.innerHTML = '<button class="btn btn-warning" id="'+key+'" type="button" onclick="clickreply(this.id)">Apagar</button>';
                    td_button.innerHTML = '<button class="btn btn-danger" id="controlador/power/'+key+'" type="button" onclick="replyclick(this.id)">Borrar</button>';

                    td_power.appendChild(input_power);
                    tr.appendChild(td_controller);
                    tr.appendChild(td_power);
                    tr.appendChild(td_ruta);
                    tr.appendChild(td_power_on);
                    tr.appendChild(td_power_off);
                    tr.appendChild(td_button);
                    tbody.appendChild(tr);

                    document.getElementById(key).value = json.data[key].power;
                }
            } else {
                s = json.path.split("/");
                console.log(s[1]);
                console.log(json.data);
                document.getElementById(s[1]).value = json.data;
            }
        });
};