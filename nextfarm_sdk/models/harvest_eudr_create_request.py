from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestEudrCreateRequest")



@_attrs_define
class HarvestEudrCreateRequest:
    

    delivery_id: UUID | Unset = UNSET
    hs_code: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        delivery_id: str | Unset = UNSET
        if not isinstance(self.delivery_id, Unset):
            delivery_id = str(self.delivery_id)

        hs_code: None | str | Unset
        if isinstance(self.hs_code, Unset):
            hs_code = UNSET
        else:
            hs_code = self.hs_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if delivery_id is not UNSET:
            field_dict["delivery_id"] = delivery_id
        if hs_code is not UNSET:
            field_dict["hs_code"] = hs_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _delivery_id = d.pop("delivery_id", UNSET)
        delivery_id: UUID | Unset
        if isinstance(_delivery_id,  Unset):
            delivery_id = UNSET
        else:
            delivery_id = UUID(_delivery_id)




        def _parse_hs_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hs_code = _parse_hs_code(d.pop("hs_code", UNSET))


        harvest_eudr_create_request = cls(
            delivery_id=delivery_id,
            hs_code=hs_code,
        )

        return harvest_eudr_create_request

