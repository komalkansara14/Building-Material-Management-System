function deleteUser(id){



$.ajax({
				url:"jspCode/tax-collector-delete.jsp",
				type:"post",
				data:{
					name:name,
					sheeft:sheeft,
					email:email,
					pass:password,
					dob:dob,
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
					}else if(data.indexOf("invalid")>=0){
						alert("Invalid username or password.");	
					}else if(data.indexOf("error")>=0){
						alert("Server Error! Please try again later.");
					}
						
				},
				error : function(xhr,status,error){
					alert(xhr+"-"+status+"-"+error);
				}
					
});
}

