from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotTheTichServerTinhDto")



@_attrs_define
class IotTheTichServerTinhDto:
    

    lit: float | None | Unset = UNSET
    ly_do: None | str | Unset = UNSET
    nguon: None | str | Unset = UNSET
    ulp_da_dung: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        lit: float | None | Unset
        if isinstance(self.lit, Unset):
            lit = UNSET
        else:
            lit = self.lit

        ly_do: None | str | Unset
        if isinstance(self.ly_do, Unset):
            ly_do = UNSET
        else:
            ly_do = self.ly_do

        nguon: None | str | Unset
        if isinstance(self.nguon, Unset):
            nguon = UNSET
        else:
            nguon = self.nguon

        ulp_da_dung: int | None | Unset
        if isinstance(self.ulp_da_dung, Unset):
            ulp_da_dung = UNSET
        else:
            ulp_da_dung = self.ulp_da_dung


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if lit is not UNSET:
            field_dict["lit"] = lit
        if ly_do is not UNSET:
            field_dict["ly_do"] = ly_do
        if nguon is not UNSET:
            field_dict["nguon"] = nguon
        if ulp_da_dung is not UNSET:
            field_dict["ulp_da_dung"] = ulp_da_dung

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_lit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lit = _parse_lit(d.pop("lit", UNSET))


        def _parse_ly_do(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ly_do = _parse_ly_do(d.pop("ly_do", UNSET))


        def _parse_nguon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nguon = _parse_nguon(d.pop("nguon", UNSET))


        def _parse_ulp_da_dung(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ulp_da_dung = _parse_ulp_da_dung(d.pop("ulp_da_dung", UNSET))


        iot_the_tich_server_tinh_dto = cls(
            lit=lit,
            ly_do=ly_do,
            nguon=nguon,
            ulp_da_dung=ulp_da_dung,
        )

        return iot_the_tich_server_tinh_dto

