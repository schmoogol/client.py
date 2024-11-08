"""Auto Empty event module."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, unique

from .base import Event


@unique
class AutoEmpty(Enum):
    """Enum class for all possible auto empty frequencies."""

    AUTO = "auto"
    SMART = "smart"


@dataclass(frozen=True)
class AutoEmptyEvent(Event):
    """Auto empty event representation."""

    mode: AutoEmpty
    enable: bool
