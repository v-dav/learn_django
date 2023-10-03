$(() => {
	$('button').on('click', () => {
		console.log("Nous avons réussi!");
		$.get('http://127.0.0.1:8000/depistclic/questions/', function (data) {
			$('body').append("<h1>Test I Learn API</h1>");
		})
	});
});
