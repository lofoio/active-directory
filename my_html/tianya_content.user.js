// ==UserScript==
// @name                tianya-content
// @namespace	        wangdian.wdsl400.com
// @description	        tianya content
// @require             http://code.jquery.com/jquery-latest.js
// @include		http://bbs.tianya.cn/post-worldlook*
// @exclude
// @version     1
// ==/UserScript==
$(document).ready(function(){
$('body').append('<p id="mylastp" font color="blue" ></p>');
var patt_trash=/(会拐弯的子弹)|(kjl245)|(铁三角铁骑)|(我真的很啊倏)|(davidlimshcn)|(寂寞夜聊人睾)|(langht)|(windows74)|(与孤独有关)|(单骑的路虾)|(牛联社)|(龙德德)|(maynard2008)|(forwardman)|(bclt)|(播种机)/;
var patt_fun=/(闻弦不知雅)/;
var mypg = $('form:last');
var myvstg = $('div.atl-info:first').find('span:first').text();
myvstg += $('div.atl-content:first').text();
// alert(myvstg);
$('div.atl-item[id]').each(function(){
    var ts = $(this).find('span:first').text();
    if(ts.search(patt_trash)==-1){
        myvstg += ts + $(this).find('div.bbs-content').text().replace(/.*(----|====|[*]{4}|___)/, "");}});
$('#mylastp').append(myvstg);
$('#mylastp').siblings().remove();
$('body').append(mypg);
$('#mylastp').css("font-size", "150%");
});
// alert($('div.atl-info span:eq(12)').text());
// $('#mylastp').append($('h1 span:first').text());
// $.twFile.load(filePath): load contents from file
// $.twFile.save(filePath, content): save contents to file
// $.twFile.copy(dest, source): duplicate existing file
// $.twFile.convertUriToLocalPath(filePath): normalizes specified absolute file path
// $('#mylastp').css("color", "green");
// $('body').css("background-color", "black");
