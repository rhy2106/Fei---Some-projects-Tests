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
server.listen(3000);

console.log("servidor rodando...")

let user = "";
let senha = "";

app.get("/", function(entrada, saida){
    saida.redirect("project.html");
});

app.get("/cadastra", function(entrada, saida){
    saida.redirect("cadastro.html");
});

app.get("/login", function(entrada, saida){
    saida.redirect("login.html");
});

app.post("/cadastrar_usuario", function(req, resp) {

    // salva dados no banco
    client.db("exemplo_bd").collection("usuarios").insertOne(
    { db_nome: req.body.nome, db_login: req.body.login, db_senha: req.body.senha }, function (err) {
        if (err) {
            resp.render('resposta_usuario', {resposta: "Erro ao cadastrar usuário!"})
        }else {
            resp.render('resposta_usuario', {resposta: "Usuário cadastrado com sucesso!"})       
        };
    });
 
});

app.post("/logar_usuario", function(req, resp) {

    // busca um usuário no banco de dados
    client.db("exemplo_bd").collection("usuarios").find(
    {db_login: req.body.login, db_senha: req.body.senha}).toArray(function(err, items) {
        console.log(items);
        if (items.length == 0) {
          resp.render('resposta_usuario', {resposta: "Usuário/senha não encontrado!"})
        }else if (err) {
          resp.render('resposta_usuario', {resposta: "Erro ao logar usuário!"})
        }else {
          resp.render('resposta_usuario', {resposta: "Usuário logado com sucesso!"})       
        };
    });
 
});

app.post("/deletar_usuario", function(req, resp) {

    client.db("exemplo_bd").collection("usuarios").deleteOne(
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
    client.db("exemplo_bd").collection("usuarios").updateOne(
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
 
app.get("/blog", function(entrada, saida){
    client.db("exemplo_bd").collection("blog").find(
        {}).toArray(function(err, lista) {
            console.log(lista);
            saida.render("blog.ejs", {lista});
        });
});

app.get("/criar", function(entrada,saida){
    saida.render("blog_post");
});

app.post("/criar_post", function(req, resp) {

    // salva dados no banco
    client.db("exemplo_bd").collection("blog").insertOne(
    { titulo: req.body.titulo, resumo: req.body.resumo, mensagem: req.body.mensagem}, function (err) {
        if (err) {
            resp.render('resposta_blog', {resposta: "Erro ao cadastrar o post"})
        }else {
            resp.render('resposta_blog', {resposta: "Post Cadastrado"})       
        };
    });
 
});