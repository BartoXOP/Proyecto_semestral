$(document).ready(function() {
    $("#basic-form").validate({
        rules: {
            name : {
            required: true,
            minlength: 3
            },
            age: {
            required: true,
            number: true,
            min: 18
            },
            email: {
            required: true,
            email: true
            },
            pass:{
                required: true,
                minlength:8
            },
            pass2:{
                required: true,
                minlength: 8
            }
        },
        messages : {
            name: {
                required:"Ingresa un nombre",
            minlength: "El nombre debe tener al menos 3 letras"
            },
            age: {
            required: "Por favor ingrese su edad",
            number: "Por favor ingrese su edad usando números",
            min: "Ud debe tener al menos 18 años"
            },
            email: {
                required:"Ingresa un email",
            email: "El email debe tener el sgte formato: abc@domain.tld"
            },
            pass:{
                required:"Ingresa contraseña",
                minlength:"La contraseña debe ser de minimo 8 caracteres"
            },
            pass2:{
                required:"Ingresa contraseña",
                minlength:"La contraseña debe ser de minimo 8 caracteres"
            }
        }
    });
});