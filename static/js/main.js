
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
            $("#searchDbLocationExtraType, #searchDbCounty, #searchDbPostcode, #searchDbBuilding").addClass('hidden');
            $('#searchDbLocationExtraTypeOptions').val("");
        }
        else if (val == "county"){
            $("#searchDbCounty").removeClass('hidden');
            $("#searchDbLocationExtraType, #searchDbCity, #searchDbPostcode, #searchDbBuilding").addClass('hidden');
            $('#searchDbLocationExtraTypeOptions').val("");
        }

        else{
            $("#searchDbPostcode").removeClass('hidden');
            $("#searchDbLocationExtraType, #searchDbCounty, #searchDbCity, #searchDbBuilding").addClass('hidden');
            $('#searchDbLocationExtraTypeOptions').val("");
        }
     }
});

$('#searchDbLocationExtraTypeOptions').change(function(){
    var val = $(this).val();
     if (val == "postcode") {
         console.log("postcode reached")
        $("#searchDbPostcode, #searchDbBuilding").removeClass('hidden');
        $("#searchDbCounty, #searchDbCity").addClass('hidden');
     }
     else {
         if (val == "city") {
            $("#searchDbCity, #searchDbBuilding").removeClass('hidden');
            $("#searchDbCounty, #searchDbPostcode").addClass('hidden');
        }
        else if (val == "county"){
            $("#searchDbCounty, #searchDbBuilding").removeClass('hidden');
            $("#searchDbCity, #searchDbPostcode").addClass('hidden');
        }

        else{
             $("#searchDbCounty, #searchDbCity, #searchDbPostcode").addClass('hidden');
             $("#searchDbBuilding").removeClass('hidden');                        
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
            format: "yyyy-mm-dd"
        }
    );
  });
   

 $(document).ready(function(){
    $('.sidenav').sidenav();
  });