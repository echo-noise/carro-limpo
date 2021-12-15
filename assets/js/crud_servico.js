$(document).ready(function(){
	var actions = $("table td:last-child").html();
	// Tabela com adicionar, editar e remover ao formulario
    $(".add-new-servico").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody  tr:last-child").index();
        var row = '<tr data-id=-1 id="edit" >' +
            '<td data-label="NOME"><input type="text" scope="col" class="form-control-crud" name="servico" id="servico" maxlength="20" >Serviço</td>' +
			'<td data-label="VALOR"><input type="number" lang="pt" step="0.01" scope="col" class="form-control-crud"  name="valor" id="valor" maxlength="14">Valor</td>' +
			'<td>' + actions + '</td>' +
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
			        		"valor": $("td[data-label='VALOR']").children('input').eq(0).val(),
			        	},
			        	success: function (response) {
			        		if(!response['error']) {
			        		    console.log(response['message']);

			        			item.attr("data-id", response['id']);
			        			item.removeAttr("id");
			        		}
			        	},
			        	error: function(response) { console.log(response['message']); } 
			        });
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
				if(!($("tr#edit").attr("data-id") == -1)) {
				    $.ajax({
				    	type: "POST",
				    	url: "delete/" + $(this).parents("tr").attr("data-id"),
				    	success: function(response) { console.log(response['message']); },
				    	error: function(response) { console.log(response['message']);}
				    });
			    }
						$(this).parents("tr").remove();
				$(".add-new-servico").removeAttr("disabled");
				});
		});