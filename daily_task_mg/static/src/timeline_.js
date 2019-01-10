$(function() {

            var DateField = function(config) {
                jsGrid.Field.call(this, config);
            };

            DateField.prototype = new jsGrid.Field({
                sorter: function(date1, date2) {
                    return new Date(date1) - new Date(date2);
                },

                itemTemplate: function(value) {
                    return new Date(value).toDateString();
                },

                insertTemplate: function(value) {
                    return this._insertPicker = $("<input>").datepicker({ defaultDate: new Date() });
                },

                editTemplate: function(value) {
                    return this._editPicker = $("<input>").datepicker().datepicker("setDate", new Date(value));
                },

                insertValue: function() {
                    return this._insertPicker.datepicker("getDate").toISOString();
                },

                editValue: function() {
                    return this._editPicker.datepicker("getDate").toISOString();
                },
                filterValue: function() {
                    return {
                        from: this._fromPicker.datepicker("getDate"),
                        to: this._toPicker.datepicker("getDate")
                    };
                },
                filterTemplate: function() {
                    var now = new Date();
                    this._fromPicker = $("<input>").datepicker({ defaultDate: now.setFullYear(now.getFullYear() - 1) });
                    this._toPicker = $("<input>").datepicker({ defaultDate: now.setFullYear(now.getFullYear() + 1) });
                    return $("<div>").append(this._fromPicker).append(this._toPicker);
                },
            });

            jsGrid.fields.dateField = DateField;

            $("#jsGrid").jsGrid({
                height: "70%",
                width: "100%",
                filtering: true,
                editing: true,
                inserting: true,
                sorting: true,
                paging: true,
                autoload: true,
                pageSize: 15,
                pageButtonCount: 5,
                deleteConfirm: "Do you really want to delete the client?",
                controller: {

                loadData: function(filter) {
                    var d = $.Deferred();
                    $.ajax({
                        type: "GET",
                        url: "/timesheet/api/?task_id=1",
                        data: filter
                    }).done(function(result) {
                        d.resolve($.map(JSON.parse(result), function(item) {
                            return $.extend(item.fields, { id: item.pk });
                        }));
                    });
                    return d.promise();
                },

                insertItem: function(item) {
                        return $.ajax({
                            type: "POST",
                            url: '/timesheet/api/',
                            data: item
                        });
                    },
                updateItem: function(item) {
                        return $.ajax({
                            type: "PUT",
                            url: "/timesheet/api/?rec_id=" + item.id,
                            data: item
                        });
                    },
                deleteItem: function(item) {
                    return $.ajax({
                        type: "DELETE",
                        url: "/timesheet/api/?rec_id=" + item.id
                    });
                }
                },
                fields: [
                    { name: "name", type: "text", width: 250 },
                    { name: "consumed_hours", type: "number", width: 100 },
                    { name: "work_date", type: "dateField", width: 100, align: "center"},
                    { type: "control" }
                ]
            });
        });