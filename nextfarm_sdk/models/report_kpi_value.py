from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReportKpiValue")



@_attrs_define
class ReportKpiValue:
    

    compare: float | None | Unset = UNSET
    delta_pct: float | None | Unset = UNSET
    key: None | str | Unset = UNSET
    value: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        compare: float | None | Unset
        if isinstance(self.compare, Unset):
            compare = UNSET
        else:
            compare = self.compare

        delta_pct: float | None | Unset
        if isinstance(self.delta_pct, Unset):
            delta_pct = UNSET
        else:
            delta_pct = self.delta_pct

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if compare is not UNSET:
            field_dict["compare"] = compare
        if delta_pct is not UNSET:
            field_dict["deltaPct"] = delta_pct
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_compare(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        compare = _parse_compare(d.pop("compare", UNSET))


        def _parse_delta_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        delta_pct = _parse_delta_pct(d.pop("deltaPct", UNSET))


        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        report_kpi_value = cls(
            compare=compare,
            delta_pct=delta_pct,
            key=key,
            value=value,
        )

        return report_kpi_value

