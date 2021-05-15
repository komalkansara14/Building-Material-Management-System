<%@include file="../connection.jsp"%>

<% 
		String userid="";
%>
<%
		userid=request.getParameter("id");
		PreparedStatement ps= con.prepareStatement("delete from user where user_id="+userid);
		int rowsDeleted = ps.executeUpdate();
		if (rowsDeleted > 0)
			{
				response.sendRedirect("../sub-user-table.jsp");//out.print("success");
			}
		else
			{
				response.sendRedirect("../sub-user-table.jsp");
			}
%>