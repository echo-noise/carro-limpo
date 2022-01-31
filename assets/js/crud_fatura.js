$(document).ready(function () {
  // Tabela editar, atualizar e remover da fatura
  // Botao Adicionar
  $(document).on("click", ".add", function () {
    var empty = false;
<<<<<<< HEAD
    var input = $(this).parents("tr").find("select");
=======
    var id = $(this).parents("tr").attr('data-id');
    var url = "edit/" + id;
    var input = $(this).parents("tr").find("select");
    ajaxPost(faturaSerialize(input), url); 
>>>>>>> testing
    {
      input.each(function () {
        $("select#status_pag")
          .change(function () {
            var _class = $(this).find(":selected").data("class");
            $(this)
              .closest("td")
              .html(
                "<span id='status_pagamento' class='status'> " +
                  $(this).val() +
                  "</span>"
              );
            $(".status").attr("class", "status " + _class);
          })
          .change();
      });
      $(this).parents("tr").find(".add, .edit").toggle();
    }
  });
  // Botao Editar
  $(document).on("click", ".edit", function () {
    $(this)
      .parents("tr")
      .find("td:nth-last-child(10)")
      .each(function () {
        $(this).html(
          '<select id="status_pag" class=" form-control-crud"><option data-class="badge-soft-warning badge badge-boxed" value="PENDENTE" selected>PENDENTE</option><option  data-class="badge-soft-primary badge badge-boxed" value="PAGO">PAGO</option>'
        );
      });

    $(this).parents("tr").find(".add, .edit").toggle();
  });
  // Botao Deletar
  $(document).on("click", ".delete", function () {
    $(this).parents("tr").remove();
  });
});
