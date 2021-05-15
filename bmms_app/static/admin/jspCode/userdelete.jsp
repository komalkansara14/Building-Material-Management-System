<%@include file="../connection.jsp"%>

<% 
		String userid="";
%>
<%
		userid=request.getParameter("id");
		PreparedStatement ps= con.prepareStatement("delete from owner where owner_id="+userid);
		int rowsDeleted = ps.executeUpdate();
		if (rowsDeleted > 0)
			{
				response.sendRedirect("../user_table.jsp");//out.print("success");
			}
		else
			{
				response.sendRedirect("../user_table.jsp");
			}
%>