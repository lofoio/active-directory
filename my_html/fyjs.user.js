// ==UserScript==
// @name        fyjs
// @namespace   wangdian.wdsl400.com
// @description fyjs.cn
// @require file:///usr/share/jquery/jquery-1.8.3.min.js
// @require http://code.jquery.com/jquery-latest.js
// @include     http://www.fyjs.cn/bbs/thread.php?fid=*
// @version     1
// ==/UserScript==
$(document).ready(function(){
    $('.listinline').css("text-align", "center");
    $('#toptool ul li:gt(5)').remove();
    var telm = $('#ajaxtable');
    var tpgs = $('.pages:last');
    $('body').html($('#toptool'));
    $('body').append(telm);
    $('body').append(tpgs);
    $('tbody:eq(0)').remove();
    $('tr:lt(14)').remove();
    $('td:not([id])').remove();
});
// $('body > :not(#myid)').remove();
// $("table tr:last").hide();##td{padding-top:5px !important;}
