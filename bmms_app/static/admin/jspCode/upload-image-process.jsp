<%@include file ="../../connection.jsp"%>
<%
	DataFormatter formatter = new DataFormatter();
	boolean isMultipart = ServletFileUpload.isMultipartContent(request);
	String filePath = config.getServletContext().getRealPath("")+"/images/wallet/";
	File file;
     if (!isMultipart){
	 
     }else{
    		FileItemFactory factory = new DiskFileItemFactory();
	       	ServletFileUpload upload = new ServletFileUpload(factory);
       		List items = null;
	       	try{
               items = upload.parseRequest(request);
    	   	}catch (FileUploadException e){
               e.printStackTrace();
       		}
       		Iterator itr = items.iterator();     //this will create iterator object from list..used for traversing the data.
		    String amount = "";
	   		String payment = "";
	       	while (itr.hasNext()){
           		FileItem item = (FileItem) itr.next();
           		if (item.isFormField()){
			   		String name = item.getFieldName();
			   		String value = item.getString();
			   		if(name.equals("amount")){
					   amount=value;
					}
					if(name.equals("payment")){
					   payment=value;
					}
            	}else{
					PreparedStatement pst2=con.prepareStatement("select * from owner where email like '"+session.getAttribute("email")+"'");
					ResultSet rs2 = pst2.executeQuery();
					rs2.next();
					String id = rs2.getString("owner_id");
					
					PreparedStatement pst=con.prepareStatement("insert into wallet(owner_id,`amount`,`image_proof`,`payment_type`) values(?,?,?,?)",Statement.RETURN_GENERATED_KEYS);
					pst.setString(1,id);
					pst.setString(2,amount);
					pst.setString(3,"");
					pst.setString(4,payment);
					pst.executeUpdate();
					ResultSet rs = pst.getGeneratedKeys();
					rs.next();
					String key = String.valueOf(rs.getInt(1));
				
				
					try {
        	           	String itemName = item.getName();  
					   	String format= null;
						int index = itemName.lastIndexOf(".");
						if(index > 0){
							format = itemName.substring(index+1);
							format = format.toLowerCase();
						}
	                   	String filename=config.getServletContext().getRealPath("")+"/images/wallet/";
				   		String fname = "wallet-"+key+"."+format;
            	       	filename=filename+fname;      
                	   	File savedFile=new File(filename);
                   		item.write(savedFile);    
						
						PreparedStatement pst1=con.prepareStatement("update wallet set image_proof='"+fname+"' where id="+key);
						pst1.executeUpdate();
						
                   		out.println("success");
             		}catch(Exception ste){
                    	out.println(ste);
                	}
              	}
			}
       	}
%>