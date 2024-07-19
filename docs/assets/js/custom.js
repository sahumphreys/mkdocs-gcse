document.addEventListener("DOMContentLoaded", function() {
    var pagesToHideNavigation = ["/index.html", "/documents.html", "/about.html", "/contact.html"]; // Add paths for pages without pagination
    var currentPagePath = window.location.pathname;

    console.log("Page content loaded");
    if (pagesToHideNavigation.includes(currentPagePath)) {
        var footerNav = document.querySelector("nav.md-footer__inner");
        if (footerNav) {
            footerNav.style.display = "none";
        }
    }
});
