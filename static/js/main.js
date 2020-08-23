
let collapsibleChoice;
let timeFrame;



// JS to make sure the uses adds all the relevant information for the initial add_report page.

$('#category').change(function(){
    var val1 = $("#category").val();
    var val2 = $("#add_report_to_authorities").val();
    console.log(val1);
    console.log(val2);
    if((val1 != undefined) && (val2 != undefined)){
        $("#addReportButton").prop("disabled", false);
    }
}
);

$('#add_report_to_authorities').change(function(){
    alert("reached")
    var val1 = $("#category").val();
    var val2 = $("#add_report_to_authorities").val();
    console.log(val1);
    console.log(val2);
    if((val1 != undefined) && (val2 != undefined)){
       $("#addReportButton").prop("disabled", false);
    }
}
);

// JS to make sure the uses adds all the relevant information for the search to go ahead.


$('#searchbyDiscrimination').change(function(){
    var val1 = $(this).val();
    console.log(val1);
    if(val1 != undefined){
        $("#searchCategoryButton").prop("disabled", false);
    }
}
);

$('#reportedToAuthorities').change(function(){
    var val1 = $(this).val();
    console.log(val1);
    if(val1 != undefined){
        $("#searchIncidentButton").prop("disabled", false);
    }
}
);

// Managing reports in dashboard

$('#userSearchType').change(function(){
    var val1 = $(this).val();
    console.log(val1);
    if(val1 == "all"){
        $("#managingReportSearchButton").prop("disabled", false);
    }
    else{
         $("#managingReportSearchButton").prop("disabled", true);

    }
}
);

$('#userDashSearchCat').change(function(){
    var val1 = $(this).val();
    console.log(val1);
    if(val1 != undefined){
        $("#managingReportSearchButton").prop("disabled", false);
    }
});

$('#userDashSearchBuilding, #userDashSearchCity, #userDashSearchCounty, #userDashSearchPostcode').change(function(){
    var locationTypeVal = $('#locationType').val();
    if(locationTypeVal != 'building'){
    var val1 = $(this).val();
    console.log(val1);
    if(val1 != undefined){
        $("#managingReportSearchButton").prop("disabled", false);
    }}
});





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
            $('#extraLocationChoice').val("");
        }
        else if (val == "county"){
            $("#countyLocation").removeClass('hidden');
            $("#userSearchExtraLocation, #cityLocation, #postcodeLocation, #buildingLocation").addClass('hidden');
            $('#extraLocationChoice').val("");
        }

        else{
            $("#postcodeLocation").removeClass('hidden');
            $("#userSearchExtraLocation, #countyLocation, #cityLocation, #buildingLocation").addClass('hidden');
            $('#extraLocationChoice').val("");
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
     $(document).ready(function(){
         $("#validatedPassword").css("display", "none");
    });


    $("#password").click(function(){  
    var password = document.getElementById('password')
    password.onkeyup = function(){
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
    var input = document.getElementById('password')
        if(input.value.match(passw))
            {
            $("#validatedPassword").css("display", "inline-block");
            }
        else
            {
            $("#validatedPassword").css("display", "none");
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

  
  $(document).ready(function(){
    $('.tooltipped').tooltip();
  });