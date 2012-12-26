// ==UserScript==
// @name        lxml
// @namespace   lxml-no-css
// @description lxml-no-css
// @require     http://code.jquery.com/jquery-latest.js
// @include     *
// @exclude     http://lt.cjdby.net/*
// @exclude     http://www.youtube.com/*
// @exclude     http://tv.cntv.cn/live/*
// @exclude     http://*youku.com/*
// @exclude     http://www.dbz.tv/*
// @exclude     http://www.dbz.tv/*
// @exclude     http://www.animeget.com/*
// @exclude     http://www.soku.com/*
// @version     1
// ==/UserScript==
$(document).ready(function(){
    $('head link').remove();
});
    // alert("css remove");
