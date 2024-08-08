#!/usr/bin/node
/**
 * Updates text color of header element to red
 * not allowed to use document.querySelector
 * must use JQuery API
 */
const $ = window.$;
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
