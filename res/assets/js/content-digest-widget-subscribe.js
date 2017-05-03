define(['assetman', 'pytsite-http-api'], function (assetman, httpApi) {
    assetman.loadCSS('plugins.content_digest@content-digest-widget-subscribe.css');

    return function (widget) {
        var form = widget.em.find('form');

        form.submit(function (e) {
            e.preventDefault();

            var emailInput = form.find('input[name=email]');

            httpApi.post('content_digest/subscribe', {email: emailInput.val()}).done(function (r) {
                emailInput.val('');
                alert(r.message);
            });
        });
    }
});
