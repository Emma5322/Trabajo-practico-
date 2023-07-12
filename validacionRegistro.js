function validarFormulario() {
    // Obtener los valores ingresados por el usuario y recortar
    // los posibles espacios en blanco al principio y al final.
    var nombres = document.getElementById("nombres").value.trim();
    var dni = document.getElementById("dni").value.trim();
    var apellidos = document.getElementById("apellidos").value.trim();
    var mail = document.getElementById("mail").value.trim();
    var validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

    // Verificar si algún campo está en blanco
    if (dni === "" || nombres === "" || apellidos === "" || mail === "") {
      alert("Por favor, complete todos los campos del formulario.");
      return false;
    }

    // Verificar si el nombre contiene solo caracteres alfabéticos y espacios
    for (var i = 0; i < nombres.length; i++) {
      var charCode = nombres.charCodeAt(i);
      if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32)) {
        alert("El campo 'nombre' solo puede contener caracteres alfabéticos y espacios.");
        return false;
      }
    }

    for (var i = 0; i < apellidos.length; i++) {
      var charCode = apellidos.charCodeAt(i);
      if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32)) {
        alert("El campo 'apellidos' solo puede contener caracteres alfabéticos y espacios.");
        return false;
      }
    }

    // Verificar si el DNI contiene solo 8 dígitos numéricos
    if (dni.length !== 8) {
      alert("El campo 'dni' debe contener exactamente 8 dígitos numéricos.");
      return false;
    }
    for (var j = 0; j < dni.length; j++) {
      var digit = dni.charAt(j);
      if (digit < "0" || digit > "9") {
        alert("El campo 'dni' solo puede contener dígitos numéricos.");
        return false;
      }
    }

    if( validEmail.test(mail) ){
   
  }else{
      alert('En el campo "email" complete un email válido');
      return false;
  }


    // Si todas las validaciones son exitosas, enviar el formulario
    alert("Registro realizado con éxito. Verifique su casilla de email para validar la cuenta");
    return true;
  }
