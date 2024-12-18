# Copyright 2024 kobros-tech
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "FastAPI Auth JWT Model",
    "summary": """
        A prototype module for fastapi_auth_jwt.""",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "author": "kobros-tech, Odoo Community Association (OCA)",
    "maintainers": ["kobros-tech"],
    "website": "https://github.com/OCA/rest-framework",
    "depends": ["fastapi", "fastapi_auth_jwt"],
    "data": [
        "data/auth_jwt_validator.xml",
        "data/fastapi_endpoint_demo.xml",
        "data/fastapi_endpoint.xml",

        "views/fastapi_endpoint_view.xml",
    ],
    'installable': True,
}
