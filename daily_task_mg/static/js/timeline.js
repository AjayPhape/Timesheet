      $(document).ready(function() {


        $('#altEditor-modal [id="Work Date"]').attr({'type':'date'});
        var data_list= [];
        var columnDefs = [{
        title:"rec_ID", visible: false,
        searchable:false}, {
          title: "Name"
        }, {
          title: "Consumed Hours"
        }, {
          title: "Work Date",
        }
        ];

        var myTable = $('#example').DataTable({
          "sPaginationType": "full_numbers",
          "ajax": {
                    "url":"http://10.200.234.215:9000/timesheet/api/",
                    "type": "GET",
                    "params": {"task_id":1}
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
                'url': "http://10.200.234.215:9000/timesheet/api/",
                'method': "POST",
                'async': false,
                'data': {"consumed_hours":$('[id="Consumed Hours"]').val(),
                        "work_date":$('[id="Work Date"]').val(),
                        "name":$('#Name').val()},
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
                'url': "http://10.200.234.215:9000/timesheet/api/",
                'method': "PUT",
                'data': {"rec_id":$('[id="rec_ID"]').val(),
                        "consumed_hours":$('[id="Consumed Hours"]').val(),
                        "work_date":$('[id="Work Date"]').val(),
                        "name":$('#Name').val()}
            });
        });

        $('#altEditor-modal').on('click', '#deleteRowBtn', function(e){
            $.ajax({
                'url': "http://10.200.234.215:9000/timesheet/api/",
                'method': "DELETE",
                'data': {"rec_id":$('[id="rec_ID"]').val()}
            });
        });


      });