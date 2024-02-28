    window.addEventListener("scroll", function() {
        var content = document.querySelector(".content");
        var scrolled = window.scrollY;

        // Aplica algún efecto o lógica según sea necesario
        // En este ejemplo, simplemente cambiamos el color de fondo al hacer scroll
        if (scrolled > 100) {
        content.style.backgroundColor = "#e74c3c";
        } else {
        content.style.backgroundColor = "";
        }
    });