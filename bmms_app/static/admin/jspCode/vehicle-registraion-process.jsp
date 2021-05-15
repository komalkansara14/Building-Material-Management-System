<%@include file = "../connection.jsp"%>
<%
	String name=request.getParameter("name");
	String type = request.getParameter("type");
	String company = request.getParameter("company");
	String number = request.getParameter("numberplate");
	String tag = request.getParameter("tag");;
			try{
	
	  //String encryptedPassword = encrypt(pass);					 
	  PreparedStatement ps = con.prepareStatement("{CALL vehicle_registration(?,?,?,?,?)}");
      ps.setInt(1,Integer.parseInt(name));
	  ps.setString(2,type);
      ps.setString(3,company);
      ps.setString(4,number);
	  ps.setString(5,tag);
      
	  ResultSet rs=ps.executeQuery();
	  out.println(name);
	  out.println("success");
	  
	  con.close();
			}
	catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>