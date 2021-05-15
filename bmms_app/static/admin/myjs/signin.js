$(document).ready(function(){
	/*$("#login-form").submit(function(e){
		e.preventDefault();
	});*/
	$("#submit").click(function(){
		//alert("Enter");
		
		var email=$("#email").val();
		var pass=$("#inputPassword").val();
		var role=$("#role").val();
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
			$("#erroremail").html("<font color='red'>Please enter password.</font>");
			$("#email").css('border-color','red');
			isValid=false;
		}
		
		
		if(pass==''){
			$("#errorpass").html("<font color='red'>Please enter password.</font>");
			$("#inputPassword").css('border-color','red');
			isValid=false;
		}
		
		if(isValid){
			$.ajax({
				url:"jspCode/signin-process.jsp",
				type:"post",
				data:{
					email:email,
					pass:pass,
					role:role
				},
				beforeSend:function(){
					//alert("Please Wait...");
					$("#signinform").hide();
					$("#loader").show();

				},
				success:function(data){
						$("#signupform").show();
						$("#loader").hide();

					if(data.indexOf("success")>=0)
					{// jump to home page
						if(role=="Admin"){
							location.href = "index.jsp";
						}else if(role=="Owner"){
							location.href = "owner-index.jsp";
						}else if(role=="Taxcollector"){
							location.href = "taxcollector-index.jsp";
						}
						//$("#signinform").show();
						//$("#loader").hide();
						
					}else if(data.indexOf("invalid")>=0){
						//alert("Invalid username or password.");
						$("#message").addClass("text-danger");
						$("#message").html("Invalid username or password.");		
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