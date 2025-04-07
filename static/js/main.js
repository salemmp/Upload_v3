const productos=document.querySelectorAll(".producto")
const marco= document.getElementById("marco")


productos.forEach(x=>{
    
    x.addEventListener("click",()=>{
        marco.innerHTML=""
        let id= x.getAttribute('id')
        let url= `imagen/${id}`


        
     


        const peticion = async ()=>{
            const res = await fetch(url)
            const data = await res.json()
            let urls = data.urls
            urls.forEach(x=>{
                let img= document.createElement("img")
                img.setAttribute("data-aos","flip-up")
                img.setAttribute("src",x)
                marco.appendChild(img)
            })
            
        }
        peticion()
       
        
    })
})