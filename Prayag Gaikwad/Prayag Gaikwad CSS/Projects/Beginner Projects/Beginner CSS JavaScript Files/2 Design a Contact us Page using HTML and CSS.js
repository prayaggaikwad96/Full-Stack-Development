
const hamburger = document.getElementById("hamburger-icon");
const navMenu = document.getElementById("nav-menu");

hamburger.addEventListener("click", function () {
    navMenu.classList.toggle("active");

    const isExpanded = navMenu.classList.contains("active");

    hamburger.setAttribute("aria-expanded", isExpanded);
});
