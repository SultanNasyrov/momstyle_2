$(document).ready(function () {
    function cardMouseEnter(card) {
        let imageCaption = card.find('.image-caption');
        let image = card.find('.main-img');
        TweenMax.to(imageCaption, 0.5, {opacity: 1});
        TweenMax.to(image, 3, {scale: 1.3});
    }

    function cardMouseLeave(card) {
        let imageCaption = card.find('.image-caption');
        let image = card.find('img');
        TweenMax.to(imageCaption, 0.5, {opacity: 0});
        TweenMax.to(image, 3, {scale: 1});
    }

    $(".contact-phone").mask("+7 (999) 999-9999");

    // handle contact us form
    $('.contact-us').submit(function (e) {
        e.preventDefault();

        let name = $('.contact-name').val();
        let phone = $('.contact-phone').val();

        let url = $(this).attr('action');
        let data = {'name': name, 'phone': phone};

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("success");
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.up').click(function () {
        TweenMax.to(window, 0.5, {scrollTo: 0})
    });

});