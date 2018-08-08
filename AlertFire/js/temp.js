var Chik = 0
var numberCheck = function() {
	var result = document.getElementById('input').value;
	if (isNaN(result) == true) {
		alert("숫자만 입력가능합니다. ");
	} else {
		location.href="http://13.125.224.60:5000/templates/dangerous/"+result
	}
}
