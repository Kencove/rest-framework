# Copyright 2024 kobros-tech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from pydantic import BaseModel


class TestData(BaseModel):
    name: str | None = None
    email: str | None = None
    uid: int
