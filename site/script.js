function soma(){
    let num1 = parseInt(document.getElementById("e1").value);
    let num2 = parseInt(document.getElementById("e2").value);
    document.getElementById("r1").innerHTML = "A soma é " + (num1 + num2);
}
function aleatorio(){
    var lista = [];
    for(let i = 0; i < 50; i++){
        lista[i] = i + 1;
    }
    var indiceAleatorio = Math.floor(Math.random() * lista.length);
    var elementoAleatorio = lista[indiceAleatorio];
    document.getElementById("r2").innerHTML = "O número gerado foi " + elementoAleatorio;
}
function bom(){
    let num1 = parseInt(document.getElementById("e3").value);
    if(num1 < 10){
        document.getElementById("r3").innerHTML = "Insuficiente";
    } else if(num1 < 15){
        document.getElementById("r3").innerHTML = "Bom";
    } else{
        document.getElementById("r3").innerHTML = "Muito Bom";
    }
}

var nome = '';
var login = '';
var senha = '';
function cadastro(){
    if(nome !== ''|| login !== '' || senha !== ''){
        document.getElementById("r4").innerHTML = "Já existe um cadastro. Por favor, limpe os dados para se cadastrar";
    } else{
        nome = document.getElementById("e4");
        login = document.getElementById("e5");
        senha = document.getElementById("e6");
        document.getElementById("r4").innerHTML = "Cadastro realizado com sucesso";
    }
}
function limpar(){
    nome = '';
    login = '';
    senha = '';
    document.getElementById("e4").value = '';
    document.getElementById("e5").value = '';
    document.getElementById("e6").value = '';
    document.getElementById("r4").innerHTML = '';
}
function dados(){
    if(nome !== ''|| login !== ''|| senha !== ''){
        alert("Nome: " + nome.value + "\nLogin: " + login.value);
    } else{
        document.getElementById("r4").innerHTML = "Nenhum dado cadastrado"
    }
}
function logar(){
    let login1 = document.getElementById("e7");
    let senha1 = document.getElementById("e8");
    if(senha.value !== senha1.value || login.value !== login1.value){
        document.getElementById("r5").innerHTML = "Login ou senha invalida";
    } else{
        document.getElementById("r5").innerHTML = "Login realizado com sucesso";
    }
}