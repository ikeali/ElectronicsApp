const loader = document.querySelector('.loader-icon')

window.addEventListener('load', function(){
    this.setTimeout(myload, 1500)
})
function myload(){
    loader.style.display = 'none';
    document.body.style.overflow = 'auto';
}