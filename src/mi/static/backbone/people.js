
var Person = Backbone.Model.extend({
    // url: personBackboneUrl
});

var PersonCollection = Backbone.Collection.extend({
    model: Person,
    url: personBackboneUrl
});

var PersonView = Backbone.View.extend({
    tagName: "div",
    className: "person-view",
    template: Mustache.template('person'),
    formFields: [{'field': 'first_name', 'label': 'First Name'},
                 {'field': 'last_name', 'label': 'Last Name'},
                 {'field': 'email', 'label': 'Email'},
                 {'field': 'phone', 'label': 'Phone'}],

    initialize: function () {
        _.bindAll(this, 'save', 'cancel', 'render', 'saveSuccessCallback', 'saveErrorCallback');
        this.render();
    },

    render: function(){
        var context = this.model.toJSON();
        for(i=0; i < this.formFields.length; i++){
            this.formFields[i]['data'] = this.model.get(this.formFields[i]['field']);
        }
        context.formFields = this.formFields;
        $(this.el).html(this.template.render(context));
        if (this.options.open){
            this.open();
        }
    },    

    events: {
        "click .model-header": "toggle",
        "click .save": "save",
        "click .cancel": "cancel"
    },

    open: function(e){
        $(".model", this.el).addClass('open');
    },

    close: function(e){
        $(".model", this.el).removeClass('open');
    },

    toggle: function(e){
        $(".model", this.el).toggleClass('open');
    },

    save: function(e){
        e.preventDefault();
        // Gather form data and update model
        for(i=0; i < this.formFields.length; i++){
            var field = this.formFields[i]['field'];
            var value = $('[name=' + field + ']', this.el).val();
            this.model.set(field, value);
        }

        if (this.model.isNew()){
            this.model.url = personBackboneUrl;
        }

        this.model.save({}, {
            success: this.saveSuccessCallback,
            error: this.saveErrorCallback
        });
    },

    saveSuccessCallback: function(model, response, options){
        var full_name = this.model.get("first_name") + ' ' + this.model.get("last_name");
        $('.name', this.el).html(full_name);
        this.close();
    },

    saveErrorCallback: function(model, xhr, options){
        errors = JSON.parse(xhr.responseText);
        for (var field in errors) {
            var error = errors[field][0];
            $("#" + field + "-errors", this.el).html(error);
        }
    },

    cancel: function(e){
        e.preventDefault();
        if(!this.model.isNew()){
            $(".person", this.el).removeClass('open');
        } else {
            this.model.destroy();
            this.remove();
        }
    }

});

var PeopleView = Backbone.View.extend({

    initialize: function () {
        _.bindAll(this, 'renderItem', 'addItem');
        this.collection.each(this.renderItem);
        $(".btn").draggable({ opacity: 0.7, helper: "clone" });
    },

    events: {
        // "click .action-icon-add": "addPerson",
    },

    renderItem: function(model){
        var personView = new PersonView({model: model});
        $(this.el).append(personView.el); 
    },

    addItem: function(model){
        var personView = new PersonView({model: model, open: true});
        $(this.el).prepend(personView.el);

    }
});