$(document).ready(function(){
    $('#btnSignUp').click(function(e) {
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                var valueList;
                valueList = JSON.parse(response, (key,value) => {
                    console.log(key);
                    return value; 
                });
                var output = "";
                for(key in valueList){
                    output += valueList[key] + "<br>";
                }
                $("#output").html(output);
            },
            error: function(error) {
                console.log(error);
            }
        });
        e.preventDefault();
    });
});
