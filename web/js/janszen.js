$(document).ready(function() {

    var optionsLocation = {
        target:        '#map',
        beforeSubmit:  workingBackground,
        success: doneWorking
    };

    // bind to the form's submit event
    $('#formLocation').submit(function() {
        $(this).ajaxSubmit(optionsLocation);
        return false;
    });
});

mapDiv = document.getElementById("map");
loadingDiv = document.getElementById("loading");
inputText = document.getElementById("inputLocation");
inputGeoButton = document.getElementById("inputGeoLocation");
inputSubmitButton = document.getElementById("inputSubmitButton");

function getLocation() {
    workingBackground();
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
      mapDiv.innerHTML = "Data: "+data;
      doneWorking();
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

function workingBackground() {
  disableFields();
  mapDiv.style.display = 'none';
  loadingDiv.style.display = 'block';
}

function doneWorking() {
  enableFields();
  mapDiv.style.display = 'block';
  loadingDiv.style.display = 'none';
}
