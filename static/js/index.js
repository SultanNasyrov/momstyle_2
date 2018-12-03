$(document).ready(function () {

    // carousel
    let bannerImages = $('.banner-image');
    let firstBannerImage = bannerImages.first();
    let imagesNumber = bannerImages.length;

    firstBannerImage.addClass('active');
    firstBannerImage.siblings().addClass('dnone');

    function change_slide(current_slide, next_slide){
        current_slide
    };


})