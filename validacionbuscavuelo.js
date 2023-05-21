document.getElementById("segundo").style.display = "none";
document.getElementById("labelsalida").style.display = "none";
document.getElementById("inputsalida").style.display = "none";

function idaVuelta(){
    document.getElementById("labelvuelta").style.display = "flex";
    document.getElementById("inputvuelta").style.display = "flex";
    document.getElementById("segundo").style.display = "none";
    document.getElementById("inputvuelta").disabled = false;
    document.getElementById("dividayvuelta").style.display = "flex";
    document.getElementById("labelsalida").style.display = "none";
    document.getElementById("inputsalida").style.display = "none";
}

function soloIda(){
    
    document.getElementById("inputvuelta").disabled = true;
    document.getElementById("segundo").style.display = "none";
    document.getElementById("labelsalida").style.display = "none";
    document.getElementById("inputsalida").style.display = "none";
    document.getElementById("dividayvuelta").style.display = "flex";
}

function multipleDestinos(){
    document.getElementById("labelsalida").style.display = "flex";
    document.getElementById("inputsalida").style.display = "flex";
    document.getElementById("segundo").style.display = "flex";
    document.getElementById("dividayvuelta").style.display = "none";
}

