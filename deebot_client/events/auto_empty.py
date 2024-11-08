"""Auto Empty event module."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, Enum, unique

from .base import Event


@unique
class AutoEmpty(IntEnum):
    """Enum class for all possible auto empty frequencies."""

    ON = "1"
    OFF = "0"

@unique
class AutoEmptyFrequency(Enum):
    """Enum class for all possible auto empty frequencies."""

    AUTO = "auto"
    SMART = "smart"

@dataclass(frozen=True)
class AutoEmptyEvent(Event):
    """Auto empty event representation."""

    frequency: AutoEmptyFrequency
    enable: AutoEmpty
