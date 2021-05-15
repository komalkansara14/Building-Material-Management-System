<%@include file = "../connection.jsp"%>
<%
	String name = request.getParameter("name");
	String dob = request.getParameter("dob").toString();
	String email = request.getParameter("email");
	String pass = request.getParameter("pass");
	String password = "";
	String phoneno=request.getParameter("phone");
	
	String address = request.getParameter("address");
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
	
	  String encryptedPassword = encrypt(pass);					 
	  PreparedStatement ps = con.prepareStatement("{CALL user_register(?,?,?,?,?,?)}");
      ps.setString(1,name);
	  ps.setString(2,dob);
      ps.setString(3,email);
      ps.setString(4,encryptedPassword);
	  ps.setString(5,phoneno);
      ps.setString(6,address);
	  
	  ResultSet rs=ps.executeQuery();
	  out.println("success");
	  
	  con.close();
			}
	catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>