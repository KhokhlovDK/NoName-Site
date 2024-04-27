
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("burger").addEventListener("click", function(){
        document.querySelector("body").classList.toggle("open")
    })
})