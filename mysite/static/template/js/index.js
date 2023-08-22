let img = document.getElementById("go")
let header = document.getElementsByTagName('header')[0]
document.addEventListener('scroll', function (e) {
    img.style = "display:block;"

})

let detail = document.querySelector('.article_detail')
const btn_cart = detail.querySelector('.addtocart');
    btn_cart.addEventListener('click', function (e) {
        const action=e.target.dataset.action
        const article={
             id:detail.querySelectorAll('li > span')[0].innerText,
             name:detail.querySelectorAll('li > span')[1].innerText,
             marque:detail.querySelectorAll('li > span')[3].innerText,
        }       
        console.table([article.id,article.name,article.marque]);
        addtocart(article.id)
}); 
function addtocart(id){
    let data={article_id:id}
    let url='/updatecart'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-type':'application/json'
        },
        body:JSON.stringify(data)
  })
  .then(resoponse => resoponse.json())
  .then(data =>{
    console.log('success:',data);
  })
  .catch((error)=>{
    console.log('ERROR:',error);
  }) ;
}
// there's a forbidden error, need to include a django crsf token 





// const greeting=()=>{
//     console.log('print hello world');
// }
// greeting();

