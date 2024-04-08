let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

function quadrado(a,b,c,d,cor1,cor2){
    ctx.beginPath();
    ctx.linewidth = '10px';
    ctx.strokeStyle = cor1;
    ctx.fillStyle = cor2;
    ctx.strokeRect(a,b,c,d);
    ctx.fillRect(a,b,c,d);
    ctx.stroke();
    ctx.closePath();
}
function arco(a,b,c,d,e,cor1,cor2){
    ctx.beginPath();
    ctx.lineWidth = '10px';
    ctx.strokeStyle = cor1;
    ctx.fillStyle = cor2;
    ctx.arc(a,b,c,d,e);
    ctx.stroke();
    ctx.fill();
    ctx.closePath();
}
function linha(a,b,c,d,cor){
    ctx.beginPath();
    ctx.lineWidth = '10px';
    ctx.strokeStyle = cor;
    ctx.moveTo(a,b);
    ctx.lineTo(c,d);
    ctx.stroke();
    ctx.closePath();
}
function texto(T,a,b,cor1,cor2){
    ctx.beginPath();
    ctx.lineWidth = 5;
    ctx.fillStyle = cor2;
    ctx.font = "20px Arial"
    ctx.fillText(T,a,b);
    ctx.closePath();
}


let q0 = quadrado(10,10,280,280,"black","white")
let a3 = arco(150,150,50,Math.PI,2*Math.PI,"green","white");
let a1 = arco(150,150,75,-0.25*Math.PI,0,"green","white");
let a2 = arco(150,150,75,Math.PI,1.25*Math.PI,"green","white");
let q1 = quadrado(10,10,50,50,"blue","blue");
let q2 = quadrado(240,10,50,50,"red","red");
let l1 = linha(10,10,150,150,"blue");
let l2 = linha(290,10,150,150,"red");
let q3 = quadrado(10,125,25,50,"cyan","cyan");
let q4 = quadrado(265,137.5,25,25,"cyan","cyan");
let l3 = linha(10,150,290,150,"green");
let l4 = linha(150,150,150,290,"black");
let a6 = arco(150,290,75,Math.PI,1.5*Math.PI,"green","white");
let a5 = arco(150,290,55,-0.5*Math.PI,0,"green","white");
let a4 = arco(150,290,40,-1*Math.PI,0,"green","cyan");
let q5 = quadrado(10,240,50,50,"yellow","yellow");
let q6 = quadrado(240,240,50,50,"black","black");
let q7 = quadrado(35,235,30,30,"white","white");
let q8 = quadrado(235,235,30,30,"white","white");
let q9 = quadrado(115,150,35,35,"red","red");
let a7 = arco(75,215,15,0,2*Math.PI,"green","yellow");
let a8 = arco(225,215,15,0,2*Math.PI,"green","yellow");
let a9 = arco(150,120,13,0,2*Math.PI,"green","cyan");
let T = texto("Canvas",117.5,55,'black','black');