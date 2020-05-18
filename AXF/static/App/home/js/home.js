$(function () {
    initTopSwiper();
    initSwiperMenu();
})

function initTopSwiper() {
    var swiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        autoplay:3000,
    })
}

function initSwiperMenu() {
    var swiperMenu = new Swiper('#swiperMenu', {
        slidesPerView: 3,
    })
}