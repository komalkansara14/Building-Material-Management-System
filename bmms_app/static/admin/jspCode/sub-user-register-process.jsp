<%@include file = "../connection.jsp"%>
<%
	String name = request.getParameter("name");
	String dob = request.getParameter("dob").toString();
	String email = request.getParameter("email");
	String pass = request.getParameter("pass");
	String password = "";
	String phoneno=request.getParameter("phone");
	String address = request.getParameter("address");
	//out.print(dob);
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
		
		  PreparedStatement ps1 = con.prepareStatement("select * from user where email like '"+email+"' or phone_no like '"+phoneno+"'");
		  ResultSet rs1 = ps1.executeQuery();
		  if(rs1.next()){
		  	out.print("invalid");
		  }else{
			  String encryptedPassword = encrypt(pass);					 
			  PreparedStatement ps = con.prepareStatement("{CALL sub_user_register(?,?,?,?,?,?)}");
			  ps.setString(1,name);
			  ps.setString(2,dob);
			  ps.setString(3,email);
			  ps.setString(4,encryptedPassword);
			  ps.setString(5,phoneno);
			  ps.setString(6,address);
			  
			  ResultSet rs=ps.executeQuery();
			  out.println("success");
		  }
	}
	catch(Exception e){
		out.print("error"+e.getMessage());
	}finally{
		con.close();
	}
%>