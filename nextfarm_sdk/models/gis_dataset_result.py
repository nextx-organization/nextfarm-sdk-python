from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.gis_dataset_result_totals_type_0 import GisDatasetResultTotalsType0
  from ..models.gis_dataset_row import GisDatasetRow





T = TypeVar("T", bound="GisDatasetResult")



@_attrs_define
class GisDatasetResult:
    

    dataset: None | str | Unset = UNSET
    has_sample: bool | Unset = UNSET
    reason_code: None | str | Unset = UNSET
    record_count: int | Unset = UNSET
    rows: list[GisDatasetRow] | None | Unset = UNSET
    status: None | str | Unset = UNSET
    totals: GisDatasetResultTotalsType0 | None | Unset = UNSET
    truncated: bool | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_dataset_result_totals_type_0 import GisDatasetResultTotalsType0 # noqa: PLC0415
        from ..models.gis_dataset_row import GisDatasetRow # noqa: PLC0415
        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        has_sample = self.has_sample

        reason_code: None | str | Unset
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

        record_count = self.record_count

        rows: list[dict[str, Any]] | None | Unset
        if isinstance(self.rows, Unset):
            rows = UNSET
        elif isinstance(self.rows, list):
            rows = []
            for rows_type_0_item_data in self.rows:
                rows_type_0_item = rows_type_0_item_data.to_dict()
                rows.append(rows_type_0_item)


        else:
            rows = self.rows

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        totals: dict[str, Any] | None | Unset
        if isinstance(self.totals, Unset):
            totals = UNSET
        elif isinstance(self.totals, GisDatasetResultTotalsType0):
            totals = self.totals.to_dict()
        else:
            totals = self.totals

        truncated = self.truncated

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if has_sample is not UNSET:
            field_dict["has_sample"] = has_sample
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if record_count is not UNSET:
            field_dict["record_count"] = record_count
        if rows is not UNSET:
            field_dict["rows"] = rows
        if status is not UNSET:
            field_dict["status"] = status
        if totals is not UNSET:
            field_dict["totals"] = totals
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_dataset_result_totals_type_0 import GisDatasetResultTotalsType0 # noqa: PLC0415
        from ..models.gis_dataset_row import GisDatasetRow # noqa: PLC0415
        d = dict(src_dict)
        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("dataset", UNSET))


        has_sample = d.pop("has_sample", UNSET)

        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reason_code", UNSET))


        record_count = d.pop("record_count", UNSET)

        def _parse_rows(data: object) -> list[GisDatasetRow] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rows_type_0 = []
                _rows_type_0 = data
                for rows_type_0_item_data in (_rows_type_0):
                    rows_type_0_item = GisDatasetRow.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisDatasetRow] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_totals(data: object) -> GisDatasetResultTotalsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                totals_type_0 = GisDatasetResultTotalsType0.from_dict(data)



                return totals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GisDatasetResultTotalsType0 | None | Unset, data)

        totals = _parse_totals(d.pop("totals", UNSET))


        truncated = d.pop("truncated", UNSET)

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        gis_dataset_result = cls(
            dataset=dataset,
            has_sample=has_sample,
            reason_code=reason_code,
            record_count=record_count,
            rows=rows,
            status=status,
            totals=totals,
            truncated=truncated,
            updated_at=updated_at,
        )

        return gis_dataset_result

