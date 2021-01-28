var host = "localhost";
var port = "8888";

function initializeStream() {
    var w = window.innerWidth;
    var h = window.innerHeight;
    document.getElementById("stream-container").src = 'http://' + host + ':' + port + '/apps/VREDStream/index.html?width='+w+'&height='+h+'';
}

function updateVariantSets() {
    sendAndReceivePython("getVariantSets()", 
    (response) => {
        var variantSets = eval(response);

        if(variantSets) {
            // get a reference to our variant set container
            var variantSetContainer = document.getElementById('variant-set-container');

            // add element for each variant set
            variantSets.forEach(variantSet => {
                var variantSetNode = document.createElement('div');
                variantSetNode.innerHTML = variantSet;
                variantSetNode.onclick = function() {
                    sendAndReceivePython("selectVariantSet('"+variantSet+"')");
                }
                variantSetContainer.appendChild(variantSetNode);
            });
        }
    }
    );
}

function executeTerminalCode(python) {
    console.log(python);
    sendAndReceivePython(python, 
        (response) => {
            var text = document.getElementById('python-response').value;
            text += '\n' + response;
            document.getElementById('python-response').value = text;
        }, 
        (error) => console.error("Error sending pyhton command.", python)
    );
}

function sendAndReceivePython(command, successCallback, errorCallback) {
    var http = new XMLHttpRequest();
    var url = 'http://' + host + ':' + port + '/pythoneval2?value=' + encodeURI(command);
    http.open('GET', url, true);
    http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            if(this.responseText && successCallback) {
                successCallback(this.responseText)
            }
        }
    };
    http.onerror = function() {
        if(errorCallback) {
            errorCallback();
        }
    }
    http.send();
}


window.onload = function() {
    initializeStream();
    updateVariantSets();
}

window.onresize = function() {
    initializeStream();
}