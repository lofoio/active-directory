// ==UserScript==
// @name        cjdby
// @namespace   wangdian.wdsl400.com
// @description lt.cjdby.net
// @require     http://code.jquery.com/jquery-latest.js
// @include     http://lt.cjdby.net/forum-112-1.html
// @version     1
// ==/UserScript==
$(document).ready(function(){
    // $('.listinline').css("text-align", "center");
    // $('#toptool ul li:gt(5)').remove();
    // var tptl = $('#toptool');
    alert($("tr").length);
    alert("hello");
    var telm = $('#threadlist');
    // var tpgs = $('.pages:last');
    $('body').empty();
    // $('body').append(tptl);
    $('body').append(telm);
    // $('body').append(tpgs);
    // $('tbody:eq(0)').remove();
    // $('tr:lt(14)').remove();
    // $('td:not([id])').remove();
});
// $('body > :not(#myid)').remove();
