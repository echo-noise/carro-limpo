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

// serializadores
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

function transacaoSerialize(item) { 
    var transacao = {
        "value": item.value,
        "description": item.description,
        "type": item.type
    }
    return transacao;
}

function faturaSerialize(select) {
    var flag;
    if (select.val() == "PAGO") { flag = true; console.log(flag);} 
    else { flag = false; }

    console.log(flag);

    var fatura = { "pago": flag };

    return fatura;

}

// posts
function ajaxPost(data, url) {
    var objID;
    $.ajax({
        type: 'POST',
        url: url,
        async: false,
        dataType: 'json',
        headers: {'X-CSRFToken': getToken() },
        data: data,
        success: function (response) {
            objID = response['object'];
            if(!response['error']) {
                if($("tr#edit")) {
                  $("tr#edit").attr("data-id", response['id']);
                  $("tr#edit").removeAttr("id");
                }
            }
        },
        error: function(response) { 
            console.log(response['responseJSON']['message']); 
            alert(response['responseJSON']['user_alert']);
        } 
    });
    return objID;
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

// gets
function getCaixa() {
    var data = [];
    $.ajax({
        type: "GET",
        url: "get/",
        async: false,
        success: function(response) { data = response; },
        error: function(response) { alert("Erro ao recuperar dados do caixa"); }

    });
    return data;
}

function caixaDeleteAll() {
        $.ajax({
        type: "POST",
        url: "deleteall/",
        headers: {'X-CSRFToken': getToken() },
        success: function(response) { alert(response['message']); },
        error: function(response) { alert(response['message']);}
    });
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
                    $("#status_tabela").html("PAGO");
                    $("#status_tabela").toggleClass("badge-soft-warning badge-soft-primary");
                },
        error: function(response) { 
                    console.log(response['message']); 
                    alert("Erro ao gerar fatura. O caixa está aberto?");
                }
    });
}
