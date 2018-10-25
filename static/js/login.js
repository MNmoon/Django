<script>
    $('#js-captcha-refresh').click(function(){
        $.get("?newsn=1", function(result){
            $('.captcha').attr("src",result);
            $('#id_captcha_0').attr("value",result.split('/')[3]);
        });
        return false;
    });
</script>