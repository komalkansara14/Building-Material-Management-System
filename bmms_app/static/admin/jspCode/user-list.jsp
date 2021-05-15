<%@include file="../connection.jsp"%>
<% 
	String name = request.getParameter("name");
	String phone = request.getParameter("phone");
	
	
	ArrayList al = new ArrayList();

	if(name!="" && name!=null){
		al.add("owner_name like '%"+name+"%'");
	}
	
	if(phone!="" && phone !=null){
		al.add("phone_no like '%"+phone+"%'");
	}
	
	
		String condition ="";
		if(al.size()>0){
			condition = String.join(" and ", al);
		}
		
		String query = "select * from owner";
		
		if(condition!=""){
			query += " where "  +condition;
		}
		//String query = "select * from taxcollector";
		query += " order by owner_id desc";
		try{
		PreparedStatement pst = con.prepareStatement(query);  
		
		ResultSet rs = pst.executeQuery();
			if(rs.next()){
				rs.previous();
				int count=0;
				while(rs.next()){
					count++;
					  out.print("<tr>");
					  out.print("<td><input type='checkbox'></td>");
                      out.print("<td>"+count+"</td>");
                      out.print("<td>"+rs.getString("owner_name")+"</td>");
                      out.print("<td>"+rs.getString("phone_no")+"</td>");
                      out.print("<td>"+rs.getString("date_time")+"</td>");
					  //out.print("<td><button onClick='location.href=\"vehicle_reg.jsp?id="+rs.getString("owner_name")+"\"'>Add Vehicle</button></td>");
					  out.print("<td><button onClick='location.href=\"userlist_edit.jsp?id="+rs.getString("owner_id")+"\"'>Edit</button></td>");
					   out.print("<td><a href='jspCode/userdelete.jsp?id="+rs.getString("owner_id")+"'><button>Delete</button></a></td>");
                   out.print(" </tr>");
                   
					}
			 	
					
			}else{
				out.print("invalid");
			}
	}catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>
