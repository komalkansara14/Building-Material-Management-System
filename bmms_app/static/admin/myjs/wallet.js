$(document).ready(function(e) {
	
	$("#walletform").on('submit',(function(e){
		e.preventDefault();
		var title = $("#amount").val();
		var file = $("#proof").val();
		var payment = $("#payment").val();
		
		var isValid = true;
		var ext = file.split('.').pop().toLowerCase();
		if($.inArray(ext, ['gif','png','jpg','jpeg']) == -1) {
    		alert('invalid extension!');
			var isValid = false;
		}	
		//alert($("#active").val());
		if(isValid){
			$.ajax({
				url: "jspCode/upload-image-process.jsp",
				type: "POST",
				data:  new FormData(this),
				beforeSend: function(){
					//$("#myModal").modal('show');
				},
				contentType: false,
				cache: false,
				processData:false,
				success: function(data){
					//$("#myModal").modal('hide');
					$("#uploadform")[0].reset();
					if(data.indexOf("success")>=0){
						$("#message").html('<div class="alert alert-success">Banner successfully uploaded.</div>');
					}else{
						$("#message").html('<div class="alert alert-warning">Server error. Please try again latter.</div>');
					}
					setTimeout(function(){
							$("#message").html("");
							$("#message").hide();
						},3000);
					//$("#targetLayer").html(data);
				},
				error: function(){} 	        
			});
		}
	}));
	
});
