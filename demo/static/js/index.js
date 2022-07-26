/*!
 * 首页JS
 * 
 * author: zhouhuajian
 * version: v1.0
 */
$(function () {
	var $modal = $('#modal')
	var modal = new bootstrap.Modal($modal.get(0))
	$('form').submit(function () {
		var $form = $(this);
		var url = $form.attr('action');
		var data = $form.serialize();
		$.post(url, data, function (result) {
			if (result.success == 1) {
				window.location.reload();
			} else {
				$modal.find('p').html(result.message)
				modal.show()
			}
		}, 'json');

		return false;
	});
});
