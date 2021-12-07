var minDate, maxDate;
 
// Custom filtering function which will search data in column four between two values
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = minDate.val();
        var max = maxDate.val();

        
        var date = new Date( data[4] );
 
        if (
            ( min === null && max === null ) ||
            ( min === null && date <= max ) ||
            ( min <= date   && max === null ) ||
            ( min <= date   && date <= max )
        ) {
            return true;
        }
        return false;
    }
);
 
$(document).ready(function() {
    // Create date inputs
    minDate = new DateTime($('.min'), {
        format: 'DD/MM/YYYY'
    });
    maxDate = new DateTime($('.max'), {
        format: 'DD/MM/YYYY'
    });
 
      var table = $('.form-data').DataTable();
 
      // Add event listeners to the two range filtering inputs
      $('.min').keyup( function() { table.draw(); } );
      $('.max').keyup( function() { table.draw(); } );
  } );
