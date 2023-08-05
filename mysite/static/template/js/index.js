const btns = document.querySelectorAll('.addtocart');
btns.forEach(btn => {
    
    btn.addEventListener('click',handclick,'false')
});
function handclick(e){
    e.preventDefault();
    console.log('A button was clicked');
}