from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeSupportQueueCountsDto")



@_attrs_define
class OfficeSupportQueueCountsDto:
    

    chua_ai_tra_loi: int | Unset = UNSET
    chua_doc: int | Unset = UNSET
    cua_toi: int | Unset = UNSET
    tat_ca: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        chua_ai_tra_loi = self.chua_ai_tra_loi

        chua_doc = self.chua_doc

        cua_toi = self.cua_toi

        tat_ca = self.tat_ca


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if chua_ai_tra_loi is not UNSET:
            field_dict["chuaAiTraLoi"] = chua_ai_tra_loi
        if chua_doc is not UNSET:
            field_dict["chuaDoc"] = chua_doc
        if cua_toi is not UNSET:
            field_dict["cuaToi"] = cua_toi
        if tat_ca is not UNSET:
            field_dict["tatCa"] = tat_ca

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chua_ai_tra_loi = d.pop("chuaAiTraLoi", UNSET)

        chua_doc = d.pop("chuaDoc", UNSET)

        cua_toi = d.pop("cuaToi", UNSET)

        tat_ca = d.pop("tatCa", UNSET)

        office_support_queue_counts_dto = cls(
            chua_ai_tra_loi=chua_ai_tra_loi,
            chua_doc=chua_doc,
            cua_toi=cua_toi,
            tat_ca=tat_ca,
        )

        return office_support_queue_counts_dto

