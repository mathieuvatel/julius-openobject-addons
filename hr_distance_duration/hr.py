# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

# from openerp.addons.google_maps_distance_duration.google_maps import GoogleMaps
# from openerp.addons.base_geolocalize.models.res_partner import geo_query_address
import datetime
import time
from openerp import models, fields, api

class hr_job(models.Model):
    _inherit = 'hr.job'

    @api.one
    def get_duration(self):
        departure_time = self._context.get('departure_time')
        if not departure_time:
            n = datetime.datetime.now()
            departure_time = int(time.mktime(n.timetuple()))
        self.application_ids.get_distance_duration()
        return True

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: