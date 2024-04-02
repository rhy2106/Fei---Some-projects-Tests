let resposta = Math.floor(Math.random()*100);
function adivinhar(){
    var x = parseInt(document.getElementById("e1").value);
    if(x == resposta){
        document.getElementById("r1").innerHTML = "número igual";
        document.getElementById("r1").style.backgroundColor = "green";
    }
    else{
        document.getElementById("r1").innerHTML = "número errado";
        document.getElementById("r1").style.backgroundColor = "red";
        if(x > resposta){
            document.getElementById("grande").innerHTML = x;
        } else {
            document.getElementById("pequeno").innerHTML = x;
        }
    }
    return 0;
}
