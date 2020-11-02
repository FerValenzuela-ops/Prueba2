/* Esta funcion permite hacer un contador responsivo de caracteres en el text area de unete */ 
function count_down(obj) {
    var element = document.getElementById('count2');

    element.innerHTML = 140 - obj.value.length;

    if (140 - obj.value.length < 0) {
        element.style.color = 'red';

    } else {
        element.style.color = 'grey';
    }
}