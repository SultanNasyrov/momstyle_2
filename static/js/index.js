$(document).ready(function () {
    $(function() {
        $('.slide').slide();
	});

    const category = $('.category');

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

    category.mouseenter(function () {
        cardMouseEnter($(this));
    });
    category.mouseleave(function () {
        cardMouseLeave($(this));
    });

    const product = $('.product');
    product.mouseenter(function () {
        cardMouseEnter($(this));
    });
    product.mouseleave(function () {
        cardMouseLeave($(this))
    });

    const look = $('.look');
    look.mouseenter(function () {
        cardMouseEnter($(this))
    });
    look.mouseleave(function () {
        cardMouseLeave($(this))
    });

    const catalogBtn = $('.catalog-btn');
    catalogBtn.mouseenter(function () {
        TweenMax.to($(this), 0.5, {backgroundColor: 'rgba(0, 0, 0, 0.6)'});
    });

    catalogBtn.mouseleave(function () {
        TweenMax.to($(this), 0.5, {backgroundColor: 'rgba(0, 0, 0, 0.3)'});
    });
});