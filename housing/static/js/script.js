// script.js
function updatePrice(value) {
    const formattedValue = parseInt(value).toLocaleString();
    const maxPrice = 20000000; // Maximum pricee.toLocaleString(); 
    document.getElementById('price-label').textContent = `Ksh ${formattedValue} - Ksh ${formattedMax}`;
}
function performSearch() {
    const location = document.getElementById('location').value;
    const propertyType = document.getElementById('property-type').value;
    const priceRange = document.getElementById('price-range').value;

    console.log(`Searching for ${propertyType} in ${location} with a price up to Ksh ${priceRange}`);
}
