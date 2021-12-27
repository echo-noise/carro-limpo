function getUrl() {
	var item_id = $("tr#edit").attr("data-id");

	if($("tr#edit").attr("data-id") == -1) { var _url = "insert";  } 
	else { var _url = "update/" + item_id; }

    return _url;
}

function getToken() {
    let cookie = document.cookie;
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1);

    return csrfToken;
}

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

function servicoSerialize() {
    var servico = {
    "nome": $("td[data-label='NOME']").children().first().val(),
    "valor": $("td[data-label='VALOR']").children().first().val()
    };
    return servico;
}

function clienteSerialize() {
    var cliente = {
							"nome": $("td[data-label='NOME']").children().first().val(),
							"telefone": $("td[data-label='TELEFONE']").children().first().val(),
							"email": $("td[data-label='E-MAIL']").children().first().val(),
							"documento": $("td[data-label='CPF/CNPJ']").children().first().val(),
							"placa": $("td[data-label='PLACA']").children().first().val(), 
							"marca": $("td[data-label='MARCA']").children().first().val(),
							"modelo": $("td[data-label='MODELO']").children().first().val(),
							"cor": $("td[data-label='COR']").children().first().val(),
						};
    return cliente;
}

function ajaxPost(data) {
    $.ajax({
        type: 'POST',
        url: getUrl(),
        dataType: 'json',
        headers: {'X-CSRFToken': getToken() },
        data: data,
        success: function (response) {
            if(!response['error']) {
                console.log(response['message']);

                $("tr#edit").attr("data-id", response['id']);
                $("tr#edit").removeAttr("id");
            }
        },
        error: function(response) { console.log(response['message']); } 
    });
}

function ajaxDelete(id){
    $.ajax({
        type: "POST",
        url: "delete/" + id,
        headers: {'X-CSRFToken': getToken() },
        success: function(response) { console.log(response['message']); },
        error: function(response) { console.log(response['message']);}
    });
}