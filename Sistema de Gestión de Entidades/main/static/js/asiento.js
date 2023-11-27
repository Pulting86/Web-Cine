function seleccionar(){
    const imgs = document.querySelectorAll('img');
    imgs.forEach((img) => {
      img.addEventListener('click', e => {
      e.stopImmediatePropagation()
        imgAcambiar=document.getElementById(e.target.id)
        if (imgAcambiar.src.includes("silla_seleccionada")){
            imgAcambiar.src="/static/img/silla_vacia.png";}else if(imgAcambiar.src.includes("silla_vacia.png")){
            imgAcambiar.src="/static/img/silla_seleccionada.png";}else{
            }
      });
    });

}

function reservar(){
    span=document.getElementById("ventanaReserva")
    span.removeAttribute("hidden")
}