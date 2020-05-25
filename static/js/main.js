
$(document).ready(function () {
  $('.menu-toggler').on('click', function(){
    $(this).toggleClass('open');
    $('.top-nav').toggleClass('open');
  });

  $('.top-nav .nav-link').on('click', function(){
    $('.menu-toggler').removeClass('open');
    $('.top-nav').removeClass('open');
  });

  $("#designDescription").hide();
  $("#developmentDescription").hide();
  $("#productDescripton").hide();

  $("#designImage").click(function () {
    $("#designImage").hide();
    $("#designDescription").show();
  });

  $("#designDescription").click(function () {
    $("#designDescription").hide();
    $("#designImage").show();
  });

  $("#developmentImage").click(function(){
    $("#developmentImage").hide();
    $("#developmentDescription").show();
  });

  $("#developmentDescription").click(function(){
    $("#developmentDescription").hide();
    $("#developmentImage").show();
  });
  
  $("#productImage").click(function (){
    $("#productImage").hide()
    $("#productDescripton").show()
  });

  $("#productDescripton").click(function (){
    $("#productDescripton").hide()
    $("#productImage").show()
  });

  // $('#message-container').on('click', function(){
  //   $(this).toggleClass('open');
  //   $('.top-nav').toggleClass('open');
  // });

  AOS.init({
    easing: 'ease',
    duration: 1800,
    once: true
  });

});

