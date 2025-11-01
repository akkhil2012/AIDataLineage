"""Base definitions for data lineage pipelines."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Pipeline(Protocol):
    """Protocol describing a lineage extraction pipeline."""

    def run(self) -> None:
        """Execute the pipeline."""


@dataclass
class PipelineContext:
    """Shared context passed between pipeline stages."""

    run_id: str
    workspace: str
