let telefono = document.getElementById('telefono')

telefono.addEventListener('keypress', (event) => {
  event.preventDefault()
   console.log(event.keyCode)
  let valorTecla = String.fromCharCode(event.keyCode)
  console.log(valorTecla)
  let valorParsed = parseInt(valorTecla)
   console.log(valorParsed)
  if(valorParsed) {
    telefono.value = telefono.value + valorParsed
  }
})