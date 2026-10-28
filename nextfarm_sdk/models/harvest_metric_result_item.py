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
  from ..models.harvest_metric_parcel_value_dto import HarvestMetricParcelValueDto





T = TypeVar("T", bound="HarvestMetricResultItem")



@_attrs_define
class HarvestMetricResultItem:
    

    by_parcel: list[HarvestMetricParcelValueDto] | None | Unset = UNSET
    key: None | str | Unset = UNSET
    reason_code: None | str | Unset = UNSET
    source_updated_at: datetime.datetime | None | Unset = UNSET
    status: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    value: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_metric_parcel_value_dto import HarvestMetricParcelValueDto # noqa: PLC0415
        by_parcel: list[dict[str, Any]] | None | Unset
        if isinstance(self.by_parcel, Unset):
            by_parcel = UNSET
        elif isinstance(self.by_parcel, list):
            by_parcel = []
            for by_parcel_type_0_item_data in self.by_parcel:
                by_parcel_type_0_item = by_parcel_type_0_item_data.to_dict()
                by_parcel.append(by_parcel_type_0_item)


        else:
            by_parcel = self.by_parcel

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

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
        if by_parcel is not UNSET:
            field_dict["by_parcel"] = by_parcel
        if key is not UNSET:
            field_dict["key"] = key
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if source_updated_at is not UNSET:
            field_dict["source_updated_at"] = source_updated_at
        if status is not UNSET:
            field_dict["status"] = status
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_metric_parcel_value_dto import HarvestMetricParcelValueDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_by_parcel(data: object) -> list[HarvestMetricParcelValueDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_parcel_type_0 = []
                _by_parcel_type_0 = data
                for by_parcel_type_0_item_data in (_by_parcel_type_0):
                    by_parcel_type_0_item = HarvestMetricParcelValueDto.from_dict(by_parcel_type_0_item_data)



                    by_parcel_type_0.append(by_parcel_type_0_item)

                return by_parcel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestMetricParcelValueDto] | None | Unset, data)

        by_parcel = _parse_by_parcel(d.pop("by_parcel", UNSET))


        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reason_code", UNSET))


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

        source_updated_at = _parse_source_updated_at(d.pop("source_updated_at", UNSET))


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


        harvest_metric_result_item = cls(
            by_parcel=by_parcel,
            key=key,
            reason_code=reason_code,
            source_updated_at=source_updated_at,
            status=status,
            unit=unit,
            value=value,
        )

        return harvest_metric_result_item

