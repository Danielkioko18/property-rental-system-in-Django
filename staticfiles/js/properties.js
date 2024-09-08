const filterButton = document.querySelector('.filter-button');
const filterList = document.getElementById('filter-list');
const addButton = document.querySelector('.add-button');
const addModal = document.getElementById('add-modal');
const closeModalButton = document.getElementById('close-modal');

filterButton.addEventListener('click', function() {
    filterList.classList.toggle('hidden');
});

addButton.addEventListener('click', function() {
    addModal.style.display = 'flex';
});

closeModalButton.addEventListener('click', function() {
    addModal.style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target === addModal) {
        addModal.style.display = 'none';
    }
});

document.getElementById('add-property-form').addEventListener('submit', function(event) {
    event.preventDefault();
    console.log('Form submitted');
    addModal.style.display = 'none'; 
});