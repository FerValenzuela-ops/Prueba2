/* Esta funcion nos permite verificar los datos y validar que el registro del usuario sea ejecutado correctamente  */
var llenado = false;
function validarRegistro(){
  var nombre = document.getElementById("nombre").value;
  var apellido = document.getElementById("apellido").value;
  var telefono = document.getElementById("telefono").value;
  var email = document.getElementById("email").value;
  var message = document.getElementById("message").value;
  var pass = document.getElementById("pass").value;
  var passconfirm = document.getElementById("passconfirm").value;
  var error_message = document.getElementById("error_message");
  
  error_message.style.padding = "10px";
  
  var text;
  if(nombre.length < 3){
    text = "Ingrese mas de 3 caracteres en su nombre";
    error_message.innerHTML = text;
    return false;
  }
  if(apellido.length < 3){
    text = "Ingrese mas de 3 caracteres en su apellido";
    error_message.innerHTML = text;
    return false;
  }
  if(isNaN(telefono) || telefono.length != 8){
    text = "Ingrese su numero de telefono";
    error_message.innerHTML = text;
    return false;
  }
  if(email.indexOf("@") == -1 || email.length < 6){
    text = "Por favor ingresa un email valido";
    error_message.innerHTML = text;
    return false;
  }
  if(message.length <= 140){
    text = "Por favor ingresa minimo 140 Characters";
    error_message.innerHTML = text;
    return false;
  }


  if (pass != passconfirm) {
    text = "Las contraseñas deben coincidir"
    error_message.innerHTML = text;
    return false;
  }
  
  if (pass.length < 5) {
    text = "La contraseña debe tener minimo 5 caracteres"
    error_message.innerHTML = text;
    return false;
  }
  alert("Registro exitoso!");
  return true;
}



/*
nombre apellido email telefono user pass passconfirm region message

*/ 