from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GisPhatLaiMuaVuKetQua")



@_attrs_define
class GisPhatLaiMuaVuKetQua:
    

    so_vu_da_phat: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        so_vu_da_phat = self.so_vu_da_phat


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if so_vu_da_phat is not UNSET:
            field_dict["so_vu_da_phat"] = so_vu_da_phat

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        so_vu_da_phat = d.pop("so_vu_da_phat", UNSET)

        gis_phat_lai_mua_vu_ket_qua = cls(
            so_vu_da_phat=so_vu_da_phat,
        )

        return gis_phat_lai_mua_vu_ket_qua

