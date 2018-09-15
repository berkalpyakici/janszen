$(document).ready(function() {

    var optionsLocation = {
        target:        '#map',
        beforeSubmit:  disableFields,
        success: enableFields
    };

    // bind to the form's submit event
    $('#formLocation').submit(function() {
        $(this).ajaxSubmit(optionsLocation);
        return false;
    });
});

var mapDiv = document.getElementById("map");
var inputText = document.getElementById("inputLocation");
var inputGeoButton = document.getElementById("inputGeoLocation");
var inputSubmitButton = document.getElementById("inputSubmitButton");

function getLocation() {
    disableFields();
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(sendPosition);
    } else {
        mapDiv.innerHTML = "Geolocation is not supported by this browser.";
        enableFields();
    }
}

function sendPosition(position) {
    $.post( "search-geolocation", { latitude:  position.coords.latitude, longitude: position.coords.longitude })
    .done(function( data ) {
      mapDiv.innerHTML = data;
      enableFields();
    });
}

function disableFields() {
  $(inputText).attr('disabled', true);
  $(inputGeoButton).attr('disabled', true);
  $(inputSubmitButton).attr('disabled', true);
}

function enableFields() {
  $(inputText).attr('disabled', false);
  $(inputGeoButton).attr('disabled', false);
  $(inputSubmitButton).attr('disabled', false);
}
