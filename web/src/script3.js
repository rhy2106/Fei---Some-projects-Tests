let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

function quadrado(a,b,c,d,cor){
    ctx.beginPath();
    ctx.fillStyle = cor;
    ctx.fillRect(a,b,c,d);
    ctx.closePath();
}
class Bloco {
    x = 10;
    y = 10;
    a = 50;
    l = 50;
    cor = "red";

    constructor(x,y,a,l,cor) {
        this.x = x;
        this.y = y;
        this.a = a;
        this.l = l;
        this.cor = cor;
    }

    desenhar() {
        quadrado(this.x,this.y,this.a,this.l,this.cor);
    }
}

b1 = new Bloco(10,10,50,50,"red");

function animacao() {
    ctx.clearRect(0,0,300,300);
    if(b1.y > 250){
        b1.y = 250;
    }
    if(b1.y < 0){
        b1.y = 0;
    }
    if(b1.x > 250){
        b1.x = 250;
    }
    if(b1.x < 0){
        b1.x = 0;
    }
    b1.desenhar();
    requestAnimationFrame(animacao);
}

animacao();

document.addEventListener("mousemove", function(e){
    rect = canvas.getBoundingClientRect();
    let posx = e.clientX - rect.left - 25;
    let posy = e.clientY - rect.top - 25;
    b1.x = posx;
    b1.y = posy;
    
    console.log(b1.x, " ", b1.y)
}) 