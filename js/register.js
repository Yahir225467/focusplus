function validateFormRegister() {
    var form = document.getElementById('form-register');
    var formData = new FormData(form);
    
    var nameInput = document.getElementById('nombre');
    var lastnameInput = document.getElementById('apellidos');
    var nameValue = nameInput.value.trim();
    var lastnameValue = lastnameInput.value.trim();
    var emailInput = document.getElementById('exampleInputEmail1');
    var passInput = document.getElementById('exampleInputPassword1');
    var regex = /^[A-Za-zñÑáÁéÉíÍóÓúÚ\s]+$/;
    
    if (!regex.test(nameValue)) {
      alert('Ingrese solo letras mayúsculas y minusculas en el nombre');
      nameInput.focus();
      return false
    } else if (!regex.test(lastnameValue)) {
        alert('Ingrese solo letras mayúsculas y minusculas en los apellidos');
        nameInput.focus();
        return false
    } else if (passInput < 8) {
        alert('La contraseña debe tener al menos mas de 8 caracteres');
        return false
      } else if (passInput > 16) {
        alert('La contraseña debe tener menos de 16 caracteres');
        return false
      } 
    
      fetch('../backend/register.php', {
        method: 'POST',
        body: formData
      })
      .then(response => response.text())
      .then(data => {
        if (data === 'Bienvenido') {
          alert(data);
          alert("Datos cargados correctamente");
          window.location.reload();
        } else {
          alert(data);
        }
      })
      .catch(error => {
        alert("Error; ", error);
      });
    
    return false
  }