# Copyright 2024 kobros-tech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from typing import Union

from pydantic import BaseModel


class TestData(BaseModel):
    name: Union[str, None] = None
    email: Union[str, None] = None
    uid: int
