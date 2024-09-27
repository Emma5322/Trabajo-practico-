
    for (var i = 1; i < 3; i++){
        if (i == 1)  {
    fetch('https://randomuser.me/api/') // API a leer
        // Cuando ha finalizado la lectura
        // guardo en datos el texto leido:

                
        .then(datos => datos.json()) //res va a guardar el dato mediante el método .json()
        .then(datos => {
            // Y luego copio ese texto en #opiniones.
            opiniones.innerHTML +=
                `<div class="tarjeta">
                 <img src = "${datos.results[0].picture.large}"</img>
                 <div>
                 <h1>Es genial!!</h1>
                 <i><p>"Gracias al Club Auri pude ahorrar en mi viaje familiar"</p></i>
                 ${datos.results[0].name.last}, ${datos.results[0].name.first} 
                 </div>           
                 </div>`
                 
        })
    }

    else {   
        
        fetch('https://randomuser.me/api/') // API a leer
        // Cuando ha finalizado la lectura
        // guardo en datos el texto leido:
          .then(datos => datos.json()) //res va a guardar el dato mediante el método .json()
    .then(datos => {
        // Y luego copio ese texto en #opiniones.
        opiniones.innerHTML +=
            `<div class="tarjeta">
             <img src = "${datos.results[0].picture.large}"</img>
             <div>
             <h1>Lo super recomiendo!!</h1>
             <i><p>"Todos los meses acumulo millas que me ayudan a mejorar mi viaje"</p></i>
             ${datos.results[0].name.last}, ${datos.results[0].name.first} 
             </div>           
             </div>`
             
    })
}
    }