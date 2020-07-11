 $("#category").change(function() {
        var val = $(this).val();
        if (val == "Xenophobia") {
            $("#subCategoryChoices").css("display", "block");
            $("#addCategoryChoice, #addSubCategoryChoice").css("display", "none")
        }
        else if(val == "Other"){
            $("#addCategoryChoice").css("display", "block")
            $("#subCategoryChoices, #addSubCategoryChoice").css("display", "none")
        }
        else{
            $("#subCategoryChoices, #addCategoryChoice, #addSubCategoryChoice").css("display", "none");
        }
 });

 $("#sub_category").change(function() {
        var val = $(this).val();
        if (val == "Other") {
            $("#addSubCategoryChoice").css("display", "block")
        }
        else{
            $("#addSubCategoryChoice").css("display", "none")
        }
 });


  $("#search_type").change(function() {
        var val = $(this).val();
        $(".searchValue").addClass("hidden");
        if (val == "email") {
            $("#search_email").removeClass("hidden");
        }
        else if (val == "username") {
            $("#search_username").removeClass("hidden");
        }

 });


  $("#basic").click(function(){;
      $("#orSearch").toggle();
  });

    $("#filtered").click(function(){;
      $("#filteredSearch").toggle();
  });



//  Signup page

// Temporarily seeing passwords.

$("#seePassword").click(function(){
         var seePassword = document.getElementById('password');
        seePassword.type = "text";
    var passwordTimeout = setTimeout(passwordReveal, 2000);
    function passwordReveal() {
        seePassword.type = "password";
    }
    clearTimeout();
    
})

$("#seeConfirmedPassword").click(function(){
         var seeConfirmedPassword = document.getElementById('confirmedPassword');
        seeConfirmedPassword.type = "text";
    var confirmedPasswordTimeout = setTimeout(confirmedPasswordReveal, 2000);
    function confirmedPasswordReveal() {
        seeConfirmedPassword.type = "password";
    }
    clearTimeout();
    
})




//   Matching passwords



// There is a console error on this. 
var confirmPassword = document.getElementById('confirmedPassword');

// In here add the code to put a tick next to the password box once it is a certain length.

password, confirmPassword.onkeyup = function(){
    var password = document.getElementById('password');
    if (confirmedPassword.value == password.value){
        console.log("match")
        $("#passwordMatch").removeClass("hidden");
        document.getElementById("signupButton").disabled = false;
        // In here add the code to put a tick next to the password box.
        
    } else {
        $("#passwordMatch").addClass("hidden");
        console.log("no match")
        document.getElementById("signupButton").disabled = true;
    }
    // Add in a loop here that checks for each array.
    
    }


     // Live validating the password
    password = document.getElementById('password')
    password.onkeyup = function(){
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    var input = document.getElementById('password')
        if(input.value.match(passw))
            {
            $("#validatedPassword").removeClass('hidden');
            }
        else
            {
            $("#validatedPassword").addClass('hidden');
            }
    }
