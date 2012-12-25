// ==UserScript==
// @name        cjdby
// @namespace   wangdian.wdsl400.com
// @description lt.cjdby.net
// @require     http://code.jquery.com/jquery-latest.js
// @include     http://lt.cjdby.net/forum*
// @version     1
// ==/UserScript==
$(document).ready(function(){
    var telm = $('table[summary^="forum_"]');
    var tpgs = $('.pg:last');
    $('body').html($('#cd_nav a:lt(4)'));
    $('body').append(telm);
    $('tbody:lt(6)').remove();
    $('td').remove();
    $('body').append(tpgs);
});
// $('body > :not(#myid)').remove();
