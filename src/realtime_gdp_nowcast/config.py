from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(slots=True)
class ProjectPaths:
    root: Path
    raw_data: Path
    bronze_data: Path
    silver_data: Path
    interim_data: Path
    processed_data: Path
    outputs: Path
    docs: Path
    series_catalog: Path
    target_catalog: Path

    def ensure_directories(self) -> None:
        for path in [
            self.raw_data,
            self.bronze_data,
            self.silver_data,
            self.interim_data,
            self.processed_data,
            self.outputs,
            self.docs,
            self.outputs / "tables",
            self.outputs / "figures",
            self.outputs / "reports",
            self.outputs / "forecasts",
        ]:
            path.mkdir(parents=True, exist_ok=True)


@dataclass(slots=True)
class ProjectSettings:
    config_path: Path
    data: dict[str, Any]
    paths: ProjectPaths

    @property
    def project(self) -> dict[str, Any]:
        return self.data["project"]

    @property
    def sample(self) -> dict[str, Any]:
        return self.data["sample"]

    @property
    def checkpoints(self) -> list[dict[str, Any]]:
        return list(self.data["checkpoints"])

    @property
    def download(self) -> dict[str, Any]:
        return self.data["download"]

    @property
    def models(self) -> dict[str, Any]:
        return self.data["models"]

    @property
    def reporting(self) -> dict[str, Any]:
        return self.data["reporting"]

    def get(self, *keys: str, default: Any = None) -> Any:
        current: Any = self.data
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current


def _resolve_path(root: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (root / path).resolve()


def load_settings(root: str | Path | None = None, config_path: str | Path | None = None) -> ProjectSettings:
    root_path = Path(root or Path.cwd()).resolve()
    config_file = Path(config_path) if config_path else root_path / "configs" / "project.yaml"
    config_file = config_file.resolve()
    with config_file.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle)

    paths_raw = raw["paths"]
    paths = ProjectPaths(
        root=root_path,
        raw_data=_resolve_path(root_path, paths_raw["raw_data"]),
        bronze_data=_resolve_path(root_path, paths_raw["bronze_data"]),
        silver_data=_resolve_path(root_path, paths_raw["silver_data"]),
        interim_data=_resolve_path(root_path, paths_raw["interim_data"]),
        processed_data=_resolve_path(root_path, paths_raw["processed_data"]),
        outputs=_resolve_path(root_path, paths_raw["outputs"]),
        docs=_resolve_path(root_path, paths_raw["docs"]),
        series_catalog=_resolve_path(root_path, paths_raw["series_catalog"]),
        target_catalog=_resolve_path(root_path, paths_raw["target_catalog"]),
    )
    paths.ensure_directories()
    return ProjectSettings(config_path=config_file, data=raw, paths=paths)
