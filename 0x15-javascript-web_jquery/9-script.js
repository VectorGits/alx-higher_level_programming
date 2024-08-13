#!/usr/bin/node
/**
  * fetches and lists the title for all movies from https://swapi-api.hbtn.io/api/films/?format=json
  * you must use JQuery API
  */
const $ = window.$;
$(document).ready(function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.get(url, function(data) {
        $('#hello').text(data.hello);
    });
});
