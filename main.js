console.log("Hola")

function voltearCarta(elemento) {
    elemento.style.display = "none";
    console.log(elemento)
    elemento.nextSibling.nextElementSibling.style.display = "block"
}