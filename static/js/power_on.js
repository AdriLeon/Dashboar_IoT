function click_reply(id) {
    var sensor = id;
    var firebase = "https://iotplatform-11dca-default-rtdb.firebaseio.com/users/";
    var json = "/data_widget/controlador/power/";
    var end = ".json";
    var cookies = document.cookie.split(';').map(cookie => cookie.split('=')).reduce((accumulator, [key, value]) => ({...accumulator, [key.trim()]: decodeURIComponent(value) }), {});
    var id = cookies.localId;
    var url = firebase+id+json+sensor+end;

    const toSend = {
        "name": "prueba1",
        "power": "Encendido",
        "value": 1
      }
    const jsonString = JSON.stringify(toSend);

    const request = new XMLHttpRequest();
    

    request.onload = function () {
      const data = JSON.parse(this.responseText);
      const text = this.responseText;
      console.log(text);
      console.log(data);
      location.reload();
    }

    request.open("PUT", url);
    request.send(jsonString);
  };