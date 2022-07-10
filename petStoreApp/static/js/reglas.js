var Fn = {
    // Valida el rut con su cadena completa "XXXXXXXX-X"
    validaRut : function (txtRun) {
        txtRun = txtRun.replace("‐","-");
        if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( txtRun ))
            return false;
        var tmp     = txtRun.split('-');
        var digv    = tmp[1]; 
        var rut     = tmp[0];
        if ( digv == 'K' ) digv = 'k' ;
        
        return (Fn.dv(rut) == digv );
    },
    dv : function(T){
        var M=0,S=1;
        for(;T;T=Math.floor(T/10))
            S=(S+T%10*(9-M++%6))%11;
        return S?S-1:'k';
    }
};

// funcion validar solo letras al escribir
function validarLetras(e) { 
    tecla = (document.all) ? e.keyCode : e.which; 
    if (tecla == 8)
        return true; 
    patron = /[A-ZáÁéÉíÍóÓúÚñÑa-z\s]+$/i; 
    te = String.fromCharCode(tecla); 
    return patron.test(te);
}

// funcion validar solo numeros al escribir
function validarNumeros(e) { 
    tecla = (document.all) ? e.keyCode : e.which; 
    patron = /[^\d]+$/; 
    te = String.fromCharCode(tecla); 
    return !patron.test(te); 
}

// funcion validar formato rut al escribir
function validarRut(e) { 
    tecla = (document.all) ? e.keyCode : e.which; 
    patron = /[^\d\-]/; 
    te = String.fromCharCode(tecla); 
    return !patron.test(te); 
}

// regla formato rut
jQuery.validator.addMethod("rut", function(value) {
    return Fn.validaRut(value);
});

// regla solo letras
jQuery.validator.addMethod("sololetras", function(value) {
    patron = /^[A-ZáÁéÉíÍóÓúÚñÑa-z\s]+$/i;
    return patron.test(value);
});

// regla año 2000
jQuery.validator.addMethod("adulto",function(value){
	
	var anno = new Date(value).getFullYear();
	
	if(anno>2000){
		
		return false;
		
	}else{
		
		return true;
		
	}
	
});

// Jquery validate
$(document).ready(function(){
    $(function () {

        $("#formulario").validate({

            rules: {

                txtCorreoElectronico: {
                    required: true,
                    email: true
                },
                txtRun: {
                    required: true,
                    rut: true                   
                },
                txtNombreCompleto: {
                    required: true,
                    sololetras: true
                }, 
                txtFechaNacimiento: {
                    required: true,
                    date: true,
					adulto:true
                },
                txtTelefono: {
                    required: true,
                    number: true
                }

            },  //fin de reglas

            messages: {

                txtCorreoElectronico: {
                    required: " Ingrese el correo",
                    email: " Formato Invalido"
                },
                txtRun: {
                    required: " Ingrese el rut",
                    rut: "Run Invalido"               
                },

                txtNombreCompleto: {
                    required: " Ingrese el nombre",
                    sololetras: "Solo se permiten letras"
                },
                txtFechaNacimiento: {
                    required: " Ingrese la Fecha de Nacimiento",
                    date: " Formato Invalido",
                    adulto:"Debe ser un año anterior a 2001"
                },
                txtTelefono: {
                    required: " Ingrese el numero de telefono",
                    number: " Formato Invalido",
                    min: "asdasd"
                }

            },  //fin de mensajes

            errorClass: "invalid"

        });

    });

});



