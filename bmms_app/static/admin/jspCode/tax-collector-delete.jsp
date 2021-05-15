<%@include file="../connection.jsp"%>

<% 
		String userid="";
		/*ArrayList al=new ArrayList();
		
		for(int i=0;i<al.length();i++)
		{
			userid[i]=request.getParameter("check"+i);
			out.println(userid[i]);	
		}*/
%>
<%
		userid=request.getParameter("id");
		PreparedStatement ps= con.prepareStatement("delete from taxcollector where collector_id="+userid);
		int rowsDeleted = ps.executeUpdate();
		if (rowsDeleted > 0)
			{
				response.sendRedirect("../tax_collector_table.jsp");//out.print("success");
			}
		else
			{
				response.sendRedirect("../tax_collector_table.jsp");
			}
%>