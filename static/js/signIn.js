$(document).ready(function(){
    $('#btnSignIn').on('click',function(e){
        $.ajax({
            url: '/signin',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
                var valueList;
                valueList = JSON.parse(response, (key,value)=>{
                    console.log(key);
                    return value;
                });
                console.log(String(valueList.data)); 
                window.open(valueList.redirect, "_blank"); 
            },
            error: function(error) {
                console.log(error);
            }
        });
        e.preventDefault();
    });
})
