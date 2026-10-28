from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="IotLitPhanChuKyDto")



@_attrs_define
class IotLitPhanChuKyDto:
    

    lit: float | None | Unset = UNSET
    moc_tai: datetime.datetime | None | Unset = UNSET
    xung_tu_dau_cu: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        lit: float | None | Unset
        if isinstance(self.lit, Unset):
            lit = UNSET
        else:
            lit = self.lit

        moc_tai: None | str | Unset
        if isinstance(self.moc_tai, Unset):
            moc_tai = UNSET
        elif isinstance(self.moc_tai, datetime.datetime):
            moc_tai = self.moc_tai.isoformat()
        else:
            moc_tai = self.moc_tai

        xung_tu_dau_cu: int | None | Unset
        if isinstance(self.xung_tu_dau_cu, Unset):
            xung_tu_dau_cu = UNSET
        else:
            xung_tu_dau_cu = self.xung_tu_dau_cu


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if lit is not UNSET:
            field_dict["lit"] = lit
        if moc_tai is not UNSET:
            field_dict["moc_tai"] = moc_tai
        if xung_tu_dau_cu is not UNSET:
            field_dict["xung_tu_dau_cu"] = xung_tu_dau_cu

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


        def _parse_moc_tai(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                moc_tai_type_0 = datetime.datetime.fromisoformat(data)



                return moc_tai_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        moc_tai = _parse_moc_tai(d.pop("moc_tai", UNSET))


        def _parse_xung_tu_dau_cu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        xung_tu_dau_cu = _parse_xung_tu_dau_cu(d.pop("xung_tu_dau_cu", UNSET))


        iot_lit_phan_chu_ky_dto = cls(
            lit=lit,
            moc_tai=moc_tai,
            xung_tu_dau_cu=xung_tu_dau_cu,
        )

        return iot_lit_phan_chu_ky_dto

