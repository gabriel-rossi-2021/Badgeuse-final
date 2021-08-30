var checkoutHistory = document.getElementById('_checkbox');
checkoutHistory.onchange = function() {
console.log(checkoutHistory);
    if (checkoutHistory.checked) {
        alert("Bon travail ! ");
    } else {
        alert("Bonne pause ! ");
    }
}