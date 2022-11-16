const loginButton = document.getElementById('loginButton');
const registerButton = document.getElementById('registerButton');
const loginModal = document.getElementById('loginModal');
const registerModal = document.getElementById('registerModal');
const closeLoginModal = document.getElementById('closeLoginModal');
const closeRegisterModal = document.getElementById('closeRegisterModal');

loginButton.addEventListener('click', () => {
    loginModal.classList.remove('hidden');
    loginModal.classList.add('flex');
});

registerButton.addEventListener('click', () => {
    registerModal.classList.remove('hidden');
    registerModal.classList.add('flex');
});

closeLoginModal.addEventListener('click', () => {
    loginModal.classList.add('hidden');
    loginModal.classList.remove('flex');
});

closeRegisterModal.addEventListener('click', () => {
    registerModal.classList.add('hidden');
    registerModal.classList.remove('flex');
});