function gerarFatura(id) {
    $.ajax({
        type: "GET",
        headers: {'X-CSRFToken': getToken() },
        url: "gerar/" + id,
        success: function(response) { 
                    console.log(response); 
                    $("#fatura_id").html(id);
                    $("#loja_rs").html(response['loja_rs']);
                    $("#loja_tel").html(response['loja_tel']);
                    $("#loja_email").html(response['loja_email']);
                    $("#loja_cnpj").html(response['loja_cnpj']);
                    $("#loja_endereco").html(response['loja_endereco']);
                    $("#cliente_nome").html(response['cliente_nome']);
                    $("#cliente_tel").html(response['cliente_tel']);
                    $("#cliente_email").html(response['cliente_email']);
                    $("#cliente_documento").html(response['cliente_documento']);
                    $("#cliente_marca").html(response['cliente_marca']);
                    $("#cliente_modelo").html(response['cliente_modelo']);
                    $("#cliente_placa").html(response['cliente_placa']);
                    $("#servico_nome").html(response['servico_nome']);
                    $("#servico_valor").html(response['servico_valor']);
                    $("#fatura_valor").html(response['fatura_valor']);
                    $("#fatura_data").html(response['fatura_data']);
                    $("#fatura_status").html(response['fatura_status']);
                    $("#status_tabela").html("Pago");
                },
        error: function(response) { 
                    console.log(response['message']); 
                    alert("Erro ao gerar fatura");
                }
    });
}