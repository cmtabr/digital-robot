// Essa função atualiza os valores finais do gráfico somando os valores do eixo X, Y, Z e R.
function updateFinalValues() {
    // Seleciona os elementos de texto dos eixos X, Y, Z e R.
    const inputs = ['#x', '#y', '#z', '#r'];
    // Seleciona os elementos de texto dos valores finais dos eixos X, Y, Z e R.
    const finals = ['#last_x', '#last_y', '#last_z', '#last_r'];

    // Percorre os elementos de texto dos eixos e soma seus valores aos valores finais correspondentes.
    inputs.forEach((input, i) => {
        const inputVal = parseInt($(input).text());
        const finalVal = parseInt($(finals[i]).text()) + inputVal;
        $(finals[i]).text(finalVal);
    });
}

// Essa função envia os valores finais atualizados para o servidor através de uma requisição AJAX.
function sendUpdatedValuesToServer() {
    // Seleciona os elementos de texto dos valores finais dos eixos X, Y, Z e R.
    const finalVals = ['#last_x', '#last_y', '#last_z', '#las'];

    // Cria um objeto com os valores finais de cada eixo.
    const data = finalVals.reduce((acc, curr) => {
        acc[curr.slice(1)] = parseInt($(curr).text());
        return acc;
    }, {});

    // Realiza uma requisição AJAX POST para enviar os dados para o servidor.
    $.ajax({
        url: '/data',
        type: 'POST',
        data: data,
        success: function(response) {
            alert('Dados enviados com sucesso!');
            location.reload();
        },
        error: function(xhr, status, error) {
            alert('Erro ao enviar dados: ' + error);
            location.reload();
        }
    });
}

$(document).ready(function() {
    // Chama a função que atualiza os valores finais quando a página é carregada.
    updateFinalValues();

    // Adiciona um listener de clique no botão de atualização.
    $('#update').click(function() {
        // Chama a função que atualiza os valores finais e envia os dados para o servidor.
        updateFinalValues();
        sendUpdatedValuesToServer();
    });
});