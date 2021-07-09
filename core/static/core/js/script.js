$(document).ready(function () {
    
    $('#btn1').click(function(){
        if($("#txt1").val().indexOf('@', 7) == -1 || $("#txt1").val().indexOf('.', 0) == -1) {
            $("#error1").html("Debe introducir correo Electronico o el correo Electronico introducido no es correcto");
            $("#error1").fadeIn()
            event.preventDefault()
            
        }
        if($("#txt2").val().length < 9) { 
            $("#error2").html("Debe introducir una Contraseña valida");
            $("#error2").fadeIn()
            event.preventDefault()
        }
        else {
            alert("¡Haz iniciado sesión con éxito!");
            }
    });
});
