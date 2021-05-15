$(document).ready(function(){
	/*$("#login-form").submit(function(e){
		e.preventDefault();
	});*/
	$("#changepasswordform").submit(function(e){
		//alert("Enter");
		e.preventDefault();
		//var email=$("#email").val();
		//var role=$("#role").val();
		var currentpass=$("#currentpass").val();
		var changepass=$("#changepass").val();
		var repass=$("#repass").val();
		var isValid = true;
		//alert(email+" "+pass);
		//alert(role);
		//var email_rex = /^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
		
		/*if(!email_rex.test(email)){
			$("#erroremail").html("<font color='red'>Please enter valid email.</font>");
			$("#email").css('border-color','red');
			isValid=false;
		}*/
		
		if(currentpass==''){
			$("#errorcurrentpass").html("<font color='red'>Please enter password.</font>");
			$("#currentpass").css('border-color','red');
			isValid=false;
		}
		if(changepass==''){
			$("#errorchangepass").html("<font color='red'>Please enter password.</font>");
			$("#changepass").css('border-color','red');
			isValid=false;
		}
		if(repass==''){
				if(changepass!= repass){
				$("#error_repass").html("<font color='red'>Password not matched.</font>");
				$("#repass").css('border-color','red');
				isValid=false;
			}
			else
			{
				$("#error_repass").html("<font color='red'>Please re-enter password.</font>");
				$("#repass").css('border-color','red');
				isValid=false;
				
			}
		}
		
		if(isValid){
			$.ajax({
				url:"jspCode/changepassword-process.jsp",
				type:"post",
				data:{
					//currentpass:currentpass,
					pass:changepass,
					//repass:repass
				},
			
				success:function(data){
						/*$("#changepasswordform").show();
						$("#loader").hide();
*/
					if(data.indexOf("success")>=0)
					{// jump to home page
					alert(data);
						$("#message").html("Your password has been changed.");		
						//if(role=="Admin"){
							//location.href = "index.jsp";
						//}else if(role=="Owner"){
							//location.href = "owner-index.jsp";
					//	}else if(role=="Taxcollector"){
							//location.href = "taxcollector-index.jsp";
						//}
						//$("#signinform").show();
						//$("#loader").hide();
						
					}else if(data.indexOf("invalid")>=0){
						//alert("Invalid username or password.");
						$("#message").addClass("text-danger");
						$("#message").html("Password not changed.");		
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