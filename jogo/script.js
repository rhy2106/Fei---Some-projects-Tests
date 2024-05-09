let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");
// funcao para criar retangulos
function hitbox(a,b,c,d,cor){
    ctx.beginPath();
    ctx.lineWidth = "3px"
    ctx.strokeStyle = cor;
    ctx.strokeRect(a,b,c,d);
    ctx.closePath();
}
function quadrado(a,b,c,d,cor){
    ctx.beginPath();
    ctx.fillStyle = cor;
    ctx.fillRect(a,b,c,d);
    ctx.closePath();
}
// funcao pra criar textos
function texto(tamanho,texto,a,b){
    ctx.beginPath();
    ctx.fillStyle = "black";
    ctx.font = tamanho + " Arial";
    ctx.fillText(texto,a,b);
    ctx.fill();
    ctx.closePath();
}
// funcao pra criar tela de inicio
function inicio(){
    quadrado(0,0,400,600,"gray");
    texto("40px","Corrida Urbana",67.5,150)
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
    imagem() {
        ctx.drawImage(c1,this.x,this.y,this.a,this.l);
    }
    imagem2() {
        ctx.drawImage(c2,this.x,this.y,this.a,this.l);
    }
    cenario() {
        ctx.drawImage(fundo,this.x,this.y,this.a,this.l);
    }
    andar() {
        // mudar a posicao dos carros para baixo
        this.y += 5;
    }
}
// criar o carro do jogador
let jogador = new Carro(180,400,40,60,"gray");
let cenarios = [];
// criar lista pra armazenar os outros carros
let lista = [];
// criar os outros carros (Azuis) e armazenar na lista
for(let i = 0; i < 3; i++){
    cenarios.push(new Carro(0,(-600)*i,400,600,"gray"));
}
for(let i = 0; i < 15; i++){
   lista.push(new Carro(Math.floor(Math.random()*360), -100 - (100*i), 40, 60, "blue"));

}
// criar variavel pra tela do jogo
let tela = 0;
// atualizacao dos frames
function animacao(){
    ctx.clearRect(0,0,400,600);
    if(tela == 0){
        // tela 1 do jogo (inicio)
        inicio();
    }
    if(tela == 1){
        // tela 2 do jogo (Jogo)
        // cenario do jogo
        for(let i = 0; i < cenarios.length; i++){
            cenarios[i].cenario();
            cenarios[i].andar();
            if(cenarios[i].y >= 600){
                cenarios.splice(i,1);
                i--;
                cenarios.push(new Carro(0,-1200,400,600,"gray"));
            }
        }
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
        for(let i = 0; i < lista.length; i++){
            lista[i].imagem2();
            lista[i].andar();
            // verificar se o jogador tocou nos carros
            if(jogador.x + 40 > lista[i].x && jogador.x < lista[i].x && jogador.y < lista[i].y + 60 && jogador.y + 60 > lista[i].y){
                tela = 2;
            }

            if(jogador.x < lista[i].x + 40 && jogador.x > lista[i].x && jogador.y < lista[i].y + 60 && jogador.y + 60 > lista[i].y){
                tela = 2;
            }
            // excluir os carros que sairam da tela 
            // e criar um novo para deixar o jogo funcionando em loop
            if(lista[i].y >= 600){
                lista.splice(i,1);
                i--;
                lista.push(new Carro(Math.floor(Math.random()*360), -(100*lista.length), 40, 60, "red"));
            }
        }
        // atualizar o jogador
        jogador.imagem();
    }
    if(tela == 2){
        // tela 3 do jogo (fim)
        final();
    }
    requestAnimationFrame(animacao);
}
animacao();
// Recebe as teclas que o usuarios esta pressionando

document.addEventListener("keydown",function(evento){
    tecla = evento.key;
    if(tecla == "w"){
        jogador.y -= 10;
    }
    if(tecla == "s"){
        jogador.y += 10;
    }
    if(tecla == "a"){
        jogador.x -= 10;
    }
    if(tecla == "d"){
        jogador.x += 10;
    }
});

// Verifica se o usuario clicou no botao de começar um novo jogo
document.addEventListener("click",function(evento){
    rect = canvas.getBoundingClientRect();
    let posx = evento.clientX - rect.left;
    let posy = evento.clientY - rect.top;
    if(posx > 100 && posx < 300 && posy > 300 && posy < 350 && tela == 0){
        tela = 1;
    }
    if(posx > 75 && posx < 325 && posy > 300 && posy < 350 && tela == 2){
        tela = 1;
        jogador.x = 180;
        jogador.y = 400;
        for(let i = 0; i < lista.length; i++){
            lista[i].y = -100 - (100*i);
        }
        for(let i = 0; i < 3; i++){
            cenarios[i].y = (-600)*i;
        }
    }
});