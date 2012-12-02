var updateVisibleSSIDs = function (ssids) {
  $('#ssids').html(ssids.join(', '));
  $('#scan_button').removeClass('disabled');
  $('#scan_button').html('Refresh');
};

var init = function () {
  // FIXME this assumes there is only one scan button
  var scanButton = $('#scan_button');
  if (!scanButton)
    return;

  scanButton.click(function (e) {
    e.preventDefault();
    scanButton.addClass('disabled');
    $('#ssids').html('');
    $.getJSON('/ssids/', updateVisibleSSIDs);
  });
};

$(init);
