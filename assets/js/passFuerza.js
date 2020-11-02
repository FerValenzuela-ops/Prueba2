/* Funcion javascript que permite verificar la fuerza de la contraseña en el registro */

const myPass = document.querySelector("#pass");

const myMsg = document.querySelector(".msg");

myPass.addEventListener('keydown', function () {

    if (myPass.value.length < 5) {
        myMsg.innerText = "Muy corta";
        myMsg.style.color = '#CCC';
    }
    else if (myPass.value.length < 10) {
        myMsg.innerText = "Facil de adivinar";
        myMsg.style.color = 'red';
        myPass.style.borderColor = '#4286F4';
    }
    else if (myPass.value.length < 12) {
        myMsg.innerText = "Un poco debil";
        myMsg.style.color = '#CCC';
    }
    else if (myPass.value.length < 14) {
        myMsg.innerText = "Podria ser mejor";
        myMsg.style.color = '#CCC';
    }
    else if (myPass.value.length < 16) {
        myMsg.innerText = "Nada mal";
        myMsg.style.color = 'green';
    }
    else if (myPass.value.length < 20) {
        myMsg.innerText = '🐭😍👌';
    }


    /* Reiniciar colores uwu*/
    if (myPass.value.length == 0) {
        myMsg.innerText = '';
        myPass.style.borderColor = 'red';
    }

})