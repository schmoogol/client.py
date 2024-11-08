"""Auto empty commands."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Any

from deebot_client.command import InitParam
from deebot_client.events import AutoEmpty, AutoEmptyEvent, AutoEmptyFrequency
from deebot_client.message import HandlingResult
from deebot_client.util import get_enum

from .common import JsonGetCommand, JsonSetCommand

if TYPE_CHECKING:
    from deebot_client.event_bus import EventBus


class GetAutoEmptyFrequency(JsonGetCommand):
    """Get auto empty frequency command."""

    name = "getAutoEmpty"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        event_bus.notify(AutoEmptyEvent(AutoEmptyFrequency(int(data["frequency"]))))
        return HandlingResult.success()


class SetAutoEmptyFrequency(JsonSetCommand):
    """Set auto empty frequency command."""

    name = "setAutoEmpty"
    get_command = GetAutoEmptyFrequency
    _mqtt_params = MappingProxyType({"frequency": InitParam(AutoEmpty)})

    def __init__(self, frequency: AutoEmptyFrequency | str) -> None:
        if isinstance(frequency, str):
            frequency = get_enum(AutoEmptyFrequency, frequency)
        super().__init__({"frequency": frequency.value})

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
        event_bus.notify(AutoEmptyEvent(AutoEmpty(int(data["enable"]))))
        return HandlingResult.success()


class SetAutoEmpty(JsonSetCommand):
    """Set auto empty command."""

    name = "setAutoEmpty"
    get_command = GetAutoEmpty
    _mqtt_params = MappingProxyType({"enable": InitParam(AutoEmpty)})

    def __init__(self, frequency: AutoEmpty | str) -> None:
        if isinstance(frequency, str):
            frequency = get_enum(AutoEmpty, enable)
        super().__init__({"frequency": enable.value})