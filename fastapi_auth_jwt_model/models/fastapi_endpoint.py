# Copyright 2024 kobros-tech
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models

from ..routers.auth_jwt_model_api import router as auth_jwt_model_api_router
from ..routers.customer import customer_router

APP_NAME = "fastapi_auth_jwt_model"


class FastapiEndpoint(models.Model):
    _inherit = "fastapi.endpoint"

    app: str = fields.Selection(
        selection_add=[(APP_NAME, "Auth JWT Model Endpoint")],
        ondelete={APP_NAME: "cascade"},
    )
    auth_jwt_validator_id = fields.Many2one("auth.jwt.validator")

    @api.model
    def _get_fastapi_routers(self):
        if self.app == APP_NAME:
            return [
                auth_jwt_model_api_router,
                customer_router,
            ]
        return super()._get_fastapi_routers()
