/* Validaciones formulario de contacto*/
function validate(){
  var name = document.getElementById("name").value;
  var subject = document.getElementById("subject").value;
  var phone = document.getElementById("phone").value;
  var email = document.getElementById("email").value;
  var message = document.getElementById("message").value;
  var error_message = document.getElementById("error_message");
  
  error_message.style.padding = "10px";
  
  var text;
  if(name.length < 2){
    text = "Ingresa al menos 3 caracteres";
    error_message.innerHTML = text;
    return false;
  }
  if(subject.length < 10){
    text = "Ingresa al menos 11 caracteres";
    error_message.innerHTML = text;
    return false;
  }
  if(isNaN(phone) || phone.length != 10){
    text = "Ingresa 10 caracteres";
    error_message.innerHTML = text;
    return false;
  }
  if(email.indexOf("@") == -1 || email.length < 6){
    text = "Ingresa un mail valido";
    error_message.innerHTML = text;
    return false;
  }
  if(message.length <= 10){
    text = "Ingresa al menos 11 caracteres";
    error_message.innerHTML = text;
    return false;
  }
  alert("Enviado!");
  return true;
}