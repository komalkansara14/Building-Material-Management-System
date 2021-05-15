// JavaScript Document
function getResult(){
	    $.ajax({
	url:"jspCode/vehicle_list.jsp",
	type:"POST",
	data:{
		name : $("#name").val(),
		number : $("#number").val()
		//sheeft :$("#shift").val()
			
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
				$("#vehicle_data").html(data);
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