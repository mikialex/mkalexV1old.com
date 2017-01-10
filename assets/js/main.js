//rem calculate
function setRem() {
    var width = document.body.clientWidth;
    if (width <= 1280) {
        $('html').css("font-size", "16px");
    }else if(width<=1920){
        var ratio = (width-0.5*(width-1280)) / 80
        var fontSize = ratio + "px";
        $('html').css("font-size", fontSize);
    } else{
        $('html').css("font-size", "20px");
    }
}

window.onresize = function() {
    setRem();
}

window.onload=function(){
    setRem();
}
