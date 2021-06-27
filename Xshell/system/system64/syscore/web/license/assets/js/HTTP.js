function httpGet(URL){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", URL, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
