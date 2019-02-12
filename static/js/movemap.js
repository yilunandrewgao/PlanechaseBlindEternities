$(function(){
	$('button').click(function(){
		$.ajax({
			url: '/movemap',
			type: 'POST',
			data: { 
	            id: $(this).val()
	        },
			success: function(response){
				window.location.reload(true);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});