from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCreateHandoverRequest")



@_attrs_define
class OfficeCreateHandoverRequest:
    

    asset_id: UUID | Unset = UNSET
    condition: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    to_user_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        condition: None | str | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        to_user_id: None | str | Unset
        if isinstance(self.to_user_id, Unset):
            to_user_id = UNSET
        elif isinstance(self.to_user_id, UUID):
            to_user_id = str(self.to_user_id)
        else:
            to_user_id = self.to_user_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if condition is not UNSET:
            field_dict["condition"] = condition
        if note is not UNSET:
            field_dict["note"] = note
        if to_user_id is not UNSET:
            field_dict["toUserId"] = to_user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _asset_id = d.pop("assetId", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id,  Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)




        def _parse_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_to_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_user_id_type_0 = UUID(data)



                return to_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        to_user_id = _parse_to_user_id(d.pop("toUserId", UNSET))


        office_create_handover_request = cls(
            asset_id=asset_id,
            condition=condition,
            note=note,
            to_user_id=to_user_id,
        )

        return office_create_handover_request

