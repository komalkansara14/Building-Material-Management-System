<%@include file = "../connection.jsp"%>
<%
	String role = request.getParameter("role");
	String email = request.getParameter("email");
	//String pass=;
	String rnd=encrypt(randomString(6));
	String query = "";
	try{
		
		if(role.equals("Admin") || role=="Admin"){
		
		query = "update admin set password = '"+rnd+"' where email = '"+email+"'";
		
		}
		else if(role.equals("Owner")|| role=="Owner")
		{
			query = "update owner set password = '"+rnd+"' where email = '"+email+"'";
		}
		else if(role.equals("Taxcollector") || role=="Taxcollector")
		{
			query = "update taxcollector set password = '"+rnd+"' where email = '"+email+"'";
		}
		else
		{
			out.print("Select valid role");
		}
		PreparedStatement pst=con.prepareStatement(query);
		rnd=randomString(8);
		sendMail(email,"Your Password has benn reset.","Your password has been reset. Your new password:"+rnd);
		int result = pst.executeUpdate();
		//if(result==1){
			/*String s = sendMail(email,"Your new Password",mail_Formate);
					out.print(s);								
				}else{
					out.print("Try Again");
				}*/
				
		out.print("success");
		
	}catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>