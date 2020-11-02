/* cambio de colores en las paginas */
$(document).ready(function(){
        $('.toggle').click(function(){
            $('.toggle').toggleClass('active')
            $('body').toggleClass('night')
            $('nav').toggleClass('night')
            $('footer').toggleClass('night')
            
            
            
        })
    })
    