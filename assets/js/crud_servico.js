$(document).ready(function(){
	var actions = $("table td:last-child").html();
	// Tabela com adicionar, editar e remover ao formulario
    $(".add-new-servico").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody  tr:last-child").index();
        var row = '<tr>' +
            '<td><input type="text" scope="col" class="form-control-crud" name="servico" id="servico" maxlength="20" >Serviço</td>' +
         
						'<td><input type="text" scope="col" class="form-control-crud"  name="valor" id="valor" maxlength="14">Valor</td>' +

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
					input.each(function(){
						$(this).parent("td").html($(this).val());
					});			
					$(this).parents("tr").find(".add, .edit").toggle();
					$(".add-new-servico").removeAttr("disabled");
				}		
				});
			// Botao Editar
			$(document).on("click", ".edit", function(){		
						$(this).parents("tr").find("td:not(:last-child)").each(function(){
					$(this).html('<input type="text" class="form-control-crud" value="' + $(this).text() + '">');	
				});	
				// 	$(this).parents("tr").find(".valor").each(function(){
				// 		$(this).html('<input type="text" class="form-control-crud" value="' + $(this).text() + '">');	
					
				// });		
				$(this).parents("tr").find(".add, .edit").toggle();
				$(".add-new-servico").attr("disabled", "disabled");
				});
			// Botao Deletar
			$(document).on("click", ".delete", function(){
						$(this).parents("tr").remove();
				$(".add-new-servico").removeAttr("disabled");
				});
		});