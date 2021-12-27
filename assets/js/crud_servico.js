$(document).ready(function(){
	var actions =  '<div class="acoes-align">' 
	+ '<a class="add" title="Salvar" data-toggle="tooltip"><i class="material-icons" >&#xE03B;</i></a>'
	+ '<a class="edit" title="Editar" data-toggle="tooltip"><i class="material-icons">&#xE254;</i></a>'
	+ '<a class="delete" title="Apagar" data-toggle="tooltip"><i class="material-icons">&#xE872;</i></a>'
    + '</div>'
	// Tabela com adicionar, editar e remover ao formulario
    $(".add-new-servico").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody  tr:last-child").index();
        var row = '<tr data-id=-1 id="edit" >' +
            '<td data-label="NOME"><input type="text" scope="col" class="form-control-crud" name="servico" id="servico" maxlength="20" >Serviço</td>' +
			'<td data-label="VALOR"><input type="number" lang="pt" step="0.01" scope="col" class="form-control-crud"  name="valor" id="valor" maxlength="14">Valor</td>' +
			'<td data-label="AÇOES">' + actions + '</td>' +
            '</tr>';
				$("table").append(row);		
				$("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
				});
			// Botao Adicionar
			$(document).on("click", ".add", function(){
				var empty = false;
				var input = $(this).parents("tr").find('input[type="text"], [type="number"], [id="servico"], [id="valor"]');
						input.each(function(){
					if(!$(this).val()){
						$(this).addClass("error");
						empty = true;
					} else{
						$(this).removeClass("error");
					}
				});
				$(this).parents("tr").find(".error").first().focus();
				if(!empty){
					ajaxPost(servicoSerialize());

					input.each(function(){
						$(this).parent("td").html($(this).val());
					});			
					$(this).parents("tr").find(".add, .edit").toggle();
					$(".add-new-servico").removeAttr("disabled");
				}		
				});
			// Botao Editar
			$(document).on("click", ".edit", function(){		
				        $(this).parents("tr").attr("id", "edit");
						var textField = $(this).parents("tr").children('td').eq(0);
						var numberField = $(this).parents("tr").children('td').eq(1)
						textField.html('<input type="text" class="form-control-crud" value="' + textField.text() + '">');
						numberField.html('<input type="number" step="0.01" lang="pt" class="form-control-crud" value="' + numberField.text().replace(",", ".") + '">');
					//	$(this).parents("tr").find("td:not(:last-child)").each(function(){
				//	$(this).html('<input type="text" class="form-control-crud" value="' + $(this).text() + '">');	
				//});	
				// 	$(this).parents("tr").find(".valor").each(function(){
				// 		$(this).html('<input type="text" class="form-control-crud" value="' + $(this).text() + '">');	
					
				// });		
				$(this).parents("tr").find(".add, .edit").toggle();
				$(".add-new-servico").attr("disabled", "disabled");
				});
			// Botao Deletar
			$(document).on("click", ".delete", function(){
				var id = $(this).parents("tr").attr("data-id");
				if(!(id == -1)) {
					ajaxDelete(id);
			    }
				$(this).parents("tr").remove();
				$(".add-new-servico").removeAttr("disabled");
				});
		});