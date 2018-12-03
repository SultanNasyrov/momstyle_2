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


});