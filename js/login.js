  function validateFormLogin() {
    var form = document.getElementById('form-login');
    var formData = new FormData(form);
    var passInput = document.getElementById('exampleInputPassword1');
    
    if (passInput < 8) {
      alert('La contraseña debe tener al menos mas de 8 caracteres');
      return false
    } else if (passInput > 16) {
      alert('La contraseña debe tener menos de 16 caracteres');
      return false
    } 
    
      fetch('../backend/login.php', {
        method: 'POST',
        body: formData
      })
      .then(response => response.text())
      .then(data => {
        if (data === 'Bienvenido') {
          alert(data);
          alert("Acceso correcto");
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