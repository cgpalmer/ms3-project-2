
let collapsibleChoice;
let timeFrame;

//  Js to narrow down user choice when submitting forms.
// Searching the db
$("#categoryCollapsible").click(function(){
    collapsibleChoice = "category"
    timeFrame = ".catTimeFrameDisplay"
    console.log(timeFrame)
 });

$("#locationCollapsible").click(function(){
    timeFrame = ".locationTimeFrameDisplay"
 });

$("#reportedCollapsible").click(function(){
    timeFrame = ".reportedTimeFrameDisplay"
 });

 $("#allCollapsible").click(function(){
    timeFrame = ".allTimeFrameDisplay"
    
 });

 $(".timeFrameChoice").change(function() {
     
     var val = $(this).val();
     if (val == "Yes") {
            $(timeFrame).removeClass('hidden');
            console.log(timeFrame)
         }
    else {
            $(timeFrame).addClass('hidden');
        }
 });


// User dash - search js

$('#userSearchType').change(function(){
     var val = $(this).val();
     if (val == "all") {
     $("#userSearchCategory, #userSearchLocationType, #userSearchExtraLocation, .locationOptions, .dateOptions").addClass('hidden');

         }
    else if (val == "location") {
        $("#userSearchLocationType").removeClass('hidden');
        $("#userSearchCategory, #userSearchExtraLocation, .locationOptions, .dateOptions").addClass('hidden');
            console.log("location");
        }
    else if (val == "date") {
        $(".dateOptions").removeClass('hidden');
        $("#userSearchCategory, #userSearchLocationType, #userSearchExtraLocation, .locationOptions").addClass('hidden');
            console.log("date");
        }
    else {
        console.log("discrimination");
        $(".userSearchCategory").removeClass('hidden');
        $("#userSearchExtraLocation, .locationOptions, .dateOptions").addClass('hidden');
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
 
// In here add the code to put a tick next to the password box once it is a certain length.
    // Live validating the password
    $("#password").click(function(){  
    var password = document.getElementById('password')
    password.onkeyup = function(){
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
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
 });


// Animations
// Search page






// Materialize

 $(document).ready(function(){
    $('.collapsible').collapsible();
  });


   $(document).ready(function(){
    $('select').formSelect();
  });

   $(document).ready(function(){
    $('.datepicker').datepicker(
        {
            format: "dd/mm/yyyy"
        }
    );
  });
   

 $(document).ready(function(){
    $('.sidenav').sidenav();
  });