// JavaScript Document
function getResult(){
	    $.ajax({
	url:"jspCode/tax-collector-list.jsp",
	type:"POST",
	cache:false,
	data:{
		name : $("#name").val(),
		phone : $("#phoneno").val(),
		sheeft :$("#shift").val(),
		//multi:""
			
	},
	beforeSend:function(){
					alert("Please Wait...");
						 },
	success:function(data){
		
			if(data.indexOf("invalid")>=0){
					alert("Invalid username or password.");	
			}else if(data.indexOf("error")>=0){
					alert("Server Error! Please try again later.");
			}else{
				$("#taxcollector_data").html(data);
				}
						
			},
			error : function(){
					
			}
	
	});
	
}
$(document).ready(function(e) {
	getResult();
	
	$("#search").submit(function(e){
		e.preventDefault();
		getResult();
	});
});

$(document).ready(function(e) {
    /*getResult();*/
$("#delete-all").click(function() {
	var multi=checkval();
	alert(multi);
	$.ajax({
		type:"POST",
		url:"jspCode/multi-tax-collector-delete.jsp",
		data:{
			multi:multi
			},
		beforeSend: function(){
			
				alert("please wait..");
				},
				
		success: function(data){
			alert(data);
			//getResult(false);
			}
	
	});
	});
});

function toggle(source){
	alert("hii");
	var checkboxes = document.getElementsByName('multi');
	for(var i=0,n=checkboxes.length;i<n;i++){
		 checkboxes[i].checked = source.checked;
		}
	}
// delete function


function checkval()
	{
		var arr = [];
		$("#multi:checked").each(function(){
			arr.push($(this).val());
		});
		alert(arr);
		return arr;
	}

// delete function

function deleteme(id){
		if(confirm("Are you sure you want to delete?")){
//var multi=checkval();
	$.ajax({
                url: "jspCode/multi-tax-collector-delete.jsp",
                type: "POST",
                cache: false,
                data :{
						multi : checkval(),
					},
				success: function(data) {
				getResult(false);
		
							
         
				}
					
            });
		}
}





