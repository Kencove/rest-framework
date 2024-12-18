import json
import logging

import time

import jwt

from odoo import tests

import requests

#######################################################
#######################################################


@tests.tagged("post_install", "-at_install")
class TestEndToEnd(tests.HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env.ref(
            "fastapi_auth_jwt_model.fastapi_endpoint_auth_jwt_model"
        )._handle_registry_sync()
        cls.env.ref(
            "fastapi_auth_jwt_model.fastapi_endpoint_demo"
        )._handle_registry_sync()
    
    def _get_token(self, aud=None, email=None):
        validator = self.env["auth.jwt.validator"].search([("name", "=", "model")])
        payload = {
            "aud": aud or validator.audience,
            "iss": validator.issuer,
            "exp": time.time() + 60,
            # "email": "mark.brown23@example.com",
        }
        if email:
            payload["email"] = email
        access_token = jwt.encode(
            payload, key=validator.secret_key, algorithm=validator.secret_algorithm
        )
        return "Bearer " + access_token
    
    def test_whoami(self):
        """A end-to-end test with positive authentication and partner retrieval."""
        partner = self.env["res.users"].search([("email", "!=", False)])[0]
        token = self._get_token(email=partner.email)
        resp = self.url_open(
            "/fastapi_auth_jwt_model/whoami", headers={"Authorization": token}
        )
        resp.raise_for_status()
        whoami = resp.json()
        self.assertEqual(whoami.get("name"), partner.name)
        self.assertEqual(whoami.get("email"), partner.email)
        self.assertEqual(whoami.get("uid"), self.env.ref("base.user_demo").id)
        # Try again in a user session, it works because fastapi ignores the Odoo session.
        self.authenticate("demo", "demo")
        resp = self.url_open(
            "/fastapi_auth_jwt_model/whoami", headers={"Authorization": token}
        )
        self.assertEqual(whoami.get("name"), partner.name)
        self.assertEqual(whoami.get("email"), partner.email)
        self.assertEqual(whoami.get("uid"), self.env.ref("base.user_demo").id)
    
    def test_whoami_public_or_jwt(self):
        """A end-to-end test with positive authentication and partner retrieval."""
        partner = self.env["res.users"].search([("email", "!=", False)])[0]
        token = self._get_token(email=partner.email)
        resp = self.url_open(
            "/fastapi_auth_jwt_model/whoami-public-or-jwt", headers={"Authorization": token}
        )
        resp.raise_for_status()
        whoami = resp.json()
        self.assertEqual(whoami.get("name"), partner.name)
        self.assertEqual(whoami.get("email"), partner.email)
        self.assertEqual(whoami.get("uid"), self.env.ref("base.user_demo").id)
        # Try again in a user session, it works because fastapi ignores the Odoo session.
        self.authenticate("demo", "demo")
        resp = self.url_open(
            "/fastapi_auth_jwt_model/whoami-public-or-jwt", headers={"Authorization": token}
        )
        self.assertEqual(whoami.get("name"), partner.name)
        self.assertEqual(whoami.get("email"), partner.email)
        self.assertEqual(whoami.get("uid"), self.env.ref("base.user_demo").id)
    
    def test_customer_read(self):
        """A end-to-end test with positive authentication and partner retrieval."""
        partner = self.env["res.users"].search([("email", "=", "joel.willis63@example.com")])
        token = self._get_token(email=partner.email)
        resp = self.url_open(
            "/fastapi_auth_jwt_model/customer", headers={"Authorization": token}
        )
        resp.raise_for_status()
        customer = resp.json()
        self.assertEqual(customer.get("name"), partner.name)
        self.assertEqual(customer.get("email"), partner.email)
        self.assertEqual(customer.get("phone"), partner.phone)
    
    def test_customer_write(self):
        """A end-to-end test with positive authentication and partner retrieval."""
        partner = self.env["res.users"].search([("email", "=", "joel.willis63@example.com")])
        token = self._get_token(email=partner.email)
        # Remove field value
        partner.mobile = None
        # Read field value before update
        resp = self.url_open(
            "/fastapi_auth_jwt_model/customer", 
            headers={"Authorization": token},
        )
        resp.raise_for_status()
        customer = resp.json()
        self.assertFalse(customer.get("mobile"))
        # Read field value after update
        data=json.dumps(
            {
                "mobile": "+1-234-567",
            }
        )
        resp = self.url_open(
            "/fastapi_auth_jwt_model/customer", 
            headers={"Authorization": token},
            data=data,
        )
        # resp.raise_for_status()
        customer = resp.json()
        self.assertEqual(customer.get("mobile"), "+1-234-567")
        self.assertEqual(customer.get("mobile"), partner.mobile)
        
        