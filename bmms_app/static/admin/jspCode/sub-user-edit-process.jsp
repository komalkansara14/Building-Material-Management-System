<%@include file = "../connection.jsp"%>
<%
	String name = request.getParameter("name");
	//String email = request.getParameter("email");
	//String pass = request.getParameter("pass");
	//String password = "";
	//String phoneno=request.getParameter("phone");
	String dob = request.getParameter("dob").toString();
	String email = request.getParameter("email").toString();
	String address = request.getParameter("address");
	String phone_no = request.getParameter("phone").toString();
	String id=request.getParameter("edit_id");
	
	out.print(dob);
	//String txtdate =CmFrm.getExpireDate(); 
	//SimpleDateFormat pd = new SimpleDateFormat("dd/MM/yyyy");  
	//SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd"); 
	//Date date = (Date) pd.parse(txtdate); 
	//String DisplayDate= df.format(date); 
	//System.out.println("MyExpireDate.."+DisplayDate);
	
	//String dateStr = request.getParameter("dob");
    //SimpleDateFormat formater = new SimpleDateFormat("yyyy-MM-dd");
    //String result = formater.parse(dateStr);
    //out.println(result); 
	//DateFormat df = new SimpleDateFormat("yyyy-MM-dd");
	//String reportDate = df.format(dob);
	try{
	
	 // String encryptedPassword = encrypt(pass);					 
	  PreparedStatement ps = con.prepareStatement("{CALL edit_subuser_process(?,?,?,?,?,?)}");
      ps.setString(1,name);
      //ps.setString(2,email);
     // ps.setString(3,encryptedPassword);
	 // ps.setString(4,phoneno);
      ps.setString(2,dob);
	  ps.setString(3,email);
	  ps.setString(4,address);
	  ps.setString(5,phone_no);
	  ps.setString(6,id);
	  
	  ResultSet rs=ps.executeQuery();
	  out.println("Success");
	  
	  con.close();
			}
	catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>