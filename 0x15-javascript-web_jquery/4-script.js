$('#toggle_header').on('click', function (event) {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').addClass('green');
  }
});
