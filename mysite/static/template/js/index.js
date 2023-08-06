const items = document.querySelectorAll('.item');
items.forEach(item => {
  item.addEventListener('click', function(e) {
    if (e.target.classList.contains('addtocart')) {
      const name = item.querySelector('.description #name').textContent;
      const marque = item.querySelector('.description #marque').textContent;
      const price = item.querySelector('.description #price').textContent;
      console.log('name:', name);
      console.log('marque:', marque);
      console.log('price:', price);
      console.log('action:', e.target);
    }
  });
});
