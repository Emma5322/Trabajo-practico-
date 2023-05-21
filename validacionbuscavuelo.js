document.getElementById("segundo").style.display = "none";
document.getElementById("labelsalida").style.display = "none";
document.getElementById("inputsalida").style.display = "none";

function idaVuelta() {
    document.getElementById("labelvuelta").style.display = "flex";
    document.getElementById("inputvuelta").style.display = "flex";
    document.getElementById("segundo").style.display = "none";
    document.getElementById("inputvuelta").disabled = false;
    document.getElementById("dividayvuelta").style.display = "flex";
    document.getElementById("labelsalida").style.display = "none";
    document.getElementById("inputsalida").style.display = "none";
}

function soloIda() {

    document.getElementById("inputvuelta").disabled = true;
    document.getElementById("segundo").style.display = "none";
    document.getElementById("labelsalida").style.display = "none";
    document.getElementById("inputsalida").style.display = "none";
    document.getElementById("dividayvuelta").style.display = "flex";
}

function multipleDestinos() {
    document.getElementById("labelsalida").style.display = "flex";
    document.getElementById("inputsalida").style.display = "flex";
    document.getElementById("segundo").style.display = "flex";
    document.getElementById("dividayvuelta").style.display = "none";
}

function validarBusquedaVuelo() {
    var origen1 = document.getElementById("origen").value;
    var destino1 = document.getElementById("destino").value;
    var origen2 = document.getElementById("origen2").value;
    var destino2 = document.getElementById("destino2").value;
    var salida1 = document.getElementById("inputsalida").value;
    var salida2 = document.getElementById("inputsalida2").value;
    var ida = document.getElementById("inputida").value;
    var vuelta = document.getElementById("inputvuelta").value;
    var adultos = document.getElementById("adultos").value;
    var bebes = document.getElementById("bebes").value;

    if (document.buscarvuelo.seleccion[0].checked) {
        if (origen1 === "" || destino1 === "" || ida === "" || vuelta === "") {
            alert("Por favor, complete todos los campos del formulario1.");
            return false;
        }
        if (origen1 === destino1) {
            alert("El origen y el destino no pueden ser los mismos");
            return false;
        }

        if (ida === vuelta) {
            alert("Las fechas de ida y de vuelta no pueden ser las mismas");
            return false;
        }

        if (bebes > adultos) { 
        alert("El número de bebés no puede ser mayor al de adultos");
        return false;
    }
}

if (document.buscarvuelo.seleccion[1].checked) {
    if (origen1 === "" || destino1 === "" || ida === "") {
        alert("Por favor, complete todos los campos del formulario2.");
        return false;
    }

    if (origen1 === destino1) {
        alert("El origen y el destino no pueden ser los mismos");
        return false;
    }

    if (bebes > adultos) { 
        alert("El número de bebés no puede ser mayor al de adultos");
        return false;
}
}

if (document.buscarvuelo.seleccion[2].checked) {
    if (origen1 === "" || destino1 === "" || origen2 === "" || destino2 === "" || salida1 === "" || salida2 === "") {
        alert("Por favor, complete todos los campos del formulario3.");
        return false;
    }

    if (origen1 === destino1) {
        alert("El origen y el destino no pueden ser los mismos");
        return false;
    }
    if (origen2 === destino2) {
        alert("El origen y el destino no pueden ser los mismos");
        return false;
    }

    if (salida1 === salida2) {
        alert("Las fechas de salida de ambos tramos deben ser distintas");
        return false;
    }
    if (bebes > adultos) { 
        console.log(bebes);
        console.log(adultos);
        alert("El número de bebés no puede ser mayor al de adultos");
        
        return false;
}


    
}
alert("Formulario enviado correctamente.");
return true;


}


