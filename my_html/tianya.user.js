// ==UserScript==
// @name                tianya.cn
// @namespace	        wangdian.wdsl400.com
// @description	        tianya.cn
// @require http://code.jquery.com/jquery-latest.js
// @include		http://bbs.tianya.cn/list-worldlook-1.shtml
// @exclude
// @version     1
// ==/UserScript==
$(document).ready(function(){
    $('body').html($('table'));
    $('colgroup').remove();
    $('tbody:first').remove();
    $('tr td:first-child').siblings().remove();
});
