$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	var actions = $("table td:last-child").html();
	// Tabela com adicionar, editar e remover ao formulario
    $(".add-new").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody  tr:last-child").index();
        var row = '<tr>' +
            '<td><input type="text" scope="col" class="form-control" name="nome" id="nome" maxlength="20" >Nome</td>' +
         
						'<td><input type="text" scope="col" class="form-control"  name="telefone" maxlength="14"  id="telefone">Telefone</td>' +
         
						'<td><input type="email" scope="col" class="form-control" name="email" maxlength="20" id="email">E-mail</td>' +
					
						'<td><input type="text" scope="col" class="form-control" name"cpf_cnpj" maxlength="14" id="cpf_cnpj">CPF/CNPJ</td>' +
					
						'<td><input type="text" scope="col" class="form-control" name="placa" maxlength="7" id="placa">Placa</td>' +
					
						'<td><select class="form-control" scope="col"  name="marca"><option selected ></option><option value="Fiat">Fiat</option><option value="Volkswagen">Volkswagen</option><option value="GM">GM</option><option value="Hyundai">Hyundai</option><option value="Jeep">Jeep</option><option value="Renault">Renault</option><option value="Toyota">Toyota</option><option value="Ford">Ford</option><option value="Honda">Honda</option><option value="Nissan">Nissan</option><option value="Caoa Chery">Caoa Chery</option><option value="Peugeot">Peugeot</option><option value="Mitsubishi">Mitsubishi</option><option value="Citroen">Citroen</option><option value="BMW">BMW</option><option value="Volvo">Volvo</option><option value="Mercedes">Mercedes</option><option value="Audi">Audi</option><option value="Kia">Kia</option><option value="RAM">RAM</option><option value="Iveco">Iveco</option><option value="Land Rover">Land Rover</option><option value="Porsche">Porsche</option><option value="Suzuki">Suzuki</option><option value="Mini">Mini</option><option value="JAC">JAC</option><option value="Troler">Troler</option><option value="Subaru">Subaru</option><option value="Jaguar">Jaguar</option><option value="Dodge">Dodge</option><option value="Foton">Foton</option><option value="Lexus">Lexus</option></select>Marca</td>' +
            
						'<td><input type="text"   scope="col" class="form-control" maxlength="10" name="modelo" id="modelo">Modelo</td>' +
						
						'<td><select class="form-control" id="cor" scope="col" name="cor"><option selected ></option><option value="Preto" >Preto</option><option value="Branco" >Branco</option><option value="Prata" >Prata</option><option value="Cinza" >Cinza</option><option value="Vermelho" >Vermelho</option><option value="Azul" >Azul</option><option value="Marrom" >Marrom</option><option value="Verde" >Verde</option><option value="Bege" >Bege</option><option value="Amarelo">Amarelo</option></select>Cor</td>' +
						
						'<td><select class="form-control" id="servicos" scope="col" name="servicos"><option selected ></option><option value="Limpeza ecológica" >Limpeza ecológica</option><option value="Enceramento" >Enceramento</option><option value="Higienização interna" >Higienização interna</option><option value="Cristalização de vidros" >Cristalização de vidros</option><option value="Limpeza técnica de motor" >Limpeza técnica de motor</option><option value="lavagem" >Lavagem</option></select>Serviços</td>' +
						
						'<td><input type="text" scope="col" class="form-control" name"observacoes" maxlength="10" id="observacoes">Observações</td>' +


			'<td>' + actions + '</td>' +
        '</tr>';
				$("table").append(row);		
				$("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
						$('[data-toggle="tooltip"]').tooltip();
				});
			// Botao Adicionar
			$(document).on("click", ".add", function(){
				var empty = false;
				var input = $(this).parents("tr").find('input[type="text"], [type="number"], [type="email"], [name="servicos"], [name="marca"], [id="cor"]');
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
					$(".add-new").removeAttr("disabled");
				}		
				});
			// Botao Editar
			$(document).on("click", ".edit", function(){		
						$(this).parents("tr").find("td:not(:last-child)").each(function(){
					$(this).html('<input type="text" class="crud form-control" value="' + $(this).text() + '">');
					
				});		
				$(this).parents("tr").find(".add, .edit").toggle();
				$(".add-new").attr("disabled", "disabled");
				});
			// Botao Deletar
			$(document).on("click", ".delete", function(){
						$(this).parents("tr").remove();
				$(".add-new").removeAttr("disabled");
				});
		});