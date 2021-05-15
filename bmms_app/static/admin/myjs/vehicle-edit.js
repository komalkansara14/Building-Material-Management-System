$(document).ready(function(){
	/*$("#login-form").submit(function(e){
		e.preventDefault();
	});*/
	$("#submit").click(function(e){
		//alert("Enter");
		e.preventDefault();
		var owner=$("#name").val();
		var vehicle_type=$("#vehicletype").val();
		var vehicle_company=$("#vehiclecompany").val();
		var plate_number=$("#numberplate").val();
		var tag_id=$("#tagid").val();
		//var address=$("#address").val();
		var edit_id=$("#edit_id").val();
		var isValid = true;
	
		//alert(email+" "+pass);
		
		//var email_rex = /^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
		
		if(owner==''){
			$("#errorname").html("<font color='red'>Please enter your name.</font>");
			$("#name").css('border-color','red');
			isValid=false;
		}
		//if(!email_rex.test(email)){
		//	$("#erroremail").html("<font color='red'>Please enter valid email.</font>");
		//	$("#email").css('border-color','red');
		//	isValid=false;
		
		
		if(vehicle_type==''){
			$("#errorvehicletype").html("<font color='red'>Please enter vehicle type.</font>");
			$("#vehicletype").css('border-color','red');
			isValid=false;
		}
		
		if(vehicle_company==''){
			$("#errorcompany").html("<font color='red'>Please enter vehicle company.</font>");
			$("#vehiclecompany").css('border-color','red');
			isValid=false;
		}
		
		if(plate_number==''){
			$("#errornumberplate").html("<font color='red'>Please enter number plate.</font>");
			$("#numberplate").css('border-color','red');
			isValid=false;
		}
		
		if(tag_id==''){
			$("#errortag").html("<font color='red'>Please enter tag ID.</font>");
			$("#tagid").css('border-color','red');
			isValid=false;
		}
		
		if(isValid){
			$.ajax({
				url:"jspCode/vehicle-edit-process.jsp",
				type:"post",
				data:{
					name:owner,
					vehicle_type:vehicle_type,
					vehicle_company:vehicle_company,
					plate_number:plate_number,
					tag_id:tag_id,
					edit_id:edit_id
					},
				beforeSend:function(){
					alert("Please Wait...");
				},
				success:function(data){
					if(data.indexOf("success")>=0)
					{// jump to home page
						//location.href = "signin.jsp";
						alert("successfully edited..");
					}else if(data.indexOf("invalid")>=0){
						alert("Invalid username or password.");	
					}else if(data.indexOf("error")>=0){
						alert("Server Error! Please try again later.");
					}
						
				},
				error : function(){
					
				}
			});
		}
		
	});
});// JavaScript Document