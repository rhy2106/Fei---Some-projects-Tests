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
function final(melhor_pontuacao,pontuacao){
    quadrado(0,0,400,600,"gray");
    texto("50px","Você perdeu",50,150)
    quadrado(75,300,250,50,"lightgray");
    texto("40px","Recomeçar",100,340)
    texto("20px","Melhor pontuação: " + melhor_pontuacao.toString(),100,200);
    texto("20px","Sua pontuação: " + pontuacao.toString(),125,225);
}
// class pra criar o carro
class Carro {
    x = 0;
    y = 0;
    a = 0;
    l = 0;
    cor = "red";
    imgcarro = document.getElementById("c0");
    // receber o valor inicial dos carros
    constructor(x,y,a,l,cor,imgcarro) {
        this.x = x;
        this.y = y;
        this.a = a;
        this.l = l;
        this.cor = cor;
        this.imgcarro = imgcarro
    }
    desenha() {
        quadrado(this.x,this.y,this.a,this.l,this.cor);
    }
    imagem() {
        ctx.drawImage(this.imgcarro,this.x,this.y,this.a,this.l);
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
let jogador = new Carro(180,400,30,70,"gray", c0);
let imagens = [c1,c2,c3,c4,c5,c6,c7];
let cenarios = [];
// criar lista pra armazenar os outros carros
let lista = [];
// criar os outros carros (Azuis) e armazenar na lista
for(let i = 0; i < 3; i++){
    cenarios.push(new Carro(0,(-600)*i,400,600,"gray"));
}
for(let i = 0; i < 15; i++){
   lista.push(new Carro(Math.floor(Math.random()*360), -100 - (100*i), 30, 60, "blue",imagens[Math.floor(Math.random()*7)]));
}
// criar variavel pra tela do jogo
let tela = 0;
// criar variavel pra pontuacão do jogo
let pontuacao = 0, melhor_pontuacao = 0;
// atualizacao dos frames
function animacao(){
    ctx.clearRect(0,0,400,600);
    if(tela == 0){
        // tela 1 do jogo (inicio)
        pontuacao = 0;
        inicio();
    }
    if(tela == 1){
        // tela 2 do jogo (Jogo)
        // cenario do jogo
        for(let i = 0; i < cenarios.length; i++){
            cenarios[i].cenario();
            cenarios[i].andar();
            if(cenarios[i].y >= 600){
                cenarios[i].y = -1200
            }
        }
        // impedir que o jogador saida da tela
        if(jogador.x < 0){
            jogador.x = 0;
        }
        if(jogador.x > 400-jogador.a){
            jogador.x = 400-jogador.a;
        }
        if(jogador.y < 0){
            jogador.y = 0;
        }
        if(jogador.y > 600 - jogador.l){
            jogador.y = 600 - jogador.l;
        }
        
        // atualizar os outros carros
        for(let i = 0; i < lista.length; i++){
            lista[i].imagem();
            lista[i].andar();
            // verificar se o jogador tocou nos carros
            if(jogador.x + jogador.a >= lista[i].x && jogador.x <= lista[i].x && jogador.y <= lista[i].y + lista[i].l && jogador.y + jogador.l >= lista[i].y){
                tela = 2;
                if(melhor_pontuacao < pontuacao) {
                    melhor_pontuacao = pontuacao;
                }        
            }

            if(jogador.x <= lista[i].x + lista[i].a && jogador.x >= lista[i].x && jogador.y <= lista[i].y + lista[i].l && jogador.y + jogador.l >= lista[i].y){
                if(melhor_pontuacao < pontuacao) {
                    melhor_pontuacao = pontuacao;
                }        
                tela = 2;
            }
            // Reposiciona os carros para deixar o jogo funcionando em loop
            if(lista[i].y >= 600){
                lista[i].x = Math.floor(Math.random()*(400-lista[i].a))
                lista[i].y = -(100*(lista.length-6));
                lista[i].imgcarro = imagens[Math.floor(Math.random()*7)]
            }
        }
        // atualizar o jogador
        jogador.imagem();
        texto("20px","Sua pontuação: " + pontuacao.toString(),0,20);
        if(tela != 2){
            pontuacao++;
        }
    }
    if(tela == 2){
        // tela 3 do jogo (fim)
        final(melhor_pontuacao,pontuacao);
    }
    requestAnimationFrame(animacao);
}
animacao();
// Recebe as teclas que o usuarios esta pressionando

document.addEventListener("keydown",function(evento){
    tecla = evento.key;
    if(tecla == "w" || tecla == "W" || tecla == "ArrowUp"){
        jogador.y -= 10;
    }
    if(tecla == "s" || tecla == "S" || tecla == "ArrowDown"){
        jogador.y += 10;
    }
    if(tecla == "a" || tecla == "A" || tecla == "ArrowLeft"){
        jogador.x -= 10;
    }
    if(tecla == "d" || tecla == "D" || tecla == "ArrowRight"){
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
        pontuacao = 0
        jogador.x = 180;
        jogador.y = 400;
        for(let i = 0; i < lista.length; i++){
            lista[i].y = -100 - (100*i);
            lista[i].x = Math.floor(Math.random()*(400-lista[i].a));
            lista[i].imgcarro = imagens[Math.floor(Math.random()*7)];
        }
        for(let i = 0; i < 3; i++){
            cenarios[i].y = (-600)*i;
        }
    }
});