class Values {
    constructor(inputs, finals) {
        this.inputs = inputs;
        this.finals = finals;
    }

    updateFinalValues() {
        this.inputs.forEach((input, i) => {
        const inputVal = parseInt($(input).text());
        const finalVal = parseInt($(this.finals[i]).text()) + inputVal;
        $(this.finals[i]).text(finalVal);
        });
    }

    sendUpdatedValuesToServer() {
        const data = this.finals.reduce((acc, curr) => {
            acc[curr.slice(1)] = parseInt($(curr).text());
            return acc;
        }, {});

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

    init() {
        this.updateFinalValues();
        $('#update').click(() => {
            this.updateFinalValues();
            this.sendUpdatedValuesToServer();
        });
    }
}

class App {
    constructor() {
        this.Values = new Values(
            ['#x', '#y', '#z'],
            ['#last_x', '#last_y', '#last_z']
        );
    }

    init() {
        this.Values.init();
    }
}

$(document).ready(() => {
    const app = new App();
    app.init();
});
