function updateFinalValues() {
    const inputs = ['#x', '#y', '#z', '#r'];
    const finals = ['#x_final', '#y_final', '#z_final', '#r_final'];

    inputs.forEach((input, i) => {
        const inputVal = parseInt($(input).text());
        const finalVal = parseInt($(finals[i]).text()) + inputVal;
        $(finals[i]).text(finalVal);
    });
}

function sendUpdatedValuesToServer() {
    const finalVals = ['#x_final', '#y_final', '#z_final', '#r_final'];
    const data = finalVals.reduce((acc, curr) => {
        acc[curr.slice(1)] = parseInt($(curr).text());
        return acc;
    }, {});

    $.ajax({
        url: '/data',
        type: 'POST',
        data: data,
        success: function(response) {
            alert('Texto enviado com sucesso!');
            location.reload();
        },
        error: function(xhr, status, error) {
            alert('Erro ao enviar texto: ' + error);
            location.reload();
        }
    });
}

$(document).ready(function() {
    updateFinalValues();

    $('#update').click(function() {
        updateFinalValues();
        sendUpdatedValuesToServer();
    });
});