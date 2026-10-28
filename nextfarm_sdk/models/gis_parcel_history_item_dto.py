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






T = TypeVar("T", bound="GisParcelHistoryItemDto")



@_attrs_define
class GisParcelHistoryItemDto:
    

    change_type: None | str | Unset = UNSET
    changed_at: datetime.datetime | Unset = UNSET
    changed_by: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    new_boundary_geo_json: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    old_boundary_geo_json: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        change_type: None | str | Unset
        if isinstance(self.change_type, Unset):
            change_type = UNSET
        else:
            change_type = self.change_type

        changed_at: str | Unset = UNSET
        if not isinstance(self.changed_at, Unset):
            changed_at = self.changed_at.isoformat()

        changed_by: str | Unset = UNSET
        if not isinstance(self.changed_by, Unset):
            changed_by = str(self.changed_by)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        new_boundary_geo_json: None | str | Unset
        if isinstance(self.new_boundary_geo_json, Unset):
            new_boundary_geo_json = UNSET
        else:
            new_boundary_geo_json = self.new_boundary_geo_json

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        old_boundary_geo_json: None | str | Unset
        if isinstance(self.old_boundary_geo_json, Unset):
            old_boundary_geo_json = UNSET
        else:
            old_boundary_geo_json = self.old_boundary_geo_json

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if change_type is not UNSET:
            field_dict["change_type"] = change_type
        if changed_at is not UNSET:
            field_dict["changed_at"] = changed_at
        if changed_by is not UNSET:
            field_dict["changed_by"] = changed_by
        if id is not UNSET:
            field_dict["id"] = id
        if new_boundary_geo_json is not UNSET:
            field_dict["new_boundary_geo_json"] = new_boundary_geo_json
        if notes is not UNSET:
            field_dict["notes"] = notes
        if old_boundary_geo_json is not UNSET:
            field_dict["old_boundary_geo_json"] = old_boundary_geo_json
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_change_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        change_type = _parse_change_type(d.pop("change_type", UNSET))


        _changed_at = d.pop("changed_at", UNSET)
        changed_at: datetime.datetime | Unset
        if isinstance(_changed_at,  Unset):
            changed_at = UNSET
        else:
            changed_at = datetime.datetime.fromisoformat(_changed_at)




        _changed_by = d.pop("changed_by", UNSET)
        changed_by: UUID | Unset
        if isinstance(_changed_by,  Unset):
            changed_by = UNSET
        else:
            changed_by = UUID(_changed_by)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_new_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_boundary_geo_json = _parse_new_boundary_geo_json(d.pop("new_boundary_geo_json", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_old_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_boundary_geo_json = _parse_old_boundary_geo_json(d.pop("old_boundary_geo_json", UNSET))


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        gis_parcel_history_item_dto = cls(
            change_type=change_type,
            changed_at=changed_at,
            changed_by=changed_by,
            id=id,
            new_boundary_geo_json=new_boundary_geo_json,
            notes=notes,
            old_boundary_geo_json=old_boundary_geo_json,
            parcel_id=parcel_id,
        )

        return gis_parcel_history_item_dto

