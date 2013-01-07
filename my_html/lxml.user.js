// ==UserScript==
// @name        lxml
// @namespace   lxml-no-css
// @description lxml-no-css
// @require     http://code.jquery.com/jquery-latest.js
// @include     *
// @exclude     http://lt.cjdby.net/*
// @exclude     http://ishare.iask.sina.com.cn/*
// @exclude     http://movie.mtime.com/*
// @exclude     http://zt.pptv.com/*
// @exclude     http://www.tudou.com/*
// @exclude     http://*.hupu.com/*
// @exclude     http://www.youtube.com/*
// @exclude     http://*.cntv.cn/*
// @exclude     http://*youku.com/*
// @exclude     http://www.dbz.tv/*
// @exclude     http://www.animeget.com/*
// @exclude     http://www.w3schools.com/xsl/tryxslt*
// @exclude     http://www.soku.com/*
// @exclude     http://bbs.hupu.com/*
// @exclude     http://*:8080/*
// @exclude     http://tieba.baidu.*
// @exclude     http://www.azhibo.com/*
// @version     1
// ==/UserScript==
$(document).ready(function(){
    $('head link').remove();
    // alert("css remove");
});
    // alert("css remove");
