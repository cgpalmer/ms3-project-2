 $("#category").change(function() {
        var val = $(this).val();
        if (val == "Xenophobia") {
            $("#subCategoryChoices").css("display", "block")
        }
 });