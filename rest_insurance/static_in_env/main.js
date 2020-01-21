var btn = document.getElementById("btn")
var container = document.getElementById("ourcontainer")
var url = 'http://127.0.0.1:8000/api'
var url2 = 'http://127.0.0.1:8000/chronic2'

$.ajax({
	method: 'GET',
	url: url,
	success: function(data){
		console.log(data)
		console.log("success")
	},
	error: function(error_data){
		console.log("error")
	}
})

$.ajax({
	method: 'GET',
	url: url2,
	success: function(data){
		console.log(data)
		console.log("success")
	},
	error: function(error_data){
		console.log("error")
	}
})

btn.addEventListener("click", function(){
	var ourRequest = new XMLHttpRequest();
	ourRequest.open("GET", url);
	ourRequest.onload = function() {
		var ourData = JSON.parse(ourRequest.responseText);
		renderHTML(ourData);
	}
	ourRequest.send();

})

btn.addEventListener("click", function(){
	var ourRequest = new XMLHttpRequest();
	ourRequest.open("GET", url2);
	ourRequest.onload = function() {
		var ourData1 = JSON.parse(ourRequest.responseText);
		renderHTML(ourData1);
	}
	ourRequest.send();

})


function renderHTML(data) {
	var container = document.getElementById("ourcontainer")
	var htmlString = "";

	for (i=0; i < data.length; i++){
		htmlString += "<p>This items primary key is "  + data[i].pk + "</p>";
	}

	container.insertAdjacentHTML('beforeend', htmlString);
}
