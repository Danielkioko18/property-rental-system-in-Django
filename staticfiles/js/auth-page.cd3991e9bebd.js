const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');
const mobileToggleBtn = document.getElementById('mobileToggleBtn');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

mobileToggleBtn.addEventListener('click', () => {
    container.classList.toggle("active");
    if (container.classList.contains("active")) {
        mobileToggleBtn.textContent = "Switch to Sign In";
    } else {
        mobileToggleBtn.textContent = "Switch to Sign Up";
    }
});

// Function to check if the device is mobile
function isMobile() {
    return window.innerWidth <= 767;
}

// Function to update the visibility of forms based on screen size
function updateFormVisibility() {
    if (isMobile()) {
        if (container.classList.contains("active")) {
            mobileToggleBtn.textContent = "Switch to Sign In";
        } else {
            mobileToggleBtn.textContent = "Switch to Sign Up";
        }
    }
}

// Call the function on page load and window resize
window.addEventListener('load', updateFormVisibility);
window.addEventListener('resize', updateFormVisibility);