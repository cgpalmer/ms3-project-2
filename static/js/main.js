 $("#category").change(function() {
        var val = $(this).val();
        if (val == "Xenophobia") {
            $("#subCategoryChoices").css("display", "block")
        }
        else if(val == "Xenophobia"){
            $("#addCategoryChoice").css("display", "block")
        }
 });