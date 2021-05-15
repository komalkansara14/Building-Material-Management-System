<%@iclude file="../connection.jsp"%>
<%
		String vehicleid="";
%>
<%
		vehicleid=getParameter("id");
		PreparedStatement ps=con.prepareStatement("delete from vehicle where id="+vehicleid);
		int rowsdeleted =ps.executeUpdate();
			if(rowsDeleted > 0)
			{
				out.print("success");
			}
			else{
				out.print("error");
			}
%>