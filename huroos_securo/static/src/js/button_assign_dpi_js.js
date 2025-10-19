odoo.define("huroos_securo.assing_dpi", function (require) {
    "use strict";

    var ListController = require("web.ListController");
    var FormController = require("web.FormController");

    var includeDict = {
        renderButtons: function () {
            this._super.apply(this, arguments);
            if (this.modelName === "securo.dpi.employee" && this.$buttons) {
                var self = this;
                var data = this.model.get(this.handle);

                this.$buttons
                    .find(".assign_dpi")
                    .on("click", function () {
                        self.do_action(
                            "huroos_securo.assign_dpi_action",
                            {
                                additional_context: {},
                            }
                        );
                    });
            }
        },
    };


    ListController.include(includeDict);
    FormController.include(includeDict);
});