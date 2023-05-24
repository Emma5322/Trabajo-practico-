function validarFormularioinicio() {
var usuario = document.getElementById("usuario").value.trim();
    var passw = document.getElementById("passw").value.trim();
    


    if (usuario === "" || passw === "") {
      alert("Por favor, complete todos los campos del formulario.");
      return false;
    }

    // Verificar si el usuario contiene solo caracteres alfabéticos y espacios
    for (var i = 0; i < usuario.length; i++) {
      var charCode = usuario.charCodeAt(i);
      if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32)) {
        alert("El campo 'usuario' solo puede contener caracteres alfabéticos.");
        return false;
      }
    }


    // Verificar si la contraseña contiene un mínimo de 6 caracteres
    if (passw.length < 6) {
      alert("El campo 'contraseña' debe contener al menos 6 caracteres.");
      return false;
    }
    

    // Si todas las validaciones son exitosas, enviar el formulario
    alert("Inicio de sesión correcto.");
    return true;
  }
