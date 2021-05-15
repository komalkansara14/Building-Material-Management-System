$(document).ready(function(){
	/*$("#login-form").submit(function(e){
		e.preventDefault();
	});*/
	$("#submit").click(function(e){
		//alert("Enter");
		e.preventDefault();
		var name=$("#name").val();
		var dob=$("#dob").val();
		var email=$("#email").val();
		var password=$("#password").val();
		var phoneno=$("#phoneNo").val();
		var address=$("#address").val();
		var edit_id=$("#edit_id").val();
		var isValid = true;
	
		//alert(email+" "+pass);
		
		var email_rex = /^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
		
		if(name==''){
			$("#errorname").html("<font color='red'>Please enter your name.</font>");
			$("#name").css('border-color','red');
			isValid=false;
		}
		if(dob==''){
			$("#errordob").html("<font color='red'>Please enter DOB.</font>");
			$("#dob").css('border-color','red');
			isValid=false;
		}
		if(!email_rex.test(email)){
			$("#erroremail").html("<font color='red'>Please enter valid email.</font>");
			$("#email").css('border-color','red');
			isValid=false;
		}
		
		if(password==''){
			$("#errorpass").html("<font color='red'>Please enter password.</font>");
			$("#password").css('border-color','red');
			isValid=false;
		}
		
		if(phoneno==''){
			$("#errorphoneno").html("<font color='red'>Please enter phone number.</font>");
			$("#phoneNo").css('border-color','red');
			isValid=false;
		}
		
		
		
		if(address==''){
			$("#erroraddress").html("<font color='red'>Please enter address.</font>");
			$("#address").css('border-color','red');
			isValid=false;
		}
		
		if(isValid){
			$.ajax({
				url:"jspCode/sub-user-edit-process.jsp",
				type:"post",
				data:{
					name:name,
					dob:dob,
					email:email,
					pass:password,
					phone:phoneno,
					
					address:address,
					edit_id:edit_id
				},
				beforeSend:function(){
					alert("Please Wait...");
				},
				success:function(data){
					if(data.indexOf("success")>=0)
					{// jump to home page
						//location.href = "signin.jsp";
						alert("successfully submitted..");
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