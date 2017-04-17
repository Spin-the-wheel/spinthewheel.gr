$(document).ready(function(){

    //burger menu for mobile
    initMenu();
    $(window).resize(initMenu);

    $('#nav-icon').click(toggleMenu);

    // menu sticky on mobile
    // $(window).scroll(function() {


    //     if($(window).scrollTop() >= 20) {
    //         $('.header-container').addClass('fixed')
    //     }
    //     else {
    //         $('.header-container').removeClass('fixed')
    //     }
    // });

    $(window).scroll(function() {
        if ($(this).scrollTop()) {
            $('.icon-arrow:hidden').stop(true, true).fadeIn();
        } else {
            $('.icon-arrow').stop(true, true).fadeOut();
        }
    });

    $('.icon-arrow').on('click', function() {
        $("html, body").animate({ scrollTop: 0 }, 600);
    });


    // textarea auto height
    $(document)
    .one('focus.autoExpand', 'textarea.autoExpand', function(){
        var savedValue = this.value;
        this.value = '';
        this.baseScrollHeight = this.scrollHeight;
        this.value = savedValue;
    })
    .on('input.autoExpand', 'textarea.autoExpand', function(){
        var minRows = this.getAttribute('data-min-rows')|0, rows;
        this.rows = minRows;
        rows = Math.ceil((this.scrollHeight - this.baseScrollHeight) / 17);
        this.rows = minRows + rows;
    });

});


function toggleMenu() {
    $(this).toggleClass('open');

    var nav = $('nav');
    nav.slideToggle('slow').css('display', 'flex');
    $('body').toggleClass('hide');
}

function desktopMenu()  {
    var nav = $('nav');
    nav.css({
        'display': 'flex',
        'flex-direction': 'row',
        'justify-content': 'space-between',
        'z-index': '1'
    });
    resetBody();
}

function mobileMenu() {
    var nav = $('nav');
    $('#nav-icon').removeClass('open');
    nav.css({
        'display': 'none',
        'flex-direction': 'column',
        'justify-content': 'center',
        'align-items': 'center',

    });
    resetBody();
}

function initMenu() {
    if ($(window).outerWidth() > 900){
        desktopMenu();
    } else {
        mobileMenu();
    }
}

function resetBody() {
    if($('body').hasClass('hide')) {
        $('body').removeClass('hide');
    }
}
