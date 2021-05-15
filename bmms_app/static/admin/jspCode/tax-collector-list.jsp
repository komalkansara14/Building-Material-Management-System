<%@include file="../connection.jsp"%>
<% 
	String name = request.getParameter("name");
	String phone = request.getParameter("phone");
	String shift = request.getParameter("sheeft");
	
	ArrayList al = new ArrayList();

	if(name!="" && name!=null){
		al.add("collector_name like '%"+name+"%'");
	}
	
	if(phone!="" && phone !=null){
		al.add("phone_no like '%"+phone+"%'");
	}
	
	if(shift!="" && shift!=null){
		al.add("shift like '%"+shift+"%'");
	}

		String condition ="";
		if(al.size()>0){
			condition = String.join(" and ", al);
		}
		
		String query = "select * from taxcollector";
		
		if(condition!=""){
			query += " where "  +condition;
		}
		//String query = "select * from taxcollector";
		query += " order by collector_id desc";
		
		//out.print(query);
		
		try{
		PreparedStatement pst = con.prepareStatement(query);  
		
		ResultSet rs = pst.executeQuery();
			if(rs.next()){
				rs.previous();
				int count=0;
				while(rs.next()){
					int i=rs.getInt("collector_id");
					count++;
					  out.print("<tr>");
					  out.print("<td><input type='checkbox' id='multi' name='multi' value='"+i+"'></td>");
                      out.print("<td>"+count+"</td>");
                      out.print("<td>"+rs.getString("collector_name")+"</td>");
					  out.print("<td>"+rs.getString("shift")+"</td>");
                      out.print("<td>"+rs.getString("phone_no")+"</td>");
                      out.print("<td>"+rs.getString("date_time")+"</td>");
					 // out.print("<td><button onClick='location.href=\"tax_collector_table.jsp?id="+rs.getString("collector_id")+"\"'>View</button></td>");
					  out.print("<td><button onClick='location.href=\"tax-collector-edit.jsp?id="+rs.getString("collector_id")+"\"'>Edit</button></td>");
					   out.print("<td><a href='jspCode/tax-collector-delete.jsp?id="+rs.getString("collector_id")+"'><button>Delete</button></a></td>");
                   out.print(" </tr>");
                   
					}
			 	
					
			}else{
				out.print("invalid");
			}
	}catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>
