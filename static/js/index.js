/*!
 * 首页JS
 *
 * author: zhouhuajian
 * version: v1.0
 */
$(function () {
    var modal = new bootstrap.Modal('.modal');
    $("form").on("submit", function (event) {
        event.preventDefault();
        var $form = $(this);
        var url = $form.attr("action");
        var data = $form.serialize();
        $.post(url, data, function (result) {
            if (result.success == 1) {
                location.reload();
            } else {
                $('.modal p').text(result.message);
                modal.show();
            }
        }, 'json');
    });
});  