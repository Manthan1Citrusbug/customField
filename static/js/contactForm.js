
var submitForm = document.getElementById('contact-form');
submitForm.onsubmit = function(event) {
    event.preventDefault();
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    // var selected_list = document.getElementsByName("tags")[0].selectedOptions;
    // var selected_value = [];
    // for (var i = 0; i < selected_list.length; i++) {       
    //         selected_value.push(selected_list[i].value);
    // }
    
    var custom_field_list = [];
    var custom_field_values = document.querySelectorAll(".custom-fields");
    var custom_field_ids = document.querySelectorAll(".custom-field-id");
    for(var i=0; i< custom_field_values.length; i++){
        custom_field_list.push([custom_field_ids[i].value, custom_field_values[i].value]);
    }
    console.log(document.getElementsByName("tags").value)
    data_value = {
        'phone_no':document.getElementById("id_phone_no").value, 
        'first_name':document.getElementById("id_first_name").value,
        'last_name':document.getElementById("id_last_name").value,
        'birthday':document.getElementById("rw_date_month3").value,
        'anniversary':document.getElementById("rw_date_month4").value,
        'tags': document.getElementById('id_tags').value,
        'override_timezone':document.getElementById("id_override_timezone").value,
        'custom_fields' : custom_field_list,
    }
    $.ajax({
        url : "", // the endpoint
        type : "POST", // http method
        headers: {'X-CSRFToken': csrftoken},
        data : {'data_value':JSON.stringify(data_value)}, // data sent with the post request
        // handle a successful response
        success : function(returnValue) {
            if (returnValue.success == true){
                location.reload()
            }
            else{
                document.getElementById('error-add-contact').innerText = returnValue.error;
            }
        },
    });
}

// convert date to yy-mm-dd formate

function date_maker(date_val){
    var date_parts = date_val.split('-');
    var date_val = new Date(date_parts[0], date_parts[1], date_parts[2]);
    return(date_val.getFullYear()+"-"+date_val.getMonth()+"-"+date_val.getDate())
}

function edit_contact(cur_id){
    $.ajax({
        url : "edit-form/"+cur_id+"/", // the endpoint
        type : "GET", // http method
        // handle a successful response
        success : function(returnValue) {
            if('success' in returnValue){
                returnValue = returnValue['fields_data']
                document.getElementById('edit_id').value = returnValue['contact_id'];
                document.getElementById('edit_phone').value = returnValue['number'];
                document.getElementById('edit_fname').value = returnValue['firstname'];
                document.getElementById('edit_lname').value = returnValue['lastname'];
                document.getElementById('rw_date_month1').value = date_maker(returnValue['birthdate']);
                document.getElementById('rw_date_month2').value = date_maker(returnValue['anniversary']);
                document.getElementById('edit_tags').value = returnValue['tags']
                // var tags_cont = document.getElementById('edit_tags').options;
                // for(var i =0; i < returnValue['tags'].length; i++){
                //     if (returnValue['tags'] == tags_cont[i].value){
                //         tags_cont[i].setAttribute('selected','selected')
                //         break;
                //     }
                // }
                var time_cont = document.getElementById('edit_override').value = returnValue['override_timezone']
                // for(var i =0; i < time_cont.length; i++){
                //     if (returnValue['override_timezone'] == time_cont[i].value){
                //         time_cont[i].setAttribute('selected','selected')
                //     }
                // }
                data_field_values = returnValue['user_fields'];
                console.log(data_field_values)
                for(var i = 0; i < data_field_values.length; i++){
                    var cur_field = document.getElementById('edit_'+data_field_values[i]['name']);
                    if (cur_field.type == 'Date' && data_field_values[i]['value'] != ''){
                        cur_field.value = date_maker(data_field_values[i]['value']);
                    }
                    else{
                        cur_field.value = data_field_values[i]['value'];
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

var submitEditForm = document.getElementById('edit-contact');
submitEditForm.onsubmit = function(event) {
    event.preventDefault();
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var custom_field_list = [];
    var custom_field_values = document.querySelectorAll(".custom-edit");
    var custom_field_ids = document.querySelectorAll(".custom-edit-id");
    for(var i=0; i< custom_field_values.length; i++){
        custom_field_list.push([custom_field_ids[i].value, custom_field_values[i].value]);
    }
    data_value = {
        'client_id':document.getElementById('edit_id').value,
        'phone_no':document.getElementById('edit_phone').value, 
        'first_name':document.getElementById('edit_fname').value,
        'last_name':document.getElementById('edit_lname').value,
        'birthday':document.getElementById('rw_date_month1').value,
        'anniversary':document.getElementById('rw_date_month2').value,
        'tags': document.getElementById("edit_tags").value,
        'override_timezone':document.getElementById("edit_override").value,
        'custom_fields' : custom_field_list,
    }

    $.ajax({
        url : "edit-form/", // the endpoint
        type : "POST", // http method
        headers: {'X-CSRFToken': csrftoken},
        data : {'data_value':JSON.stringify(data_value)}, // data sent with the post request
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