#!/usr/bin/node
/**
  * adds the class red <header> element when the user clicks on the tag DIV#red_header
  * Using the JQuery API
  */
const $ = window.$;
$('DIV#red_header').click(function () {
  $('header').addClass('red');
});