<%@include file="../connection.jsp"%>

<% 
		
		
		//out.println(multi);

		try{
			String[] multi = request.getParameterValues("multi[]");
			int ele=0;
			for(int i=0;i<multi.length;i++)
			{
				ele=Integer.parseInt(multi[i]);
				PreparedStatement ps= con.prepareStatement("delete from taxcollector where collector_id="+ele);
				ps.executeUpdate();
			}
			out.print("Success");
		}
		catch(Exception e){
			out.print("error"+e.getMessage());
		}
		finally{
			con.close();
		}
%>

		
		
		
		