<%@include file = "../connection.jsp"%>
<%
	String owner = request.getParameter("name");
	//String email = request.getParameter("email");
	//String pass = request.getParameter("pass");
	//String password = "";
	//String phoneno=request.getParameter("phone");
	String vehicle_type = request.getParameter("vehicle_type");
	String vehicle_company = request.getParameter("vehicle_company").toString();
	String plate_number = request.getParameter("plate_number");
	String tag_id = request.getParameter("tag_id");
	String id=request.getParameter("edit_id");
	
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
	
	 // String encryptedPassword = encrypt(pass);					 
	  PreparedStatement ps = con.prepareStatement("{CALL edit_vehicle_process(?,?,?,?,?,?)}");
      ps.setString(1,owner);
      //ps.setString(2,email);
     // ps.setString(3,encryptedPassword);
	 // ps.setString(4,phoneno);
      ps.setString(2,vehicle_type);
	  ps.setString(3,vehicle_company);
	  ps.setString(4,plate_number);
	  ps.setString(5,tag_id);
	  ps.setString(6,id);
	  
	  ResultSet rs=ps.executeQuery();
	  out.println("Success");
	  
	  con.close();
			}
	catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>