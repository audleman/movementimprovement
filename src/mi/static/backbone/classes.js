
var ATMClass = Backbone.Model.extend({
    // url: atmclassUrl
});

var Location = Backbone.Model.extend({
    // url: atmclassUrl
});

var ATMClassCollection = Backbone.Collection.extend({
    model: ATMClass,
    url: atmclassBackboneUrl
});

var LocationCollection = Backbone.Collection.extend({
    model: Location,
    url: locationBackboneUrl
});

var ATMClassView = Backbone.View.extend({
    tagName: "div",
    className: "atm-class-view",
    template: Mustache.template('atmclass'),
    formFields: [{'field': 'location', 'label': 'Location'},
                 {'field': 'date', 'label': 'Date'},
                 {'field': 'time', 'label': 'Time'}],

    initialize: function () {
        // _.bindAll(this, 'save', 'cancel', 'render', 'saveSuccessCallback', 'saveErrorCallback');
        _.bindAll(this, 'render', 'open', 'close', 'toggle');
        this.render();
    },

    render: function(){
        var context = this.model.toJSON();
        for(i=0; i < this.formFields.length; i++){
            this.formFields[i]['data'] = this.model.get(this.formFields[i]['field']);
        }
        context.name = this.getLocationDisplay();
        context.dateDisplay = $.datepicker.formatDate('M d', new Date(context.date));
        context.formFields = this.formFields;
        
        $(this.el).html(this.template.render(context));
        if (this.options.open){
            this.open();
        }
        $('.atm-class', this.el).droppable({
            hoverClass: 'hovered',
            drop: this.dropCallback
        });
    },

    dropCallback: function(event, ui){
        var draggable = ui.draggable;
        console.log( 'The person with ID "' + draggable.attr('id') + '" was dropped onto me!' );

    },

    getLocationDisplay: function(){
        var id = this.model.get("location");
        if (id){
            classLocation = locations.get(id);
            return classLocation.get("name")
        } else {
            return ""
        }
    },

    events: {
        "click .model-header": "toggle",
        // "click .save": "save",
        // "click .cancel": "cancel"
    },

    open: function(e){
        $(".model", this.el).addClass('open');
    },

    close: function(e){
        $(".model", this.el).removeClass('open');
    },

    toggle: function(e){
        $(".model", this.el).toggleClass('open');
    }
});


var ATMClassesView = Backbone.View.extend({

    initialize: function () {
        _.bindAll(this, 'renderItem', 'addItem');
        this.collection.each(this.renderItem);
    },

    addItem: function(model){
        var atmClassView = new ATMClassView({model: model, open: true});
        $(this.el).prepend(atmClassView.el);
    },

    renderItem: function(model){
        var atmClassView = new ATMClassView({model: model});
        $(this.el).append(atmClassView.el); 
    },    
});

