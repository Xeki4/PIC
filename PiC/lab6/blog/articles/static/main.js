document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        const password = form.password.value;
        const password2 = form.password2.value;

        if (password !== password2) {
            alert("Пароли не совпадают!");
            event.preventDefault(); // отменяем отправку формы
        }
    });
});
