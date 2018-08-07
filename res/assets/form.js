require(['assetman', 'http-api'], function (assetman, httpApi) {
    $('.form-cid-plugins-content-digest-frm-subscribe').on('submit:form:pytsite', function (e) {
        var emailInput = $(this).find('input[name=email]');

        httpApi.post('content_digest/subscribe', {email: emailInput.val()}).done(function (r) {
            emailInput.val('');
            alert(r.message);
        });
    });
});
