// controllers/rankingController.js

const fs = require('fs'); // Módulo para ler arquivos
const path = require('path');

// Função para ler os dados do ranking persistidos pelo jogo Python
const getRankingFromPersistence = () => {
    // ⚠️ Se o seu código Python salvasse a AVL em JSON,
    // o caminho seria algo como:
    const persistencePath = path.join(__dirname, '..', 'data', 'ranking.json');

    try {
        if (fs.existsSync(persistencePath)) {
            const data = fs.readFileSync(persistencePath, 'utf8');
            // Assumimos que o JSON tem um array de objetos de jogador
            return JSON.parse(data);
        }
    } catch (error) {
        console.error("Erro ao ler os dados do ranking:", error);
    }

    // Retorna dados simulados ou vazios em caso de erro/arquivo ausente
    return [
        { nome_jogador: "Seraphim", pontuacao_recorde: 5200, record_eventos: 45, chefes_derrotados: 5, total_avls: 3, contador_mortes: 2 },
        { nome_jogador: "Dreadnought", pontuacao_recorde: 4850, record_eventos: 38, chefes_derrotados: 4, total_avls: 4, contador_mortes: 1 },
        { nome_jogador: "VoidWalker", pontuacao_recorde: 3100, record_eventos: 22, chefes_derrotados: 2, total_avls: 2, contador_mortes: 1 },
        { nome_jogador: "Spectre", pontuacao_recorde: 2500, record_eventos: 18, chefes_derrotados: 1, total_avls: 1, contador_mortes: 0 },
        { nome_jogador: "Rato", pontuacao_recorde: 100, record_eventos: 1, chefes_derrotados: 0, total_avls: 1, contador_mortes: 1 },
    ];
};

exports.getRankingPage = (req, res) => {
    const rankingData = getRankingFromPersistence();
    
    // Os dados são classificados e passados para a View (EJS)
    res.render('ranking/index', {
        pageTitle: 'Ranking de Sobreviventes',
        ranking: rankingData.sort((a, b) => b.pontuacao_recorde - a.pontuacao_recorde),
    });
};