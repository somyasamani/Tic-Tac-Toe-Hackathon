// script.js

const form = document.getElementById('login-form');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    if (username === '' || password === '') {
        errorMessage.textContent = 'Please fill in both username and password.';
        return;
    }

    // Here you would typically send a request to your server to verify the credentials
    // For this example, we'll just log the credentials to the console
    console.log(`Username: ${username}, Password: ${password}`);

    // Clear the form fields
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
});