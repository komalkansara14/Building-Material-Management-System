<%@include file = "../connection.jsp"%>
<%
	String type = request.getParameter("type");
	String company = request.getParameter("company");
	String number = request.getParameter("number_plate");
	String tag = request.getParameter("tag");;
			try{
	
	  String encryptedPassword = encrypt(pass);					 
	  PreparedStatement ps = con.prepareStatement("{CALL vehicle_registration(?,?,?,?)}");
      ps.setString(1,type);
      ps.setString(2,company);
      ps.setString(3,number);
	  ps.setString(4,tag);
      
	  ResultSet rs=ps.executeQuery();
	  out.println("Successfully registered");
	  
	  con.close();
			}
	catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>