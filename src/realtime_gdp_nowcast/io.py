from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def read_table(path: str | Path) -> pd.DataFrame:
    file_path = Path(path)
    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(file_path)
    if suffix in {".parquet", ".pq"}:
        return pd.read_parquet(file_path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(file_path)
    raise ValueError(f"Unsupported table format: {file_path}")


def write_table(df: pd.DataFrame, path: str | Path, *, index: bool = False) -> Path:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        df.to_csv(file_path, index=index)
    elif suffix in {".parquet", ".pq"}:
        df.to_parquet(file_path, index=index)
    else:
        raise ValueError(f"Unsupported output format: {file_path}")
    return file_path


def write_text(text: str, path: str | Path) -> Path:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(text, encoding="utf-8")
    return file_path


def ensure_parent(paths: Iterable[str | Path]) -> None:
    for path in paths:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
