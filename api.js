
    for (var i = 1; i < 3; i++){
    
    fetch('https://randomuser.me/api/') // API a leer
        // Cuando ha finalizado la lectura
        // guardo en datos el texto leido:
        .then(datos => datos.json()) //res va a guardar el dato mediante el método .json()
        .then(datos => {
            // Y luego copio ese texto en #contenido.
            opiniones.innerHTML +=
                `<div class="tarjeta">
                 <img src = "${datos.results[0].picture.large}"</img><br>
                 <div>
                 <h1>Es genial!!</h1><br>
                 <i><p>"Gracias al Club Auri pude ahorrar en mi viaje familiar"</p></i><br>
                 ${datos.results[0].name.last}, ${datos.results[0].name.first} 
                 </div>           
                 </div>`
                 
        })

    }