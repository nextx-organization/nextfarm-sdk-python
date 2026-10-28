from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeMetricPreviewDto")



@_attrs_define
class OfficeMetricPreviewDto:
    

    reason_code: None | str | Unset = UNSET
    source_updated_at: datetime.datetime | None | Unset = UNSET
    status: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    value: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        reason_code: None | str | Unset
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

        source_updated_at: None | str | Unset
        if isinstance(self.source_updated_at, Unset):
            source_updated_at = UNSET
        elif isinstance(self.source_updated_at, datetime.datetime):
            source_updated_at = self.source_updated_at.isoformat()
        else:
            source_updated_at = self.source_updated_at

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if source_updated_at is not UNSET:
            field_dict["sourceUpdatedAt"] = source_updated_at
        if status is not UNSET:
            field_dict["status"] = status
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reasonCode", UNSET))


        def _parse_source_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return source_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        source_updated_at = _parse_source_updated_at(d.pop("sourceUpdatedAt", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        office_metric_preview_dto = cls(
            reason_code=reason_code,
            source_updated_at=source_updated_at,
            status=status,
            unit=unit,
            value=value,
        )

        return office_metric_preview_dto

