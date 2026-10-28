from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotMeterCoefficientRequest")



@_attrs_define
class IotMeterCoefficientRequest:
    

    idx: int | Unset = UNSET
    kind: None | str | Unset = UNSET
    ulp_moi_xung: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        idx = self.idx

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        ulp_moi_xung: int | None | Unset
        if isinstance(self.ulp_moi_xung, Unset):
            ulp_moi_xung = UNSET
        else:
            ulp_moi_xung = self.ulp_moi_xung


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if idx is not UNSET:
            field_dict["idx"] = idx
        if kind is not UNSET:
            field_dict["kind"] = kind
        if ulp_moi_xung is not UNSET:
            field_dict["ulp_moi_xung"] = ulp_moi_xung

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idx = d.pop("idx", UNSET)

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_ulp_moi_xung(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ulp_moi_xung = _parse_ulp_moi_xung(d.pop("ulp_moi_xung", UNSET))


        iot_meter_coefficient_request = cls(
            idx=idx,
            kind=kind,
            ulp_moi_xung=ulp_moi_xung,
        )

        return iot_meter_coefficient_request

