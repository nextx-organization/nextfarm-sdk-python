from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestEudrDdsRequest")



@_attrs_define
class HarvestEudrDdsRequest:
    

    reason: None | str | Unset = UNSET
    reference: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))


        harvest_eudr_dds_request = cls(
            reason=reason,
            reference=reference,
        )

        return harvest_eudr_dds_request

