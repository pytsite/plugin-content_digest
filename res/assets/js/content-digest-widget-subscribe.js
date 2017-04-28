define(['pytsite-http-api'], function (httpApi) {
    return function () {
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
