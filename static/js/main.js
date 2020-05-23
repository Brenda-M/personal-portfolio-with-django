$(document).ready(function () {
  $('.menu-toggler').on('click', function(){
    $(this).toggleClass('open');
    $('.top-nav').toggleClass('open');
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



});