function validarFormulariorecupero() {
    var dni = document.getElementById("dni").value.trim();

    if (dni === "") {
        alert("Por favor, complete el campo vacío.");
        return false;
    }

    // Verificar si el DNI contiene solo 8 dígitos numéricos
    if (dni.length !== 8) {
        alert("El campo 'dni' debe contener exactamente 8 dígitos numéricos.");
        return false;

    }

    // Si todas las validaciones son exitosas, enviar el formulario
    alert("Enviamos un email a su casilla para recuperar la contraseña.");
    return true;
}