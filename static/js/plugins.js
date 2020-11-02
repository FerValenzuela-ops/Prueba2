





/*==========  (NO TOCAR) Esto permite visualizar los waypoints ==========*/
$(function () { 
    function onScrollInit(items, trigger) { 
        items.each(function () { 
            var osElement = $(this), 
                osAnimationClass = osElement.attr('data-animation'), 
                osAnimationDelay = osElement.attr('data-delay'); 
            osElement.css({
                '-webkit-animation-delay': osAnimationDelay, // para safari 
                '-moz-animation-delay': osAnimationDelay, //para mozilla
                'animation-delay': osAnimationDelay // general
            });

            var osTrigger = (trigger) ? trigger : osElement; 

            osTrigger.waypoint(function () { 
                osElement.addClass('animated').addClass(osAnimationClass); 
            }, {
                    triggerOnce: true, 
                    offset: '70%' 
                });
        });
    }

    onScrollInit($('.os-animation')); //function call with only items
    onScrollInit($('.staggered-animation'), $('.staggered-animation-container')); //function call with items and trigger
});

/*========== [SOLO MOBILE]Cierra barra de navegacion al presionar en cualquierr parte  ==========*/
$(document).ready(function () { //when document loads completely.
    $(document).click(function (event) { 
        var clickover = $(event.target); 
        var _opened = $(".navbar-collapse").hasClass("show"); 
        if (_opened === true && !clickover.hasClass("navbar-toggler")) { 
            $(".navbar-toggler").click(); 
        }
    });
});









/*============================================================
Estas funciones permiten el correcto funcionamiento del owl carousel de la pagina index y nosotros
NO CAMBIAR NADA
=============================================================*/


/*========== Carrusel para la pagina de inicio ==========*/
$(document).ready(function () {
    $('#owl-carousel .carousel-wrap .owl-carousel').owlCarousel({
        autoplay: true, 
        autoplayHoverPause: true, 
        loop: true, 
        autoplayTimeout: 8000, 
        smartSpeed: 2000, 
        nav: true, 
        navSpeed: 1500, 
        navText: [ 
            "<i class='fas fa-chevron-left'></i>",
            "<i class='fas fa-chevron-right'></i>"
        ],
        responsive: { 
            0: {
                items: 1 
            }
        }
    });
});


/*========== Logo en el carrusel ==========*/
$(document).ready(function () {
    $('#logo-carousel .carousel-wrap .owl-carousel').owlCarousel({
        autoplay: true, 
        autoplayHoverPause: true, 
        loop: true, 
        autoplayTimeout: 4000, 
        smartSpeed: 1700, 
        margin: 10, 
        responsive: { 
            0: {
                items: 1 
            },
            600: {
                items: 3 
            },
            1000: {
                items: 5 
            }
        }
    });
});





/*========== Carrusel para la pagina de Nosotros ==========*/
$(document).ready(function () {
    $('#team-carousel .carousel-wrap .owl-carousel').owlCarousel({
        autoplay: true, 
        autoplayHoverPause: true, 
        loop: true, 
        autoplayTimeout: 8000,
        smartSpeed: 1800, 
        nav: true, 
        navSpeed: 1500, 
        margin: 10, 
        navText: [ 
            "<i class='fas fa-chevron-left'></i>",
            "<i class='fas fa-chevron-right'></i>"
        ],
        responsive: { 
            0: {
                items: 1 
            },
            1200: {
                items: 2 
            }
        }
    });
});












