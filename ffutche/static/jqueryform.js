$(document).ready(function() {
    $('#contact_username').on('input', function() {
        var input=$(this);
        var is_name=input.val();
        if(is_name <= 8 ){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_psword').on('input', function() {
        var input=$(this);
        var is_pass=input.val();
        if(is_pass <= 8 ){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
        if(is_pass.match(/[A-z]/) ){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
        if(is_pass.match(/[A-Z]/) ){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
        if(is_pass.match(/\d/) ){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_lname').on('input', function() {
        var input=$(this);
        var is_lname=input.val();
        if(is_lname){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_gender').on('input', function() {
        var input=$(this);
        var is_gender=input.val();
        if(is_gender == "Male" || is_gender == "Female"){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_address').on('input', function() {
        var input=$(this);
        var is_address=input.val();
        if(is_address){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_city').on('input', function() {
        var input=$(this);
        var is_city=input.val();
        if(is_city){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_state').on('input', function() {
        var input=$(this);
        var is_state=input.val();
        if(is_state){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_zip').on('input', function() {
        var input=$(this);
        var is_zip=input.val();
        if(is_zip.match(/\d/)){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_email').on('input', function() {
        var input=$(this);
        var re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        var is_email=re.test(input.val());
        if(is_email){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_cell').on('input', function() {
        var input=$(this);
        var is_cell=input.val();
        if(is_cell.match(/\d/)){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_country').on('input', function() {
        var input=$(this);
        var is_country=input.val();
        if(is_country){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $('#contact_dob').on('input', function() {
        var input=$(this);
        var is_dob=input.val();
        if(is_dob.match(/\d/)){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });
    $("#contact_submit button").click(function(event){
        var form_data=$("#contact").serializeArray();
        var error_free=true;
        for (var input in form_data){
            var element=$("#contact_"+form_data[input]['name']);
            var valid=element.hasClass("valid");
            var error_element=$("span", element.parent());
            if (!valid){error_element.removeClass("error").addClass("error_show"); error_free=false;}
            else{error_element.removeClass("error_show").addClass("error");}
        }
        if (!error_free){
            event.preventDefault(); 
        }
        else{
            alert('No errors: Form will be submitted');
        }
    });
});
