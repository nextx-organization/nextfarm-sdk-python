from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="HarvestCertMemberInput")



@_attrs_define
class HarvestCertMemberInput:
    

    farmer_id: UUID | Unset = UNSET
    farmer_name: None | str | Unset = UNSET
    joined_on: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        farmer_id: str | Unset = UNSET
        if not isinstance(self.farmer_id, Unset):
            farmer_id = str(self.farmer_id)

        farmer_name: None | str | Unset
        if isinstance(self.farmer_name, Unset):
            farmer_name = UNSET
        else:
            farmer_name = self.farmer_name

        joined_on: None | str | Unset
        if isinstance(self.joined_on, Unset):
            joined_on = UNSET
        elif isinstance(self.joined_on, datetime.date):
            joined_on = self.joined_on.isoformat()
        else:
            joined_on = self.joined_on


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if farmer_id is not UNSET:
            field_dict["farmer_id"] = farmer_id
        if farmer_name is not UNSET:
            field_dict["farmer_name"] = farmer_name
        if joined_on is not UNSET:
            field_dict["joined_on"] = joined_on

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _farmer_id = d.pop("farmer_id", UNSET)
        farmer_id: UUID | Unset
        if isinstance(_farmer_id,  Unset):
            farmer_id = UNSET
        else:
            farmer_id = UUID(_farmer_id)




        def _parse_farmer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        farmer_name = _parse_farmer_name(d.pop("farmer_name", UNSET))


        def _parse_joined_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                joined_on_type_0 = datetime.date.fromisoformat(data)



                return joined_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        joined_on = _parse_joined_on(d.pop("joined_on", UNSET))


        harvest_cert_member_input = cls(
            farmer_id=farmer_id,
            farmer_name=farmer_name,
            joined_on=joined_on,
        )

        return harvest_cert_member_input

