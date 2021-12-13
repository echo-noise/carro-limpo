$(document).ready(function(){
	var actions = $("table td:last-child").html();
	// Tabela com adicionar, editar e remover ao formulario
    $(".add-new").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody  tr:last-child").index();
        var row = '<tr data-id=-1 id="edit">' +
            '<td data-label="NOME"><input type="text" scope="col" class="form-control-crud" id="nome" name="nome" maxlength="20" >Nome</td>' +
			'<td data-label="TELEFONE"><input type="text" scope="col" class="form-control-crud"  name="telefone" maxlength="14"  id="telefone">Telefone</td>' +
			'<td data-label="E-MAIL"><input type="email" scope="col" class="form-control-crud" name="email" maxlength="20" id="email">E-mail</td>' +
			'<td data-label="CPF/CNPJ"><input type="text" scope="col" class="form-control-crud" name"cpf_cnpj" maxlength="14" id="cpf_cnpj">CPF/CNPJ</td>' +
			'<td data-label="PLACA"><input type="text" scope="col" class="form-control-crud" name="placa" maxlength="7" id="placa">Placa</td>' +
			'<td data-label="MARCA"><select class="form-control-crud" scope="col"  name="marca" id="marca"><option selected ></option><option value="Fiat">Fiat</option><option value="Volkswagen">Volkswagen</option><option value="GM">GM</option><option value="Hyundai">Hyundai</option><option value="Jeep">Jeep</option><option value="Renault">Renault</option><option value="Toyota">Toyota</option><option value="Ford">Ford</option><option value="Honda">Honda</option><option value="Nissan">Nissan</option><option value="Caoa Chery">Caoa Chery</option><option value="Peugeot">Peugeot</option><option value="Mitsubishi">Mitsubishi</option><option value="Citroen">Citroen</option><option value="BMW">BMW</option><option value="Volvo">Volvo</option><option value="Mercedes">Mercedes</option><option value="Audi">Audi</option><option value="Kia">Kia</option><option value="RAM">RAM</option><option value="Iveco">Iveco</option><option value="Land Rover">Land Rover</option><option value="Porsche">Porsche</option><option value="Suzuki">Suzuki</option><option value="Mini">Mini</option><option value="JAC">JAC</option><option value="Troler">Troler</option><option value="Subaru">Subaru</option><option value="Jaguar">Jaguar</option><option value="Dodge">Dodge</option><option value="Foton">Foton</option><option value="Lexus">Lexus</option></select>Marca</td>' +
			'<td data-label="MODELO"><input type="text"   scope="col" class="form-control-crud" maxlength="10" name="modelo" id="modelo">Modelo</td>' +
			'<td data-label="COR"><select class="form-control-crud" id="cor" scope="col" name="cor"><option selected ></option><option value="Preto" >Preto</option><option value="Branco" >Branco</option><option value="Prata" >Prata</option><option value="Cinza" >Cinza</option><option value="Vermelho" >Vermelho</option><option value="Azul" >Azul</option><option value="Marrom" >Marrom</option><option value="Verde" >Verde</option><option value="Bege" >Bege</option><option value="Amarelo">Amarelo</option></select>Cor</td>' +
			
			// '<td><select class="form-control-crud" id="servicos" scope="col" name="servicos"><option selected ></option><option value="Limpeza ecológica" >Limpeza ecológica</option><option value="Enceramento" >Enceramento</option><option value="Higienização interna" >Higienização interna</option><option value="Cristalização de vidros" >Cristalização de vidros</option><option value="Limpeza técnica de motor" >Limpeza técnica de motor</option><option value="lavagem" >Lavagem</option></select>Serviços</td>' +
			
			// '<td><input type="text" scope="col" class="form-control-crud" name"observacoes" maxlength="10" id="observacoes">Observações</td>' +


			'<td>' + actions + '</td>' +
        '</tr>';
				$("table").append(row);		
				$("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
				});
			// Botao Adicionar
			$(document).on("click", ".add", function(){
				var empty = false;
				var input = $(this).parents("tr").find('input[type="text"], [type="number"], [type="email"], [name="servicos"], [name="marca"], [id="cor"]');
				input.each(function(){
				    if(!$(this).val()){
				    	$(this).addClass("error");
				    	empty = true;
				    } else {
				    	$(this).removeClass("error");
				    }
				});
				$(this).parents("tr").find(".error").first().focus();
	     	    if(!empty){
						var item = $("tr#edit");
						var item_id = $("tr#edit").attr("data-id");

	     				if($("tr#edit").attr("data-id") == -1) { var _url = "insert";  } 
						else { var _url = "update/" + item_id; }

				        $.ajax({
				        	type: 'POST',
				        	url: _url,
				        	dataType: 'json',
				        	data: { 
				        		"nome": $("td[data-label='NOME']").children('input').eq(0).val(),
				        		"documento": $("td[data-label='CPF/CNPJ']").children('input').eq(0).val(),
				        		"telefone": $("td[data-label='TELEFONE']").children('input').eq(0).val(),
				        		"email": $("td[data-label='E-MAIL']").children('input').eq(0).val(),
				        		"cor": $("td[data-label='COR']").children('input').eq(0).val(),
				        		"modelo": $("td[data-label='MODELO']").children('input').eq(0).val(),
				        		"marca": $("td[data-label='MARCA']").children('input').eq(0).val(),
				        		"placa": $("td[data-label='PLACA']").children('input').eq(0).val()
				        	},
				        	success: function (response) {
				        		if(!response['error']) {
				        		    console.log(response['message']);
				                    input.each(function(){
				                    	$(this).parent("td").html($(this).val());
				                    });			
				                    $(this).parents("tr").find(".add, .edit").toggle();

				        			item.attr("data-id", response['id']);
				        			item.removeAttr("id");

				                    $(".add-new").removeAttr("disabled");
				        		}
				        	},
				        	error: function(response) { console.log(response['message']); } 
				        });
			    }
				});
			// Botao Editar
			$(document).on("click", ".edit", function(){		
				        $(this).parents("tr").attr("id", "edit");
						$(this).parents("tr").find("td:not(:last-child)").each(function(){
					        $(this).html('<input type="text" class="form-control-crud" value="' + $(this).text() + '">');
						});		
				$(this).parents("tr").find(".add, .edit").toggle();
				$(".add-new").attr("disabled", "disabled");
				});
			// Botao Deletar
			$(document).on("click", ".delete", function(){
				if(!($("tr#edit").attr("data-id") == -1)) {
				    $.ajax({
				    	type: "POST",
				    	url: "delete/" + $(this).parents("tr").attr("data-id"),
				    	success: function(response) { console.log(response['message']); },
				    	error: function(response) { console.log(response['message']);}
				    });
			    }
			    $(this).parents("tr").remove();
				$(".add-new").removeAttr("disabled");
				});
		});