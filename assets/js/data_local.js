  $(document).ready(function(){
    $(".datetime").each(function(){
      var dateStr = $(this).html();
      var dateObj = new Date(parseInt(dateStr) * 1000);
      var formatted = new Intl.DateTimeFormat(undefined, { dateStyle: "short", timeStyle: "short" }).format(dateObj);
      $(this).html(formatted);
    });
    $(".date").each(function(){
        var dateStr = $(this).html();
        var dateObj = new Date(parseInt(dateStr) * 1000);
        var formatted = new Intl.DateTimeFormat(undefined, { dateStyle: "short"}).format(dateObj);
        $(this).html(formatted);
    });
  });