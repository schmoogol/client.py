"""Auto Empty event module."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, unique

from .base import Event


@unique
class AutoEmpty(IntEnum):
    """Enum class for all possible auto empty modes."""

    AUTO_EMPTY_OFF = 0
    ON_AUTO = 1
    ON_SMART = 2


@dataclass(frozen=True)
class AutoEmptyEvent(Event):
    """Auto empty event representation."""

    mode: AutoEmpty
