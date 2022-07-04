(function ($) {
  "use strict";

  var $accountDelete = $("#delete-account"), //boton para abrir
    $accountDeleteDialog = $("#confirm-delete"), //ventana
    $distancebutton = $("#distance-button"),
    $distanceemergent = $("#distance-emergent"),
    $speedbutton = $("#speed-button"),
    $speedemergent = $("#speed-emergent"),
    $humeditybutton = $("#humedity-button"),
    $humedityemergent = $("#humedity-emergent"),
    $soundbutton = $("#sound-button"),
    $soundemergent = $("#sound-emergent"),
    $powerbutton = $("#power-button"),
    $poweremergent = $("#power-emergent");

  $accountDelete.on("click", function () {
    $accountDeleteDialog[0].showModal();
  });

  $distancebutton.on("click", function () {
    $distanceemergent[0].showModal();
  });

  $speedbutton.on("click", function () {
    $speedemergent[0].showModal();
  });

  $humeditybutton.on("click", function () {
    $humedityemergent[0].showModal();
  });

  $soundbutton.on("click", function () {
    $soundemergent[0].showModal();
  });

  $powerbutton.on("click", function () {
    $poweremergent[0].showModal();
  });

  $("#cancel").on("click", function () { //boton cancelar
    $accountDeleteDialog[0].close();
  });

  $("#cancel1").on("click", function () { //boton cancelar
    $distanceemergent[0].close();
  });

  $("#cancel2").on("click", function () { //boton cancelar
    $humedityemergent[0].close();
  });

  $("#cancel3").on("click", function () { //boton cancelar
    $speedemergent[0].close();
  });

  $("#cancel4").on("click", function () { //boton cancelar
    $soundemergent[0].close();
  });

  $("#cancel5").on("click", function () { //boton cancelar
    $poweremergent[0].close();
  });

})(jQuery);
