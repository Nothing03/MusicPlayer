"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Anonymous Boy <https://github.com/AnonymousBoy1025>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "21849173")
        self.API_HASH: str = os.environ.get("API_HASH", "5d4ae6614b45dc890f3cbe3980c493f3")
        self.SESSION: str = os.environ.get("SESSION", "AQBUa3P0U8HfcilFtPP84n6M4oTPhSWDqiDR2c-kCa4AMt46xk4TcoTi-Tf8-piRcZfF1JiQPXdoM2Q7zzAA5HdD0oVnnODtWdW_Df8irPCDcd4hbVtEWmiZFQLU4gYuNn-G5Mxk2_q8waPDv6B0FIuMJbugq7XD1Jm3T_t7rmwjbPXlX7QV8EcZb1JIJlncUo4toHovq9DU3egqND9vtWVFgnx_i3eBNpYQ2BfNW3yT0plDV892D3nOW8NGdHKO51yv1ehhtY4PWCEGPKF7WdYct8F6KtdpsHY0WqtR91MHKPSNfa_CXOVc-YaWL8viCNK6Pie4RtkZBE_iqgwuqg9EAAAAAUfAUeYA")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5498753510").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.CUSTOM_QUALITY: str = os.environ.get("CUSTOM_QUALITY", "high").lower()


config = Config()
