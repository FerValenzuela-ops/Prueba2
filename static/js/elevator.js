/* Funcion que nos lleva al principio de la pagina en la que nos encontramos */
window.onload = function parriba() {
  var elevador = new Elevator({
    element: document.querySelector("#parriba")
  });
};

$("#parrriba").click(function arriba (){
  $("html,body").animate({scroollTop:0}, 500);
  return false;
});

