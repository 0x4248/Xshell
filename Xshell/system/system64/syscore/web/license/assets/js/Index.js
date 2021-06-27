var doc = `<section id="top"></section>
<h1 class="title">Licence</h1>
<div id="Warning"></div>
</div>
<div class="card">
    <a href="#bottom"><button>To Bottom of page</button></a> 
    <p id="main" class="main"></p>
    <section id="bottom"></section>
    <a href="#top"><button>To top of page</button></a>
</div>
<div class="card" style="margin-top: 20px;">
    <a href="https://raw.githubusercontent.com/awesomelewis2007/Xshell/main/LICENSE" style="margin-left: 10px;">Raw Text</a>
    <a href="https://github.com/awesomelewis2007/Xshell/blob/main/LICENSE" style="margin-left: 10px;">Source Of Licence</a>
    <a href="https://github.com/awesomelewis2007/Xshell" style="margin-left: 10px;">Xshell Homepage</a>
</div>`
document.getElementById("root").innerHTML = doc
var x = httpGet("https://raw.githubusercontent.com/awesomelewis2007/Xshell/main/LICENSE")
document.getElementById("main").innerHTML = x