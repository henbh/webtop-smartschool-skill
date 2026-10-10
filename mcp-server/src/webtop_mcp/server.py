# Copyright 2026 Hen Ben-Hemo
# SPDX-License-Identifier: Apache-2.0
"""Expose a small read-only Webtop API surface over MCP stdio."""

from __future__ import annotations

import json
import logging
import os
from typing import Any

from mcp.server.fastmcp import FastMCP
from webtop import WebtopClient

# The upstream client's error logs can include raw response bodies.
logging.getLogger("webtop").setLevel(logging.CRITICAL)

mcp = FastMCP("Webtop")


def _credentials() -> tuple[str, str, str]:
    username = os.getenv("WEBTOP_USERNAME", "").strip()
    password = os.getenv("WEBTOP_PASSWORD", "")
    data = os.getenv("WEBTOP_DATA", "+Aabe7FAdVluG6Lu+0ibrA==")
    if not username or not password:
        raise ValueError(
            "Set WEBTOP_USERNAME and WEBTOP_PASSWORD in the MCP server environment."
        )
    return username, password, data


def _json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, default=str)


async def _with_client(operation: Any) -> str:
    try:
        username, password, data = _credentials()
    except ValueError as exc:
        return str(exc)
    try:
        async with WebtopClient(
            username=username,
            password=password,
            data=data,
            auto_login=True,
        ) as client:
            return _json_text(await operation(client))
    except Exception as exc:
        # Do not include request bodies, tokens, or other server response data.
        logging.getLogger(__name__).warning("Webtop request failed: %s", type(exc).__name__)
        return (
            "Webtop request failed ("
            f"{type(exc).__name__}). Check that the credentials and WEBTOP_DATA are "
            "correct and that the Webtop API is available."
        )


@mcp.tool()
async def get_dashboard() -> str:
    """Read the signed-in account's Webtop dashboard and student details."""

    return await _with_client(lambda client: client.get_students())


@mcp.tool()
async def get_homework(class_code: int, class_number: int) -> str:
    """Read the homework records for one Webtop class.

    Returns Webtop's original JSON data. The client should preserve full
    homework text and apply requested date ranges to the returned lesson dates.
    """

    async def request(client: WebtopClient) -> Any:
        session = await client.login()
        encrypted_student_id = session.raw_login_data.get("id")
        if not encrypted_student_id:
            raise ValueError("Webtop login did not return a student identifier.")
        return await client.get_homework(
            encrypted_student_id=encrypted_student_id,
            class_code=class_code,
            class_number=class_number,
        )

    return await _with_client(request)


def main() -> None:
    """Run the MCP server over stdio for a local MCP client."""

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
