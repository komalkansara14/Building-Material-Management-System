$(document).ready(function(){
	/*$("#login-form").submit(function(e){
		e.preventDefault();
	});*/
	$("#submit").click(function(e){
		//alert("Enter");
		e.preventDefault();
		var name=$("#name").val();
		var email=$("#email").val();
		var password=$("#password").val();
		var phone_no=$("#phoneno").val();
		var dob=$("#dob").val();
		var address=$("#address").val();
		var isValid = true;
		//alert(email+" "+pass);
		
		var email_rex = /^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
		var passw=  /^[A-Za-z]\w{7,14}$/;
		var phoneno = /^\d{10}$/;
		
		if(name==''){
			$("#errorname").html("<font color='red'>Please enter your name.</font>");
			$("#name").css('border-color','red');
			isValid=false;
		}
		if(!email_rex.test(email)){
			$("#erroremail").html("<font color='red'>Please enter valid email.</font>");
			$("#email").css('border-color','red');
			isValid=false;
		}
	
		
		if(!passw.test(password)){
			$("#errorpass").html("<font color='red'>Please enter valid password.</font>");
			$("#password").css('border-color','red');
			isValid=false;
		}
		//else if(password<8 || password>10){
			//$("#errorpass").html("<font color='red'>Please enter password.</font>");
			//$("#password").css('border-color','red');
			
		//}
		
		if(!phoneno.test(phone_no)){
			$("#errorphone").html("<font color='red'>Please enter phone number.</font>");
			$("#phoneno").css('border-color','red');
			isValid=false;
			}
		
		if(dob==''){
			$("#errordob").html("<font color='red'>Please enter DOB.</font>");
			$("#dob").css('border-color','red');
			isValid=false;
		}
		
		if(address==''){
			$("#erroraddress").html("<font color='red'>Please enter address.</font>");
			$("#address").css('border-color','red');
			isValid=false;
		}
		
		if(isValid){
			$.ajax({
				url:"jspCode/signup-process.jsp",
				type:"post",
				data:{
					name:name,
					email:email,
					pass:password,
					phone:phone_no,
					dob:dob,
					address:address
				},
				beforeSend:function(){
					//alert("Please Wait...");
					$("#signupform").hide();
					$("#loader").show();
				},
				success:function(data){
					$("#signupform").show();
					$("#loader").hide();
					if(data.indexOf("success")>=0)
					{// jump to home page
						//location.href = "signin.jsp";
						//alert("Registration successful...");
						$("#message").addClass("text-success");
						$("#message").html("Registration successful.");
					}else if(data.indexOf("invalid")>=0){
						//alert("Invalid username or password.");
						$("#message").addClass("text-danger");
						$("#message").html("User with same email is already exist.");	
					}else if(data.indexOf("error")>=0){
						//alert("Server Error! Please try again later.");
						$("#message").addClass("text-danger");
						$("#message").html("Server Error! Please try again later.");
						
					}
						
				},
				error : function(){
					
				}
			});
		}
		
	});
});