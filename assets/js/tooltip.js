$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
  $('[data-toggle="tooltip"]').on("click", function () {
    $(this).tooltip("hide");
  });
});
