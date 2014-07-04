var f = new Firebase('https://arduinobt.firebaseio.com/');

function toggle() {
	f.on('value', function(x) {
		var value = x.val()
		console.log(value);
	});
};
/*
		f.set({
			"light-value": value===
		});

		document.getElementById('current').innerHTML = value;
*/