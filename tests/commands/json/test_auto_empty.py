from __future__ import annotations

from typing import Any

import pytest

from deebot_client.commands.json import GetAutoEmpty, SetAutoEmpty
from deebot_client.events import AutoEmpty, AutoEmptyEvent
from tests.helpers import (
    get_request_json,
    get_success_body,
)

from . import assert_command, assert_set_command


@pytest.mark.parametrize(
    ("json", "expected"),
    [
        ({"mode": 0}, AutoEmptyEvent(AutoEmpty.AUTO_EMPTY_OFF)),
        ({"mode": 1}, AutoEmptyEvent(AutoEmpty.ON_AUTO)),
        ({"mode": 2}, AutoEmptyEvent(AutoEmpty.ON_SMART)),
    ],
)
async def test_GetAutoEmpty(json: dict[str, Any], expected: AutoEmptyEvent) -> None:
    json = get_request_json(get_success_body(json))
    await assert_command(GetAutoEmpty(), json, expected)


@pytest.mark.parametrize(("value"), [AutoEmpty.ON_SMART, "on_smart"])
async def test_SetAutoEmpty(value: AutoEmpty | str) -> None:
    command = SetAutoEmpty(value)
    args = {"mode": 2}
    await assert_set_command(command, args, AutoEmptyEvent(AutoEmpty.ON_SMART))


def test_SetAutoEmpty_inexisting_value() -> None:
    with pytest.raises(ValueError, match="'INEXSTING' is not a valid AutoEmpty member"):
        SetAutoEmpty("inexsting")
