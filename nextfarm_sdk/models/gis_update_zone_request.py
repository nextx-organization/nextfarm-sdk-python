from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisUpdateZoneRequest")



@_attrs_define
class GisUpdateZoneRequest:
    

    boundary_geo_json: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    code: None | str | Unset = UNSET
    contact_person: None | str | Unset = UNSET
    contact_phone: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    main_crop: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_zone_id: None | Unset | UUID = UNSET
    zone_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        boundary_geo_json: None | str | Unset
        if isinstance(self.boundary_geo_json, Unset):
            boundary_geo_json = UNSET
        else:
            boundary_geo_json = self.boundary_geo_json

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        contact_person: None | str | Unset
        if isinstance(self.contact_person, Unset):
            contact_person = UNSET
        else:
            contact_person = self.contact_person

        contact_phone: None | str | Unset
        if isinstance(self.contact_phone, Unset):
            contact_phone = UNSET
        else:
            contact_phone = self.contact_phone

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        main_crop: None | str | Unset
        if isinstance(self.main_crop, Unset):
            main_crop = UNSET
        else:
            main_crop = self.main_crop

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_zone_id: None | str | Unset
        if isinstance(self.parent_zone_id, Unset):
            parent_zone_id = UNSET
        elif isinstance(self.parent_zone_id, UUID):
            parent_zone_id = str(self.parent_zone_id)
        else:
            parent_zone_id = self.parent_zone_id

        zone_type: None | str | Unset
        if isinstance(self.zone_type, Unset):
            zone_type = UNSET
        else:
            zone_type = self.zone_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if code is not UNSET:
            field_dict["code"] = code
        if contact_person is not UNSET:
            field_dict["contact_person"] = contact_person
        if contact_phone is not UNSET:
            field_dict["contact_phone"] = contact_phone
        if description is not UNSET:
            field_dict["description"] = description
        if main_crop is not UNSET:
            field_dict["main_crop"] = main_crop
        if name is not UNSET:
            field_dict["name"] = name
        if parent_zone_id is not UNSET:
            field_dict["parent_zone_id"] = parent_zone_id
        if zone_type is not UNSET:
            field_dict["zone_type"] = zone_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_geo_json = _parse_boundary_geo_json(d.pop("boundary_geo_json", UNSET))


        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branch_id", UNSET))


        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_contact_person(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person = _parse_contact_person(d.pop("contact_person", UNSET))


        def _parse_contact_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_phone = _parse_contact_phone(d.pop("contact_phone", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_main_crop(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        main_crop = _parse_main_crop(d.pop("main_crop", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_parent_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_zone_id_type_0 = UUID(data)



                return parent_zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_zone_id = _parse_parent_zone_id(d.pop("parent_zone_id", UNSET))


        def _parse_zone_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone_type = _parse_zone_type(d.pop("zone_type", UNSET))


        gis_update_zone_request = cls(
            boundary_geo_json=boundary_geo_json,
            branch_id=branch_id,
            code=code,
            contact_person=contact_person,
            contact_phone=contact_phone,
            description=description,
            main_crop=main_crop,
            name=name,
            parent_zone_id=parent_zone_id,
            zone_type=zone_type,
        )

        return gis_update_zone_request

