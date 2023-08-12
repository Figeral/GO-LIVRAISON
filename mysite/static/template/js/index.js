const btn_cart = document.getElementsByClassName('addtocart');
for (let i = 0; i < btn_cart.length; i++) {
    btn_cart[i].addEventListener('click', handclick);
}

function handclick(e) {
    
        const btn = e.target;
        const description = btn.closest('.description');
        const name = description.querySelector('#name');
        const marque = description.querySelector('#marque');
        const price = description.querySelector('#price');
        console.log('name:', name.textContent);
        console.log('marque:', marque.textContent);
        console.log('price:', price.textContent);
        console.log('action:', btn);
        console.log('parentElement:', description);
}
