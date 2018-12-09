$(document).ready(function () {
    $('.sp-wrap').smoothproducts();

    // handling product size selecting
    let sizeButton = $('.size');
    sizeButton.click(function () {
        $(this).toggleClass('chosen');
        $(this).siblings().removeClass('chosen');
    });

    // adding to cart
    $('.add-item').click(function (e) {
        e.preventDefault();
        let size = $('.chosen');

        if (size.length === 0) {
            alert('Выберите размер');
            return ;
        }

        let data = {};
        data['product_id'] = $(this).attr('product_id');
        data['size'] = size.text();
        data['quantity'] = $('.quantity-option:selected').attr('value');

        let url = $(this).attr('href');
        console.log(url);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("Success");
                $('.cart-items-number').text(response['items'])
            },
            error: function () {
                console.log('Error');
            }
        });
    });

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

    const product = $('.product');
    product.mouseenter(function () {
        cardMouseEnter($(this));
    });
    product.mouseleave(function () {
        cardMouseLeave($(this))
    });

    const sizesLayout = $('.sizes-table-layout');

    $('.sizes-table-link').click(function (e) {
        e.preventDefault();
        sizesLayout.css('display', 'block');
    });

    $('.close').click(function () {
        sizesLayout.css('display', 'none');
    });

});