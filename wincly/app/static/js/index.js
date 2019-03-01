/*Scroll to top when arrow up clicked BEGIN*/
$(window).scroll(function() {
    var height = $(window).scrollTop();
    if (height > 100) {
        $('#back2Top').fadeIn();
    } else {
        $('#back2Top').fadeOut();
    }

});



// Doc Ready
$(document).ready(function() {
    
    // Animations initialization
    new WOW().init();

    // Back to top
    $("#back2Top").click(function(event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });


    // Add smooth scrolling to all links
    $("a").on('click', function(event) {

        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();

        // Store hash
        var hash = this.hash;

        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 800, function(){
    
            // Add hash (#) to URL when done scrolling (default click behavior)
            window.location.hash = hash;
        });
        } // End if
    });

    // object-fit polyfill run
    // objectFitImages();

    /* init Jarallax */
    // jarallax(document.querySelectorAll('.jarallax'));

    // jarallax(document.querySelectorAll('.jarallax-keep-img'), {
        // keepImg: true,
    // });

    activeTab();

});
 /*Scroll to top when arrow up clicked END*/

 



function activeTab() {
    var p = window.location.pathname
    var items = $("nav li")
    items.removeClass("active");
    for (let i = 0; i < items.length; i++) {
        var id = items[i].id;
        if (p.includes(id)) {
            $("#" + id).addClass("active");
            break;
        }
        else {
            // items[0].addClass("active");
            console.log(items[0]);
        }
    }
}



