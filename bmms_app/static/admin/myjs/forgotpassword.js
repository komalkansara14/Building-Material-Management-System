$(document).ready(function(){
	/*$("#login-form").submit(function(e){
		e.preventDefault();
	});*/
	
	$("#submit").click(function(){
		//alert("Enter");
		var role=$("#role").val();
		var email=$("#email").val();
		//var pass=$("#inputPassword").val();
		//alert(email);
		var isValid = true;
		//alert(email+" "+pass);
		//alert(role);
		var email_rex = /^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
		
		
			if(!email_rex.test(email)){
				$("#erroremail").html("<font color='red'>Please enter valid email.</font>");
				$("#email").css('border-color','red');
				isValid=false;
			}
		
			if(email==''){
			$("#erroremail").html("<font color='red'>Please enter your email.</font>");
			$("#email").css('border-color','red');
			isValid=false;
		}
				
		
		
		if(isValid){
			$.ajax({
				url:"jspCode/forgotpassword-process.jsp",
				type:"post",
				data:{
					role:role,
					email:email
					},
				beforeSend:function(){
					//alert("Please Wait...");
					$("#forgotpassform").hide();
					$("#loader").show();

				},
				success:function(data){
						$("#forgotpassform").show();
						$("#loader").hide();

					if(data.indexOf("success")>=0)
					{// jump to home page
						
						$("#message").html("Your password has been updated. Please check your email.");
							$("#message").show();
							setTimeout(function(){
									$("#message").hide();
									location.href="signin.jsp";
								},3500);
							//$("#signinform").show();
						//$("#loader").hide();
						
					}else if(data.indexOf("invalid")>=0){
						//alert("Invalid username or password.");
						$("#message").addClass("text-danger");
						$("#message").html("Your email is invalid.");		
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