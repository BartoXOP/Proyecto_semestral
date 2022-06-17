$(function () {
    //fecha en crud producto
    $("#id_fecha_publicacion").datetimepicker({
        inline:true,
        dayOfWeekStart: '1',    //empieza el lunes
        startDate:'0',
        defaultDate:'+1970/01/01',
        defaultTime:0,
        minDate:0,           
        maxDate:'+1970/01/07',
        step:10,
        format: 'm/d/Y H:i',
    });
});

$(document).ready(function () {  
    jQuery.datetimepicker.setLocale('es');  
});  