function createXhr() {

    if (window.XMLHttpRequest) {
        //支持 XMLHttpRequest
        var xhr = new XMLHttpRequest();
    } else {
        //不支持XMLHttpRequest,使用 ActiveXObject 创建异步对象
        var xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }

    return xhr

}