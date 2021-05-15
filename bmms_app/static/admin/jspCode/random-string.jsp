<%@include file="../connection-2.jsp"%>

<%
	public static String randomString(int n){
 	java.util.Random r =new java.util.Random();
  	String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
	String no="";
      for (int i=0; i<n; i++)
      	{
          	int index = (int)(r.nextDouble()*letters.length());
          	no += letters.substring(index, index+1);
      	}
   	 	return no;
}
%>
