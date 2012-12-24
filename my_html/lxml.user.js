// ==UserScript==
// @name        lxml
// @namespace   lxml-no-css
// @description lxml-no-css
// @require     http://code.jquery.com/jquery-latest.js
// @include     http://lxml.de/index.html
// @version     1
// ==/UserScript==
$(document).ready(function(){
    $('head link').remove();
});
