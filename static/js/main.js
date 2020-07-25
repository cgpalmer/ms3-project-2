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





// //  Signup page

// // Temporarily seeing passwords.

$("#seePassword").click(function(){
         var seePassword = document.getElementById('password');
        seePassword.type = "text";
    var passwordTimeout = setTimeout(passwordReveal, 2000);
    function passwordReveal() {
        seePassword.type = "password";
    }
    clearTimeout();
    
})



// //   Matching passwords



// // There is a console error on this. 


// // In here add the code to put a tick next to the password box once it is a certain length.


    //  // Live validating the password
    // var password = document.getElementById('password')
    // password.onkeyup = function(){
    // var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
    // var input = document.getElementById('password')
    //     if(input.value.match(passw))
    //         {
    //         $("#validatedPassword").removeClass('hidden');
    //         }
    //     else
    //         {
    //         $("#validatedPassword").addClass('hidden');
    //         }
    // }



// Animations
// Search page

$("#searchLinkBasic").click(function(){ 
    $('#basicSearchForm'). attr('action', "/search_report_parameter");
    $('#basicSearchForm').css('display', 'block');
    $('#compareSearch').css('display', 'none');
    $('#orSearch').removeClass('order-sm-1').removeClass('order-sm-2').addClass('order-sm-3');
    $('#filteredSearch').removeClass('order-sm-2').removeClass('order-sm-3').addClass('order-sm-1');
    $('#comparedSearch').removeClass('order-sm-3').removeClass('order-sm-1').addClass('order-sm-2');

});

$("#searchLinkFilter").click(function(){ 
    $('#basicSearchForm'). attr('action', "/and_filter_parameters"); 
    $('#basicSearchForm').css('display', 'block');
     $('#compareSearch').css('display', 'none');
    $('#orSearch').removeClass('order-sm-3').removeClass('order-sm-2').addClass('order-sm-1');
    $('#comparedSearch').removeClass('order-sm-3').removeClass('order-sm-1').addClass('order-sm-2');
    $('#filteredSearch').removeClass('order-sm-2').removeClass('order-sm-1').addClass('order-sm-3');
});

$("#searchLinkCompare").click(function(){ 
    $('#compareSearch').css('display', 'block');
    $('#basicSearchForm').css('display', 'none');
    $('#orSearch').removeClass('order-sm-3').removeClass('order-sm-2').addClass('order-sm-1');
    $('#filteredSearch').removeClass('order-sm-2').removeClass('order-sm-1').addClass('order-sm-3');
    $('#comparedSearch').removeClass('order-sm-2').removeClass('order-sm-1').addClass('order-sm-3');
    
});

// Materialize

 $(document).ready(function(){
    $('.collapsible').collapsible();
  });


   $(document).ready(function(){
    $('select').formSelect();
  });

//    $(document).ready(function(){
//     $('.datepicker').datepicker();
//   });
 $('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 15, // Creates a dropdown of 15 years to control year,
            today: 'Today',
            clear: 'Clear',
            close: 'Ok',
            closeOnSelect: false // Close upon selecting a date,
        });

 $(document).ready(function(){
    $('.sidenav').sidenav();
  });