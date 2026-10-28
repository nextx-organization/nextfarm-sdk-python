from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisFarmerGroupRequest")



@_attrs_define
class GisFarmerGroupRequest:
    

    code: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    leader_farmer_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        is_active = self.is_active

        leader_farmer_id: None | str | Unset
        if isinstance(self.leader_farmer_id, Unset):
            leader_farmer_id = UNSET
        elif isinstance(self.leader_farmer_id, UUID):
            leader_farmer_id = str(self.leader_farmer_id)
        else:
            leader_farmer_id = self.leader_farmer_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if leader_farmer_id is not UNSET:
            field_dict["leader_farmer_id"] = leader_farmer_id
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        is_active = d.pop("is_active", UNSET)

        def _parse_leader_farmer_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                leader_farmer_id_type_0 = UUID(data)



                return leader_farmer_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        leader_farmer_id = _parse_leader_farmer_id(d.pop("leader_farmer_id", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                zone_id_type_0 = UUID(data)



                return zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        zone_id = _parse_zone_id(d.pop("zone_id", UNSET))


        gis_farmer_group_request = cls(
            code=code,
            is_active=is_active,
            leader_farmer_id=leader_farmer_id,
            name=name,
            note=note,
            zone_id=zone_id,
        )

        return gis_farmer_group_request

