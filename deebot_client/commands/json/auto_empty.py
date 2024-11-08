"""Auto empty commands."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Any

from deebot_client.command import InitParam
from deebot_client.events import AutoEmpty, AutoEmptyEvent
from deebot_client.message import HandlingResult
from deebot_client.util import get_enum

from .common import JsonGetCommand, JsonSetCommand

if TYPE_CHECKING:
    from deebot_client.event_bus import EventBus


class GetAutoEmpty(JsonGetCommand):
    """Get auto empty command."""

    name = "getAutoEmpty"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        event_bus.notify(AutoEmptyEvent(AutoEmpty(int(data["mode"]))))
        return HandlingResult.success()


class SetAutoEmpty(JsonSetCommand):
    """Set auto empty command."""

    name = "setAutoEmpty"
    get_command = GetAutoEmpty
    _mqtt_params = MappingProxyType({"mode": InitParam(AutoEmpty)})

    def __init__(self, mode: AutoEmpty | str) -> None:
        if isinstance(mode, str):
            mode = get_enum(AutoEmpty, mode)
        super().__init__({"mode": mode.value})