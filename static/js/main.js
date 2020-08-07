
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
        $("#userSearchCategory").removeClass('hidden');
        $("#userSearchExtraLocation, #userSearchLocationType, .locationOptions, .dateOptions").addClass('hidden');
    }
						
});

$('#locationType').change(function(){
    var val = $(this).val();
     if (val == "building") {
         console.log("building");
         $("#userSearchExtraLocation").removeClass('hidden');
         $("#postcodeLocation, #countyLocation, #cityLocation").addClass('hidden');
     }
     else {
         if (val == "city") {
            $("#cityLocation").removeClass('hidden');
            $("#userSearchExtraLocation, #countyLocation, #postcodeLocation, #buildingLocation").addClass('hidden');
        }
        else if (val == "county"){
            $("#countyLocation").removeClass('hidden');
            $("#userSearchExtraLocation, #cityLocation, #postcodeLocation, #buildingLocation").addClass('hidden');
        }

        else{
            $("#postcodeLocation").removeClass('hidden');
            $("#userSearchExtraLocation, #countyLocation, #cityLocation, #buildingLocation").addClass('hidden');
        }
     }
});

$('#extraLocationChoice').change(function(){
    var val = $(this).val();
     if (val == "postcode") {
        $("#postcodeLocation, #buildingLocation").removeClass('hidden');
        $("#countyLocation, #cityLocation").addClass('hidden');
     }
     else {
         if (val == "city") {
            $("#cityLocation, #buildingLocation").removeClass('hidden');
            $("#countyLocation, #postcodeLocation").addClass('hidden');
        }
        else if (val == "county"){
            $("#countyLocation, #buildingLocation").removeClass('hidden');
            $("#cityLocation, #postcodeLocation").addClass('hidden');
        }

        else{
             $("#countyLocation, #cityLocation, #postcodeLocation, #buildingLocation").addClass('hidden');                        
        }
     }
});


// Search entire db

$('#searchDbLocationType').change(function(){
    var val = $(this).val();
     if (val == "building") {
         console.log("building");
         $("#searchDbLocationExtraType").removeClass('hidden');
         $("#searchDbPostcode, #searchDbCity, #searchDbCounty").addClass('hidden');
     }
     else {
         if (val == "city") {
            $("#searchDbCity").removeClass('hidden');
            $("#searchDbLocationExtraType, #searchDbCounty, #searchDbPostcode").addClass('hidden');
        }
        else if (val == "county"){
            $("#searchDbCounty").removeClass('hidden');
            $("#searchDbLocationExtraType, #searchDbCity, #searchDbPostcode").addClass('hidden');
        }

        else{
            $("#searchDbPostcode").removeClass('hidden');
            $("#searchDbLocationExtraType, #searchDbCounty, #searchDbCity").addClass('hidden');
        }
     }
});

$('#searchDbLocationExtraTypeOptions').change(function(){
    var val = $(this).val();
     if (val == "postcode") {
         console.log("postcode reached")
        $("#searchDbPostcode").removeClass('hidden');
        $("#searchDbCounty, #searchDbCity").addClass('hidden');
     }
     else {
         if (val == "city") {
            $("#searchDbCity").removeClass('hidden');
            $("#searchDbCounty, #searchDbPostcode").addClass('hidden');
        }
        else if (val == "county"){
            $("#searchDbCounty").removeClass('hidden');
            $("#searchDbCity, #searchDbPostcode").addClass('hidden');
        }

        else{
             $("#searchDbCounty, #searchDbCity, #searchDbPostcode").addClass('hidden');                        
        }
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