$(document).ready(function() {

var data_list= [];
var columnDefs = [{
title:"rec_ID", visible: false,
searchable:false}, {
  title: "Name"
}
];

var myTable = $('#task').DataTable({
  "sPaginationType": "full_numbers",
  "ajax": {
            "url":"http://10.200.234.215:9000/timesheet/api/task/",
            "type": "GET",
            "data": {"task_id":1}
  },
  columns: columnDefs,
  dom: 'Bfrtip',        // Needs button container
  select: 'single',
  responsive: true,
  altEditor: true,     // Enable altEditor
  "fnCreatedRow": function( nRow, aData, iDataIndex ) {
        $(nRow).attr('id', aData[aData.length-1]);
    },
  buttons: [{
    text: 'Add',
    name: 'add'        // do not change name
  },
  {
    extend: 'selected', // Bind to Selected row
    text: 'Edit',
    name: 'edit'        // do not change name
  },
  {
    extend: 'selected', // Bind to Selected row
    text: 'Delete',
    name: 'delete'      // do not change name
 }]

});
$('#altEditor-modal').on('click', '#addRowBtn', function(e){
    $.ajax({
        'url': "http://10.200.234.215:9000/timesheet/api/task/",
        'method': "POST",
        'async': false,
        'data': {"consumed_hours":$('[id="Consumed Hours"]').val(),
                "work_date":$('[id="Work Date"]').val(),
                "name":$('#Name').val(), "task_id":task_id},
        'success': function(res){
            console.log(res)
            $('#rec_ID').val(res)
        }
    });
});

$('#altEditor-modal').on('click', '#editRowBtn', function(e){
   console.log($('#Name').val());
    console.log($('[id="Consumed Hours"]').val());
    console.log($('[id="Work Date"]').val());
    console.log($('[id="id"]').val());

    $.ajax({
        'url': "http://10.200.234.215:9000/timesheet/api/task/",
        'method': "PUT",
        'data': {"rec_id":$('[id="rec_ID"]').val(),
                "consumed_hours":$('[id="Consumed Hours"]').val(),
                "work_date":$('[id="Work Date"]').val(),
                "name":$('#Name').val()}
    });
});

$('#altEditor-modal').on('click', '#deleteRowBtn', function(e){
    $.ajax({
        'url': "http://10.200.234.215:9000/timesheet/api/task/",
        'method': "DELETE",
        'data': {"rec_id":$('[id="rec_ID"]').val()}
    });
});

$('#task tbody').on('dblclick', 'tr', function () {
        var data = myTable.row( this ).data();
        $(location).attr('href', 'http://10.200.234.215:9000/timesheet/task_line/'+data[0]);
    } );

});