// Avoid `console` errors in browsers that lack a console.
(function() {
  var method;
  var noop = function() {};
  var methods = ['assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error', 'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log', 'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd', 'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'];
  var length = methods.length;
  var console = (window.console = window.console || {});

  while (length--) {
    method = methods[length];

    // Only stub undefined methods.
    if (!console[method]) {
      console[method] = noop;
    }
  }
}());
if (typeof jQuery === 'undefined') {
  console.warn('jQuery hasn\'t loaded');
} else {
  console.log('jQuery has loaded');
}
// Place any jQuery/helper plugins in here.
//*
$('.item-qiwi a').on('click', function() {
    $('.choose-method').fadeOut('fast');
    $('.method-qiwi').fadeIn('fast');
})
//*
$('.item-bitcoin a').on('click', function() {
    $('.choose-method').fadeOut('fast');
    $('.method-bitcoin').fadeIn('fast');
})
$('.qiwi-pocket a').on('click', function() {
    $('.method-qiwi').fadeOut('fast');
    $('.captha-ispection').fadeIn('fast');
})

$('.get-code').on('click', function() {
    $('.captha-ispection').fadeOut('fast');
    $('.second-qiwi').fadeIn('fast');
})
