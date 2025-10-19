odoo.define('huroos_openapi.ButtonOpenResPartnerDataFetch', function (require) {
    "use strict";

    const ListController = require('web.ListController');
    const KanbanController = require('web.KanbanController');

    ListController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            const self = this;
            if (this.$buttons) {
                // Bottone in res.partner per wizard fetch dati
                this.$buttons.find('.data-fetch').on('click', function () {
                    self._rpc({
                        model: 'ir.ui.view',
                        method: 'search_read',
                        domain: [['name', '=', 'view_res_partner_data_fetch_form']],
                        fields: ['id'],
                        limit: 1,
                    }).then(function (views) {
                        const view = views[0];
                        self.do_action({
                            name: 'Ottieni/Valida dati',
                            type: 'ir.actions.act_window',
                            res_model: 'res.partner.data.fetch',
                            views: [[view.id, 'form']],
                            target: 'new'
                        });
                    });
                });

                // Bottone in res.partner.visura.camerale per effettuare sync con OpenAPI delle richieste di visure
                this.$buttons.find('.sync-visure').on('click', async function () {
                    await self._rpc({
                        route: "/visure-camerali/refresh"
                    });
                    window.location.reload();
                });

                // Bottone in res.partner.visura.camerale per aprire il wizard di richiesta visura
                this.$buttons.find('.request-visura').on('click', function () {
                    self._rpc({
                        model: 'ir.ui.view',
                        method: 'search_read',
                        domain: [['name', '=', 'view_visura_camerale_request_form']],
                        fields: ['id'],
                        limit: 1,
                    }).then(function (views) {
                        const view = views[0];
                        self.do_action({
                            name: 'Richiesta di visura camerale',
                            type: 'ir.actions.act_window',
                            res_model: 'visura.camerale.request',
                            views: [[view.id, 'form']],
                            target: 'new'
                        });
                    });
                });
            }
        },
    });

    KanbanController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            const self = this;
            if (this.$buttons) {
                this.$buttons.find('.data-fetch').on('click', function () {
                    self._rpc({
                        model: 'ir.ui.view',
                        method: 'search_read',
                        domain: [['name', '=', 'view_res_partner_data_fetch_form']],
                        fields: ['id'],
                        limit: 1,
                    }).then(function (views) {
                        const view = views[0];
                        self.do_action({
                            name: 'Ottieni/Valida dati',
                            type: 'ir.actions.act_window',
                            res_model: 'res.partner.data.fetch',
                            views: [[view.id, 'form']],
                            target: 'new'
                        });
                    });
                });
            }
        },
    });
})
