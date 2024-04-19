let canvas2 = document.getElementById("canvas2");
let ctx2 = canvas2.getContext("2d");
// funcao para criar retangulos
function quadrado(a,b,c,d,cor){
    ctx2.beginPath();
    ctx2.fillStyle = cor;
    ctx2.fillRect(a,b,c,d);
    ctx2.closePath();
}
// funcao pra criar textos
function texto(tamanho,texto,a,b){
    ctx2.beginPath();
    ctx2.fillStyle = "black";
    ctx2.font = tamanho + " Arial";
    ctx2.fillText(texto,a,b);
    ctx2.fill();
    ctx2.closePath();
}
// funcao pra criar tela de inicio
function inicio(){
    quadrado(0,0,400,600,"gray");
    texto("40px","Nome do jogo",67.5,150)
    quadrado(100,300,200,50,"lightgray");
    texto("50px","Iniciar",130,340)
}
// funcao pra criar tela de fim de jogo
function final(){
    quadrado(0,0,400,600,"gray");
    texto("50px","Você perdeu",50,150)
    quadrado(75,300,250,50,"lightgray");
    texto("40px","Recomeçar",100,340)
}
// class pra criar o carro
class Carro {
    x = 0;
    y = 0;
    a = 0;
    l = 0;
    cor = "red";
    // receber o valor inicial dos carros
    constructor(x,y,a,l,cor) {
        this.x = x;
        this.y = y;
        this.a = a;
        this.l = l;
        this.cor = cor;
    }
    desenha() {
        quadrado(this.x,this.y,this.a,this.l,this.cor);
    }
    andar() {
        // mudar a posicao dos carros para baixo
        this.y += 5;
    }
}
// criar o carro do jogador
let jogador = new Carro(180,400,40,60,"gray");
// criar lista pra armazenar os outros carros
let lista2 = [];
// criar os outros carros (Azuis) e armazenar na lista
for(let i = 0; i < 10; i++){
   lista2.push(new Carro(Math.floor(Math.random()*360), Math.floor(Math.random()*(-2000)), 40, 60, "blue"));
    
}
// criar variavel pra tela do jogo
let perdemo = 0;
// atualizacao dos frames
function animacao2(){
    ctx2.clearRect(0,0,400,600);
    if(perdemo == 0){
        // tela 1 do jogo (inicio)
        inicio();
    }
    if(perdemo == 1){
        // tela 2 do jogo (Jogo)
        // impedir que o jogador saida da tela
        if(jogador.x < 0){
            jogador.x = 0;
        }
        if(jogador.x > 360){
            jogador.x = 360;
        }
        if(jogador.y < 0){
            jogador.y = 0;
        }
        if(jogador.y > 540){
            jogador.y = 540;
        }
        // atualizar os outros carros
        for(let i = 0; i < lista2.length; i++){
            lista2[i].desenha();
            lista2[i].andar();
            // verificar se o jogador tocou nos carros
            if(jogador.x + 40 >= lista2[i].x && jogador.x <= lista2[i].x && jogador.y < lista2[i].y + 60 && jogador.y + 60 > lista2[i].y){
                perdemo = 2;
            }

            if(jogador.x <= lista2[i].x + 40 && jogador.x >= lista2[i].x && jogador.y < lista2[i].y + 60 && jogador.y + 60 > lista2[i].y){
                perdemo = 2;
        
            }
            // excluir os carros que sairam da tela 
            // e criar um novo para deixar o jogo funcionando em loop
            if(lista2[i].y > 600){
                lista2.splice(i,1);
                i--;
                lista2.push(new Carro(Math.floor(Math.random()*360), Math.floor(Math.random()*(-2000)), 40, 60, "red"));
            }
        }
        // atualizar o jogador
        jogador.desenha();
    }
    if(perdemo == 2){
        // tela 3 do jogo (fim)
        final();
    }
    requestAnimationFrame(animacao2);
}
animacao2();
// Recebe as teclas que o usuarios esta pressionando
document.addEventListener("keydown",function(evento){
    tecla = evento.key;
    if(tecla == "w" || tecla == "W"){
        jogador.y -= 10;
    }
    if(tecla == "s" || tecla == "S"){
        jogador.y += 10;
    }
    if(tecla == "a"|| tecla == "A"){
        jogador.x -= 10;
    }
    if(tecla == "d"|| tecla == "D"){
        jogador.x += 10;
    }
});
// Verifica se o usuario clicou no botao de começar um novo jogo
document.addEventListener("click",function(evento){
    rect = canvas2.getBoundingClientRect();
    let posx = evento.clientX - rect.left;
    let posy = evento.clientY - rect.top;
    if(posx > 100 && posx < 300 && posy > 300 && posy < 350 && perdemo == 0){
        perdemo = 1;
    }
    if(posx > 75 && posx < 325 && posy > 300 && posy < 350 && perdemo == 2){
        perdemo = 1;
        jogador.x = 180;
        jogador.y = 400;
        for(let i = 0; i < lista2.length; i++){
            lista2[i].y = Math.floor(Math.random()*(-2000));
        }
    }
});