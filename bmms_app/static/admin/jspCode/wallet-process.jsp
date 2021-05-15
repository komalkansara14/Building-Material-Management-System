<%@include file = "../connection.jsp"%>
<%
	String amount = request.getParameter("amount");
	String proof = request.getParameter("proof");
	String payment=request.getParameter("payment");
	String owner_id;
		PreparedStatement pst=con.prepareStatement("{CALL wallet_process(?,?,?)}");
			pst.setString(1,amount);
			pst.setString(2,proof);
			pst.setString(3,payment);
			  
			  ResultSet rs=pst.executeQuery();
			  out.println("success");
	}catch(Exception e){
		out.print("error"+e.getMessage());
	}
%>