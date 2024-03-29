document.addEventListener('DOMContentLoaded', function() {
    // Handle clicks on the main dropdown button
    document.querySelectorAll('.dropbtn').forEach(button => {
        button.addEventListener('click', function() {
            // Close all dropdowns first
            let allDropdownContents = document.querySelectorAll('.dropdown-content, .function-dropdown-content');
            allDropdownContents.forEach(function(content) {
                if (content !== this.nextElementSibling) {
                    content.classList.remove('show');
                }
            }, this);
            // Then toggle the clicked dropdown
            this.nextElementSibling.classList.toggle("show");
        });
    });

    // Handle clicks on function-specific dropdown buttons
    document.querySelectorAll('.function-dropbtn').forEach(button => {
        button.addEventListener('click', function(event) {
            // Prevent the main dropdown from closing when clicking on a function dropdown
            event.stopPropagation(); 
            // Close all other function-specific dropdowns
            let allFunctionDropdownContents = document.querySelectorAll('.function-dropdown-content');
            allFunctionDropdownContents.forEach(function(content) {
                if (content !== this.nextElementSibling) {
                    content.classList.remove('show');
                }
            }, this);
            // Then toggle the clicked function-specific dropdown
            this.nextElementSibling.classList.toggle("show");
        });
    });
});

// Close the dropdowns if the user clicks outside of them
window.addEventListener('click', function(event) {
    if (!event.target.matches('.dropbtn') && !event.target.matches('.function-dropbtn')) {
        var dropdowns = document.querySelectorAll('.dropdown-content, .function-dropdown-content');
        dropdowns.forEach(function(dropdown) {
            dropdown.classList.remove('show');
        });
    }
});
