
var submitForm = document.getElementById('contact-form');
submitForm.onsubmit = function(event) {
    event.preventDefault();
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var selected_list = document.getElementsByName("tags")[0].selectedOptions;
    var custom_field_list = [];
    var selected_value = [];
    var custom_field_values = document.querySelectorAll(".custom-fields");
    var custom_field_ids = document.querySelectorAll(".custom-field-id");
    for (var i = 0; i < selected_list.length; i++) {       
            selected_value.push(selected_list[i].value);
    }
    for(var i=0; i< custom_field_values.length; i++){
        var id = custom_field_ids[i].value
        var field_value = custom_field_values[i].value
        custom_field_list.push([custom_field_ids[i].value, custom_field_values[i].value]);
    }
    data_value = {
        'phone_no':document.getElementById("id_phone_no").value, 
        'first_name':document.getElementById("id_first_name").value,
        'last_name':document.getElementById("id_last_name").value,
        'birthday':document.getElementById("rw_date_month3").value,
        'anniversary':document.getElementById("rw_date_month4").value,
        'tags': selected_value,
        'override_timezone':document.getElementById("id_override_timezone").value,
        'custom_fields' : JSON.stringify(custom_field_list),
    }
    console.log(data_value);
    $.ajax({
        url : "", // the endpoint
        type : "POST", // http method
        headers: {'X-CSRFToken': csrftoken},
        data : data_value, // data sent with the post request
        // handle a successful response
        success : function(returnValue) {
            if ('success' in returnValue){
                location.reload()
            }

            else{
                submitForm.reset();
                alert(returnValue.error)
            }
        },
    });
}


function edit_contact(cur_id){
    $.ajax({
        url : cur_id+"/", // the endpoint
        type : "GET", // http method
        // handle a successful response
        success : function(returnValue) {
            if('success' in returnValue){
                console.log(returnValue);
                var edit_cont = document.getElementById('edit_cont').options;
                for(var i =0; i < edit_cont.length; i++){
                    if (edit_cont[i].text == returnValue['field_type']['tags']){
                        console.log('passs')
                    }
                }
            }
            else{
                alert('Some Error Occur please reload the page');
                location.reload()
            }
        },
    });
}