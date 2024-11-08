from __future__ import annotations

from typing import Any

import pytest

from deebot_client.commands.json import GetAutoEmpty, SetAutoEmpty, GetAutoEmptyFrequency, SetAutoEmptyFrequency
from deebot_client.events import AutoEmpty, AutoEmptyEvent, AutoEmptyFrequency
from tests.helpers import (
    get_request_json,
    get_success_body,
)

from . import assert_command, assert_set_command


@pytest.mark.parametrize(
    ("json", "expected"),
    [
        ({"frequency": "auto"}, AutoEmptyEvent(AutoEmptyFrequency.AUTO, AutoEmpty.ON)),
        ({"frequency": "smart"}, AutoEmptyEvent(AutoEmptyFrequency.SMART, AutoEmpty.ON)),
    ],
)
async def test_GetAutoEmpty(json: dict[str, Any], expected: AutoEmptyEvent) -> None:
    json = get_request_json(get_success_body(json))
    await assert_command(GetAutoEmptyFrequency(), json, expected)


@pytest.mark.parametrize(("value"), [AutoEmptyFrequency.SMART, "smart"])
async def test_SetAutoEmpty(value: AutoEmptyFrequency | str) -> None:
    command = SetAutoEmptyFrequency(value)
    args = {"frequency": "smart"}
    await assert_set_command(command, args, AutoEmptyEvent(AutoEmpty.SMART), AutoEmpty.ON)


def test_SetAutoEmpty_inexisting_value() -> None:
    with pytest.raises(ValueError, match="'INEXSTING' is not a valid AutoEmpty member"):
        SetAutoEmptyFrequency("inexsting")
