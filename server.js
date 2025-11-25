// server.js

const express = require('express');
const path = require('path'); // Módulo para trabalhar com caminhos
const app = express();
const PORT = 3000; // Define a porta do servidor

// --- 1. CONFIGURAÇÃO DO EJS E DIRETÓRIOS ---
// Define o EJS como o motor de visualização
app.set('view engine', 'ejs');
// Informa onde estão as views (necessário, já que estamos no diretório raiz)
app.set('views', path.join(__dirname, 'views'));
// Configura a pasta 'public' para servir arquivos estáticos (CSS, imagens, etc.)
app.use(express.static(path.join(__dirname, 'public')));


// --- 2. IMPORTAÇÃO DE ROTAS ---
// Importa a nova rota de ranking que criamos
const rankingRoutes = require('./routes/rankingRoutes');
// Você deve importar as outras rotas aqui também (clientesRoutes, produtosRoutes, etc.)
// Exemplo: const clientesRoutes = require('./routes/clientesRoutes');


// --- 3. USO DAS ROTAS ---
// Usa a rota de ranking (URL base: /ranking)
app.use('/ranking', rankingRoutes); 

// Adicione suas outras rotas aqui:
// Exemplo: app.use('/clientes', clientesRoutes);


// --- 4. Rota Padrão (Opcional, redireciona a raiz para o ranking ou uma landing page) ---
app.get('/', (req, res) => {
    // Redireciona para a rota que você configurou
    res.redirect('/ranking');
    // Ou renderiza a view raiz: res.render('index', { pageTitle: 'Início' });
});


// --- 5. INICIALIZAÇÃO DO SERVIDOR ---
app.listen(PORT, () => {
    console.log(`✅ Servidor Express iniciado com sucesso!`);
    console.log(`🌐 Acesse o ranking em: http://localhost:${PORT}/ranking`);
});