// ==UserScript==
// @name        lxml
// @namespace   lxml-no-css
// @description lxml-no-css
// @require     http://code.jquery.com/jquery-latest.js
// @include     *
// @exclude     http://lt.cjdby.net/*
// @exclude     http://www.youtube.com/*
// @version     1
// ==/UserScript==
$(document).ready(function(){
    $('head link').remove();
});
    // alert("css remove");
