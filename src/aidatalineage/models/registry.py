"""Model registry for lineage inference components."""

from __future__ import annotations

from collections.abc import Callable
from typing import Dict

ModelFactory = Callable[[], object]


class ModelRegistry:
    """Simple in-memory registry for model factories."""

    def __init__(self) -> None:
        self._registry: Dict[str, ModelFactory] = {}

    def register(self, name: str, factory: ModelFactory) -> None:
        if name in self._registry:
            raise ValueError(f"Model '{name}' is already registered")
        self._registry[name] = factory

    def create(self, name: str) -> object:
        try:
            factory = self._registry[name]
        except KeyError as exc:
            raise KeyError(f"Unknown model '{name}'") from exc
        return factory()


registry = ModelRegistry()
