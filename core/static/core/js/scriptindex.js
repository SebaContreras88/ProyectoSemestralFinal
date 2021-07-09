$(document).ready(function(){

    $.getJSON(

        'https://api.gael.cloud/general/public/clima/SCVM',
        function(data){

        var horatiempo = data.HoraUpdate;
        var lugar = data.Estacion;
        var tempera = data.Temp;
        var Humedad = data.Humedad;
        var Estado = data.Estado;

        $("#hora").html("Hora actual: " + horatiempo+" Hrs.")
        $("#lugar").html("Estacion: "+ lugar)
        $("#temperatura").html("Temperatura: "+ tempera+"℃")
        $("#Humedad").html("Humedad: "+ Humedad+"%")
        $("#Estado").html("Estado: "+ Estado)
        }
    );
});