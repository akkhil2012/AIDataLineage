"""Command-line entry point for executing data lineage pipelines."""

from aidatalineage.pipelines import __all__  # noqa: F401  # Placeholder import


def main() -> None:
    """Execute the default data lineage pipeline."""
    raise NotImplementedError(
        "Pipeline execution is not yet implemented. Define your pipeline in "
        "`src/aidatalineage/pipelines` and update this entry point."
    )


if __name__ == "__main__":
    main()
