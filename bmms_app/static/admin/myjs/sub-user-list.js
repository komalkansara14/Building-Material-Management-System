// JavaScript Document
function getResult(){
	    $.ajax({
	url:"jspCode/sub-user-list-process.jsp",
	type:"POST",
	data:{
		name : $("#name").val(),
		phone : $("#phoneno").val()
		
			
	},
	beforeSend:function(){
					alert("Please Wait...");
						 },
	success:function(data){
			if(data.indexOf("invalid")>=0){
					alert("Invalid username or password.");	
			}else if(data.indexOf("error")>=0){
					alert("Server Error! Please try again later.");
			}else{
				$("#sub_user_data").html(data);
				}
						
			},
			error : function(){
					
			}
	
	});
	
}
$(document).ready(function(e) {
	getResult();
	
	$("#search").submit(function(e){
		e.preventDefault();
		getResult();
	});
});