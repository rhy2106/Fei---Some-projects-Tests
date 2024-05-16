var mongodb = require("mongodb");
var http = require('http');
var express = require('express');
var bodyParser = require("body-parser")

var app = express();

app.use(express.static('./src'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.set('view engine','ejs');
app.set('views','./views')

const MongoClient = mongodb.MongoClient;

const uri = "mongodb+srv://rhy2106:rafael2106@primeirobd.g0p84f3.mongodb.net/?retryWrites=true&w=majority&appName=primeirobd";
const client = new MongoClient(uri, {useNewUrlParser: true});

var server = http.createServer(app);
server.listen(80);

console.log("servidor rodando...")



app.get("/",function(entrada,saida){
    client.db("exemplo_bd").collection("carros").find().toArray(function(err, items) {
            console.log(items);
       });
    saida.render("home.ejs")
});
app.get("/cadastrar",function(entrada,saida){
    saida.render("cadastro.ejs")
});
app.get("/login", function(entrada, saida){
    saida.render("login.ejs");
});
app.get("/usuario", function(entrada, saida){
    saida.render("usuario.ejs");
});
app.post("/cadastrar_usuario", function(req, resp) {

    // salva dados no banco
    client.db("exemplo_bd").collection("usuarios-carro").insertOne(
    {db_nome: req.body.nome, db_login: req.body.login, db_senha: req.body.senha }, function (err) {
        if (err) {
            resp.render('resposta_usuario', {resposta: "Erro ao cadastrar usuário!"})
        }else {
            resp.render('resposta_usuario', {resposta: "Usuário cadastrado com sucesso!"})       
        };
    });
 
});

app.post("/logar_usuario", function(req, resp) {

    // busca um usuário no banco de dados
    db_login = ""
    client.db("exemplo_bd").collection("usuarios-carro").find(
    {db_login: req.body.login, db_senha: req.body.senha}).toArray(function(err, items) {
        console.log(items);
        if (items.length == 0) {
          resp.render('resposta_usuario', {resposta: "Usuário/senha não encontrado!"})
        }else if (err) {
          resp.render('resposta_usuario', {resposta: "Erro ao logar usuário!"})
        }else {
          resp.render('perfil',{db_login})
        };
    });
 
});

app.post("/deletar_usuario", function(req, resp) {

    client.db("exemplo_bd").collection("usuarios-carro").deleteOne(
    {db_login: req.body.login, db_senha: req.body.senha },function(err,result) {

        if (result.deletedCount == 0) {
            resp.render('resposta_usuario', {resposta: "Usuário/senha não encontrado!"})
        }else if (err) {
            resp.render('resposta_usuario', {resposta: "Erro ao remover usuário!"})
        }else {
            resp.render('resposta_usuario', {resposta: "Usuário removido com sucesso!"})       
        };
       
    });
    
 });

 app.post("/atualizar_usuario", function(req, resp) {

    // atualiza senha do usuário
    client.db("exemplo_bd").collection("usuarios-carro").updateOne(
    { db_login: req.body.login, db_senha: req.body.senha },
    { $set: {db_senha: req.body.novasenha} }, function (err, result) {
        console.log(result);
        if (result.modifiedCount == 0) {
            resp.render('resposta_usuario', {resposta: "Usuário/senha não encontrado!"})
        }else if (err) {
            resp.render('resposta_usuario', {resposta: "Erro ao atualizar usuário!"})
        }else {
            resp.render('resposta_usuario', {resposta: "Usuário atualizado com sucesso!"})       
        };
    });
 
});

app.post("/adicionar_carro", function(req, resp) {

    // salva dados no banco
    db_login = ""
    client.db("exemplo_bd").collection("carros").insertOne(
    {db_login: req.body.db_login, db_preco: req.body.preco, db_carro: req.body.carro, db_status: req.body.status}, function (err) {
        if (err) {
            resp.render('perfil', {db_login,resposta: "Erro ao cadastrar o carro!"})
        }else {
            resp.render('perfil', {db_login,resposta: "Carro cadastrado com sucesso!"})       
        };
    });
 
});

app.post("/atualizar_carro", function(req, resp) {

    // atualiza senha do usuário
    db_login = ""
    client.db("exemplo_bd").collection("carros").updateOne(
    { db_login: req.body.db_login, db_preco: req.body.precoatt, db_carro: req.body.carroatt},
    { $set: {db_status: req.body.statusatt} }, function (err, result) {
        console.log(result);
        if (result.modifiedCount == 0) {
            resp.render('perfil', {db_login,resposta: "Carro não encontrado!"})
        }else if (err) {
            resp.render('perfil', {db_login,resposta: "Erro ao atualizar Carro!"})
        }else {
            resp.render('perfil', {db_login,resposta: "Carro atualizado com sucesso!"})       
        };
    });
 
});

app.post("/deletar_carro", function(req, resp) {

    client.db("exemplo_bd").collection("carros").deleteOne(
    {db_login: req.body.login, db_carro: req.body.carrodel},function(err,result) {

        if (result.deletedCount == 0) {
            resp.render('perfil', {db_login,resposta: "Carro não encontrado!"})
        }else if (err) {
            resp.render('perfil', {db_login,resposta: "Erro ao remover Carro!"})
        }else {
            resp.render('perfil', {db_login,resposta: "Carro removido com sucesso!"})       
        };
       
    });
    
 });