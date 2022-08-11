function replyclick(clicked_id) {
    var sensor = clicked_id;
    var firebase = "https://iotplatform-11dca-default-rtdb.firebaseio.com/users/";
    var json = "/data_widget/";
    var end = ".json";
    var cookies = document.cookie.split(';').map(cookie => cookie.split('=')).reduce((accumulator, [key, value]) => ({...accumulator, [key.trim()]: decodeURIComponent(value) }), {});
    var id = cookies.localId;
    var url = firebase+id+json+sensor+end;

    const request = new XMLHttpRequest();
    

    request.onload = function () {
      const data = JSON.parse(this.responseText);
      const text = this.responseText;
      console.log(text);
      console.log(data);
      
    }

    request.open("DELETE", url);
    request.send();
  };