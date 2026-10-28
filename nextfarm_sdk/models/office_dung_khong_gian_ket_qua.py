from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeDungKhongGianKetQua")



@_attrs_define
class OfficeDungKhongGianKetQua:
    

    nha_vuon_da_co: int | Unset = UNSET
    spaces_dung_san: int | Unset = UNSET
    spaces_nha_vuon: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        nha_vuon_da_co = self.nha_vuon_da_co

        spaces_dung_san = self.spaces_dung_san

        spaces_nha_vuon = self.spaces_nha_vuon


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if nha_vuon_da_co is not UNSET:
            field_dict["nhaVuonDaCo"] = nha_vuon_da_co
        if spaces_dung_san is not UNSET:
            field_dict["spacesDungSan"] = spaces_dung_san
        if spaces_nha_vuon is not UNSET:
            field_dict["spacesNhaVuon"] = spaces_nha_vuon

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nha_vuon_da_co = d.pop("nhaVuonDaCo", UNSET)

        spaces_dung_san = d.pop("spacesDungSan", UNSET)

        spaces_nha_vuon = d.pop("spacesNhaVuon", UNSET)

        office_dung_khong_gian_ket_qua = cls(
            nha_vuon_da_co=nha_vuon_da_co,
            spaces_dung_san=spaces_dung_san,
            spaces_nha_vuon=spaces_nha_vuon,
        )

        return office_dung_khong_gian_ket_qua

