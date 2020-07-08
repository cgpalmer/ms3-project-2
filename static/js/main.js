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




//   Matching passwords



var confirmPassword = document.getElementById('confirmedPassword');

password, confirmPassword.onkeyup = function(){
    var password = document.getElementById('password');
    if (confirmedPassword.value == password.value){
        console.log("match")
    } else {
        console.log("no match")
    }
    // Add in a loop here that checks for each array.
    
    }