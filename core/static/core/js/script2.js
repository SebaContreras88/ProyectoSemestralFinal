$(document).ready(function () {

    $("#error_1").hide()

    $("#text1").blur(function () {
        console.log("text1 perdió el foco")

        
        if ($("#text1").val().length < 15) { 
            $("#error_1").fadeOut()
            event.preventDefault()
        }

    });

    $("#text1").focus(function () {
        console.log("text1 ganó el foco")
        $("#error_1").html("ingrese nombre mayor a 3 caracteres")
        $("#error_1").fadeIn()
    });

    $("#error_2").hide()

    $("#text2").blur(function () {
        console.log("text2 perdió el foco")

        
        if ($("#text2").val().length < 20) { 
            $("#error_2").fadeOut()
            event.preventDefault()
        }

    });

    $("#text2").focus(function () {
        console.log("text2 ganó el foco")
        $("#error_2").html("Ingrese Apellido mayor a 4 caracteres")
        $("#error_2").fadeIn()
    });

    $("#error_3").hide()

    $("#text3").blur(function () {
        console.log("text3 perdió el foco")

        
        if ($("#text3").val().length < 35) { 
            $("#error_3").fadeOut()
            event.preventDefault()
        }

    });

    $("#text3").focus(function () {
        console.log("text3 ganó el foco")
        $("#error_3").html("Ingrese Correo Electronico con '@' y '.'")
        $("#error_3").fadeIn()
    });

    $("#error_4").hide()

    $("#text4").blur(function () {
        console.log("text4 perdió el foco")

        
        if ($("#text4").val().length < 35) { 
            $("#error_4").fadeOut()
            event.preventDefault()
        }

    });

    $("#text4").focus(function () {
        console.log("text4 ganó el foco")
        $("#error_4").html("Ingrese contraseña mayor a 9 caracteres")
        $("#error_4").fadeIn()
    });






    //Validaciones//
    $('#btn2').click(function(){
        if($("#text3").val().indexOf('@', 7) == -1 || $("#text3").val().indexOf('.', 0) == -1) {
            $("#error_3").html("Debe introducir un correo o el correo introducido no es correcto");
            $("#error_3").fadeIn()
            event.preventDefault()            
        }
        if($("#text1").val().length < 3) { 
            $("#error_1").html("Debe introducir un nombre valido");
            $("#error_1").fadeIn()
            event.preventDefault()
            
        }
        if($("#text2").val().length < 4) { 
            $("#error_2").html("Debe introducir un Apellido valido");
            $("#error_2").fadeIn()
            event.preventDefault()
            
        }
        if($("#text4").val().length < 9) { 
            $("#error_4").html("Debe introducir una Contraseña valida");
            $("#error_4").fadeIn()
            event.preventDefault()
        }
        else{
            alert("¡Te haz registrado con éxito!");
            }
        });
});
