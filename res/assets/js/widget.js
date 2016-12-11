$(window).on('pytsite.widget.init:plugins.content_digest._widget.Subscribe', function(e, widget) {
    var form = widget.em.find('form');

    form.submit(function(e) {
        e.preventDefault();

        var emailInput = form.find('input[name=email]');

        pytsite.httpApi.post('content_digest/subscribe', {email: emailInput.val()}).done(function(r) {
            emailInput.val('');
            alert(r.message);
        });
    });
});
