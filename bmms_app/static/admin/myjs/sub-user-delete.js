function deleteUser(id){



$.ajax({
				url:"jspCode/sub-user-delete-process.jsp",
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
