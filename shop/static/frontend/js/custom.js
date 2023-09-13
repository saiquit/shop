(function () {
  "use strict";

  var featuredslider = function () {
    var el = document.querySelectorAll(".featured_slider");

    if (el.length > 0) {
      var slider = tns({
        container: ".featured_slider",
        items: 3,
        responsive: {
          360: {
            edgePadding: 20,
            gutter: 20,
            items: 1,
          },
          640: {
            edgePadding: 20,
            gutter: 20,
            items: 2,
          },
          700: {
            gutter: 30,
          },
          900: {
            items: 3,
          },
        },
        axis: "horizontal",
        // controlsContainer: "#testimonial-nav",
        swipeAngle: true,
        speed: 700,
        nav: false,
        controls: false,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 3500,
        autoplayButtonOutput: false,
      });
    }
  };

  featuredslider();

  var tinyslider = function () {
    var el = document.querySelectorAll(".testimonial-slider");

    if (el.length > 0) {
      var slider = tns({
        container: ".testimonial-slider",
        items: 1,
        axis: "horizontal",
        controlsContainer: "#testimonial-nav",
        swipeAngle: false,
        speed: 700,
        nav: true,
        controls: true,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 3500,
        autoplayButtonOutput: false,
      });
    }
  };
  tinyslider();

  var sitePlusMinus = function () {
    var value,
      quantity = document.getElementsByClassName("quantity-container");

    function createBindings(quantityContainer) {
      var quantityAmount =
        quantityContainer.getElementsByClassName("quantity-amount")[0];
      var increase = quantityContainer.getElementsByClassName("increase")[0];
      var decrease = quantityContainer.getElementsByClassName("decrease")[0];
      increase.addEventListener("click", function (e) {
        increaseValue(e, quantityAmount);
      });
      decrease.addEventListener("click", function (e) {
        decreaseValue(e, quantityAmount);
      });
    }

    function init() {
      for (var i = 0; i < quantity.length; i++) {
        createBindings(quantity[i]);
      }
    }

    function increaseValue(event, quantityAmount) {
      value = parseInt(quantityAmount.value, 10);

      console.log(quantityAmount, quantityAmount.value);

      value = isNaN(value) ? 0 : value;
      value++;
      quantityAmount.value = value;
    }

    function decreaseValue(event, quantityAmount) {
      value = parseInt(quantityAmount.value, 10);

      value = isNaN(value) ? 0 : value;
      if (value > 0) value--;

      quantityAmount.value = value;
    }

    init();
  };
  sitePlusMinus();

  var slider;
  0 < $(".productModal").length &&
    (slider = tns({
      container: "#productModal",
      items: 1,
      startIndex: 0,
      navContainer: "#productModalThumbnails",
      navAsThumbnails: !0,
      autoplay: !1,
      autoplayTimeout: 1500,
      swipeAngle: !1,
      speed: 1500,
      controls: !1,
      autoplayButtonOutput: !1,
      loop: !1,
    })),
    1 < $(".product").length &&
      (slider = tns({
        container: "#product",
        items: 1,
        startIndex: 0,
        navContainer: "#productThumbnails",
        navAsThumbnails: !0,
        autoplay: !1,
        autoplayTimeout: 1500,
        swipeAngle: !1,
        speed: 1500,
        controls: !1,
        autoplayButtonOutput: !1,
      }));
})();
function zoom(f) {
  var t = f.currentTarget;
  (offsetX = f.offsetX || f.touches[0].pageX),
    f.offsetY ? (offsetY = f.offsetY) : (offsetX = f.touches[0].pageX),
    (x = (offsetX / t.offsetWidth) * 100),
    (y = (offsetY / t.offsetHeight) * 100),
    (t.style.backgroundPosition = x + "% " + y + "%");
}

$(document).ready(function () {
  if ($('input[name="size"]:checked').length > 0) {
    // At least one radio button is selected
    // var selectedValue = $('input[name="size"]:checked').val();
    var price = $('input[name="size"]:checked').data("price");
    var sale = $('input[name="size"]:checked').data("sale");
    var stock = $('input[name="size"]:checked').data("stock");
    $("#sale").html(sale);
    $("#price").html(price);

    if (parseInt(stock) > 0) {
      $("#stock").html("In stock");
    } else {
      $("#stock").html("Out of stock");
    }
    // console.log("Selected Value on Page Load:", selectedValue);
  } else {
    // No radio button is selected
    // console.log("No radio button selected on Page Load");
  }
  // Add an event listener for the change event on the radio buttons
  $('input[name="size"]').change(function () {
    // Get the selected radio button's value
    var selectedValue = $(this).val();
    // Get the selected radio button's data-custom-attribute
    var price = $(this).data("price");
    var sale = $(this).data("sale");
    var stock = $(this).data("stock");

    $("#sale").html(sale);
    $("#price").html(price);
    if (parseInt(stock) > 0) {
      $("#stock").html("In stock");
    } else {
      $("#stock").html("Out of stock");
    }
    // Display the selected value and attribute in a result div
  });
});
