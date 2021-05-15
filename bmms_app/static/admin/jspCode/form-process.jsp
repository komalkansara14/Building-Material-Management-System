<%@include file = "../connection.jsp"%>
<%
	String email = request.getParameter("email");
	String pass = request.getParameter("pass");
	String password = "";
	
	try{
		PreparedStatement pst = con.prepareStatement("{CALL `admin_login`(?)}");  
		pst.setString(1,email);
		ResultSet rs = pst.executeQuery();
			if(rs.next()){
			 	password = decrypt(rs.getString("password"));
					if(password.equals(pass)){
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