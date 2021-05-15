<%@iclude file="../connection.jsp"%>
<%
		String userid="";
%>
<%
		userid=getParameter("id");
		PreparedStatement ps=con.prepareStatement("delete from user where id="+userid);
		int rowsdeleted =ps.executeUpdate();
			if(rowsDeleted > 0)
			{
				out.print("success");
			}
			else{
				out.print("error");
			}
%>