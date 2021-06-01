document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('form').onsubmit = function() {
    fetch('http://api.exchangeratesapi.io/v1/latest?access_key=6d7e781e6e4c07b61545c5a5d5e7a92c')
    .then(response => response.json())
    .then(data => {
        const currency = document.querySelector('#currency').value.toUpperCase();

        const rate = data.rates[currency];

        if (rate != undefined) {
            document.querySelector('#result').innerHTML = `1 EUR is equal to ${rate.toFixed(3)} ${currency}.`;
        }
        else {
            document.querySelector('#result').innerHTML = 'Invalid Currency';
        }
        
    })
    .catch(error => {
        console.log('Error:', error)
    })
    return false;
}
})