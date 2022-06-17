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
            }
        },
        messages : {
            name: {
            minlength: "El nombre debe tener al menos 3 letras"
            },
            age: {
            required: "Por favor ingrese su edad",
            number: "Por favor ingrese su edad usando números",
            min: "Ud debe tener al menos 18 años"
            },
            email: {
            email: "El email debe tener el sgte formato: abc@domain.tld"
            }
        }
    });
});