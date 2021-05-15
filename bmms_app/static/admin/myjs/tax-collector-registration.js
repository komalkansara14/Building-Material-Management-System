$(document).ready(function(){
	/*$("#login-form").submit(function(e){
		e.preventDefault();
	});*/
	$("#submit").click(function(e){
		//alert("Enter");
		e.preventDefault();
		var name=$("#name").val();
		var sheeft=$("#sheeft").val();
		var email=$("#email").val();
		var password=$("#password").val();
		var dob=$("#dob").val();
		var phone_no=$("#phoneno").val();
		var address=$("#address").val();
		var isValid = true;
		//alert(email+" "+pass);
		
		var email_rex = /^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
		//var pass=  /^[A-Za-z]\w{7,14}$/;
		var passw=  /^[A-Za-z]\w{7,14}$/;
		var phoneno = /^\d{10}$/;
		//var phone_rex = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
		
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
		
		if(dob==''){
			$("#errordob").html("<font color='red'>Please enter DOB.</font>");
			$("#dob").css('border-color','red');
			isValid=false;
		}
		
		if(!phoneno.test(phone_no)){
			$("#errorphone").html("<font color='red'>Please enter phone number.</font>");
			$("#phoneno").css('border-color','red');
			isValid=false;
			}
		/*else if(phoneno.length<10 && phoneno.length>13){
			$("#errorphone").html("<font color='red'>Please enter valid phone number.</font>");
			$("#phoneno").css('border-color','red');
			isValid=false;
			}*/
		
		
		
		
		if(address==''){
			$("#erroraddress").html("<font color='red'>Please enter address.</font>");
			$("#address").css('border-color','red');
			isValid=false;
		}
		
		if(isValid){
			$.ajax({
				url:"jspCode/tax-collector-registration-proces.jsp",
				type:"post",
				data:{
					name:name,
					sheeft:sheeft,
					email:email,
					pass:password,
					dob:dob,
					phone:phone_no,
					address:address
				},
				beforeSend:function(){
					//alert("Please Wait...");
					$("#tcregistration").hide();
					$("#loader").show();
				},
				success:function(data){
						$("#tcregistration").show();
						$("#loader").hide();
					if(data.indexOf("success")>=0)
					{// jump to home page
						
						$("#message").addClass("text-success");
						$("#message").html("Registration successful.");
						//location.href = "taxcollector-index.jsp";
						//alert("Registration successful...");
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