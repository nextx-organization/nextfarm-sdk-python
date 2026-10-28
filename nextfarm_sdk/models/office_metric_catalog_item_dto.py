from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeMetricCatalogItemDto")



@_attrs_define
class OfficeMetricCatalogItemDto:
    

    available: bool | Unset = UNSET
    code: None | str | Unset = UNSET
    curve: None | str | Unset = UNSET
    label_en: None | str | Unset = UNSET
    label_vi: None | str | Unset = UNSET
    planned: bool | Unset = UNSET
    reason_code: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        available = self.available

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        curve: None | str | Unset
        if isinstance(self.curve, Unset):
            curve = UNSET
        else:
            curve = self.curve

        label_en: None | str | Unset
        if isinstance(self.label_en, Unset):
            label_en = UNSET
        else:
            label_en = self.label_en

        label_vi: None | str | Unset
        if isinstance(self.label_vi, Unset):
            label_vi = UNSET
        else:
            label_vi = self.label_vi

        planned = self.planned

        reason_code: None | str | Unset
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if available is not UNSET:
            field_dict["available"] = available
        if code is not UNSET:
            field_dict["code"] = code
        if curve is not UNSET:
            field_dict["curve"] = curve
        if label_en is not UNSET:
            field_dict["labelEn"] = label_en
        if label_vi is not UNSET:
            field_dict["labelVi"] = label_vi
        if planned is not UNSET:
            field_dict["planned"] = planned
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if source is not UNSET:
            field_dict["source"] = source
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available", UNSET)

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_curve(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curve = _parse_curve(d.pop("curve", UNSET))


        def _parse_label_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_en = _parse_label_en(d.pop("labelEn", UNSET))


        def _parse_label_vi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_vi = _parse_label_vi(d.pop("labelVi", UNSET))


        planned = d.pop("planned", UNSET)

        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reasonCode", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        office_metric_catalog_item_dto = cls(
            available=available,
            code=code,
            curve=curve,
            label_en=label_en,
            label_vi=label_vi,
            planned=planned,
            reason_code=reason_code,
            source=source,
            unit=unit,
        )

        return office_metric_catalog_item_dto

