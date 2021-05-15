<%@include file="../connection.jsp"%>

<% 
		String vehicleid="";
%>
<%
		vehicleid=request.getParameter("id");
		PreparedStatement ps= con.prepareStatement("delete from vehicle where vehicle_id="+vehicleid);
		int rowsDeleted = ps.executeUpdate();
		if (rowsDeleted > 0)
			{
				response.sendRedirect("../vehicle_table.jsp");//out.print("success");
			}
		else
			{
				response.sendRedirect("../vehicle_table.jsp");
			}
%>