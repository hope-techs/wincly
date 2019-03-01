
$(document).ready(function() {
    animateBtnTo();
    setInterval(animateBtnTo, 600);
});


function animateBtnTo() {
    var a;
    a = $("#BtnTo");
    setTimeout(function () {
      a.css({"transform": "translate(0px, -7px)",});
    }, 100);
    setTimeout(function () {
        a.css({"transform": "translate(0px, 0px)",});
    }, 400);
  }

  






