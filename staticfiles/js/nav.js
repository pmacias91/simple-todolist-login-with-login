document.addEventListener("DOMContentLoaded", function() {
    // Get the current page URL
    var currentURL = window.location.href;

    // Get all the navbar links
    var navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    // Iterate over the navbar links and check if the URL matches
    for (var i = 0; i < navLinks.length; i++) {
      var link = navLinks[i];
      
      // Check if the URL in the navbar link matches the current URL
      if (link.href === currentURL) {
        // Add the "active" class to the parent li element
        link.parentNode.classList.add("active");
      }
    }
  });