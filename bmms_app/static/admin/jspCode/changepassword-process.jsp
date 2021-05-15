<%@include file = "../connection.jsp"%>
<%
	String email = session.getAttribute("email").toString();
	//String currentpass = encrypt(request.getParameter("currentpass"));
	//String changepass = encrypt(request.getParameter("changepass"));
	String pass = encrypt(request.getParameter("pass"));
	String role= session.getAttribute("role").toString();
	String query="";
	
	try{
		
		if(role.equals("Admin") || role=="Admin"){
		
		query = "update admin set password = '"+pass+"' where email = '"+email+"'";
		
		}
		else if(role.equals("Owner")|| role=="Owner")
		{
			query = "update owner set password = '"+pass+"' where email = '"+email+"'";
		}
		else if(role.equals("Taxcollector") || role=="Taxcollector")
		{
			query = "update taxcollector set password = '"+pass+"' where email = '"+email+"'";
		}
		else
		{
			out.print("Select valid role");
		}
		PreparedStatement pst=con.prepareStatement(query);
		//pst.setString(1,email);
		int result = pst.executeUpdate();
		if(result==1){
			out.print("success");
		}else{
			out.print("invalid");
		}
		
	}catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>