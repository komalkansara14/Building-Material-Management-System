<%@include file="../connection.jsp"%>
<% 
	String name = request.getParameter("name");
	String number = request.getParameter("number");
	//String shift = request.getParameter("sheeft");
	
	ArrayList al = new ArrayList();

	if(name!="" && name!=null){
		al.add("vehicle_company like '%"+name+"%'");
	}
	
	if(number!="" && number!=null){
		al.add("vehicle_number like '%"+number+"%'");
	}
	
	
		String condition ="";
		if(al.size()>0){
			condition = String.join(" and ", al);
		}
		
		String query = "select * from vehicle";
		
		if(condition!=""){
			query += " where "  +condition;
		}
		//String query = "select * from taxcollector";
		query += " order by vehicle_id desc";
	    //out.print(query);
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
					  //out.print("<td>"+rs.getString("vehicle_id")+"</td>");
                      out.print("<td>"+rs.getString("vehicle_type")+"</td>");
                      out.print("<td>"+rs.getString("vehicle_company")+"</td>");
					  out.print("<td>"+rs.getString("vehicle_number")+"</td>");
					  out.print("<td>"+rs.getString("date_time")+"</td>");
					  //out.print("<td><button>Add Vehicle</button></td>");
					  out.print("<td><button onClick='location.href=\"vehicle-edit.jsp?id="+rs.getString("vehicle_id")+"\"'>Edit</button></td>");
					  out.print("<td><a href='jspCode/vehicle-delete.jsp?id="+rs.getString("vehicle_id")+"'><button>Delete</button></a></td>");
                   out.print(" </tr>");
                   
					}
			 	
					
			}else{
				out.print("invalid");
			}
	}catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>
