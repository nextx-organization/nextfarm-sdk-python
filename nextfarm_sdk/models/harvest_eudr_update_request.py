from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestEudrUpdateRequest")



@_attrs_define
class HarvestEudrUpdateRequest:
    

    dds_reference: None | str | Unset = UNSET
    hs_code: None | str | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        dds_reference: None | str | Unset
        if isinstance(self.dds_reference, Unset):
            dds_reference = UNSET
        else:
            dds_reference = self.dds_reference

        hs_code: None | str | Unset
        if isinstance(self.hs_code, Unset):
            hs_code = UNSET
        else:
            hs_code = self.hs_code

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if dds_reference is not UNSET:
            field_dict["dds_reference"] = dds_reference
        if hs_code is not UNSET:
            field_dict["hs_code"] = hs_code
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_dds_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dds_reference = _parse_dds_reference(d.pop("dds_reference", UNSET))


        def _parse_hs_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hs_code = _parse_hs_code(d.pop("hs_code", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        harvest_eudr_update_request = cls(
            dds_reference=dds_reference,
            hs_code=hs_code,
            note=note,
        )

        return harvest_eudr_update_request

