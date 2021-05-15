$(document).ready(function(){
	$("#submit").click(function(e){
		e.preventDefault();
		//var vehicle_name=$("#vehicleName").val();
		var name=$("#name").val();
		var type=$("#type").val();
		var company=$("#company").val();
		var number_plate=$("#numberPlate").val();
		var tag=$("#tag").val();
		//var noc=$("#NOC").val();
		alert(name);
		var isValid=true;
		//alert(pass.length);
		var no_plate=/^[A-Za-z]{2}[ -][0-9]{1,2}(?: [A-Za-z])?(?: [A-Za-z]*)? [0-9]{4}$/;
		//alert("hello");
		
		if(name==''){
			$("#errorname").html("<font color='red'>Please enter company name.</font>");
			$("#name").css('border-color','red');
			isValid=false;
		}
		
		if(type==''){
			$("#errortype").html("<font color='red'>Please enter company name.</font>");
			$("#type").css('border-color','red');
			isValid=false;
		}
		
		if(company==''){
			$("#errorcompany").html("<font color='red'>Please enter company name.</font>");
			$("#company").css('border-color','red');
			isValid=false;
		}
		
		if(!no_plate.test(number_plate)){
			$("#errornumberplate").html("<font color='red'>Please enter the vehicle plate number.</font>");
			$("#numberPlate").css('border-color','red');
			isValid=false;
		}
		
		if(tag==''){
			$("#errortag").html("<font color='red'>Please enter tag ID.</font>");
			$("#tag").css('border-color','red');
			isValid=false;
		}
		
		

if(isValid){
			alert(name);
			$.ajax({
				url:"jspCode/vehicle-registraion-process.jsp",
				type:"post",
				data:{
					name:name,
					type:type,
					company:company,
					numberplate:number_plate,
					tag:tag
				},
				beforeSend:function(){
					alert("Please Wait...");
				},
				success:function(data){
					if(data.indexOf("success")>=0)
					{// jump to home page
						//location.href = "index.jsp";
						alert("vehicle registered successfully...");
					}else if(data.indexOf("invalid")>=0){
						alert("Invalid username or password.");	
					}else if(data.indexOf("error")>=0){
						alert("Server Error! Please try again later.");
					}
						
				},
				error : function(){
					
				}
			});
		}
		
	});
});
