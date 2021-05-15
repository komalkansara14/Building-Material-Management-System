<%@include file = "../connection.jsp"%>
<%
	String email = request.getParameter("email");
	String pass = request.getParameter("pass");
	String password = "";
	String role=request.getParameter("role");
	String query="";
	try{
		
		if(role.equals("Admin") || role=="Admin")
		{
		query = "{CALL `admin_login`(?)}";
		
		}
		else if(role.equals("Owner")|| role=="Owner")
		{
			query="{CALL `owner_login`(?)}";
		}
		else if(role.equals("Taxcollector") || role=="Taxcollector")
		{
		query="{CALL `taxcollector_login`(?)}";
		}
		else
		{
			out.print("Select valid role");
		}
		out.print(query);
		PreparedStatement pst=con.prepareStatement(query);
		pst.setString(1,email);
		ResultSet rs = pst.executeQuery();
			if(rs.next()){
			 	password = decrypt(rs.getString("password"));
					if(password.equals(pass)){
						session.setAttribute("email",email);
						session.setAttribute("role",role);
						out.print("success");
					}else{
						out.print("invalid");
					}
			}else{
				out.print("invalid");
			}
	}catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>