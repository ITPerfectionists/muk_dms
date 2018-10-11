# -*- coding: utf-8 -*-
###################################################################################
#
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

from odoo import models, fields, api, _

class document_detail(models.Model):
    _name = 'muk_dms.document.detail'
    _description = "Muk Document Detail View"
    _rec_name = 'trust_id'

    effective_date = fields.Date("Effective Date")
    trust_id = fields.Many2one(
        'trust.trust',
        string='Related Trust'
    )

    investor_id = fields.Many2one(
        'res.partner',
        related='trust_id.investor_id',
        string = 'Related Investor'
    )

    family_id = fields.Many2one(
        'res.partner',
        related='trust_id.family_id',
        string='Related Family'
    )
    contract_id = fields.Text("Contract ID")