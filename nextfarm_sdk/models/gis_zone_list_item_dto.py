from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisZoneListItemDto")



@_attrs_define
class GisZoneListItemDto:
    

    code: None | str | Unset = UNSET
    contact_person: None | str | Unset = UNSET
    contact_phone: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    implausible_parcel_count: int | None | Unset = UNSET
    main_crop: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    parcel_area_ha: float | None | Unset = UNSET
    parcel_count: int | None | Unset = UNSET
    parent_zone_id: None | Unset | UUID = UNSET
    total_area_ha: float | None | Unset = UNSET
    zone_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        implausible_parcel_count: int | None | Unset
        if isinstance(self.implausible_parcel_count, Unset):
            implausible_parcel_count = UNSET
        else:
            implausible_parcel_count = self.implausible_parcel_count

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

        parcel_area_ha: float | None | Unset
        if isinstance(self.parcel_area_ha, Unset):
            parcel_area_ha = UNSET
        else:
            parcel_area_ha = self.parcel_area_ha

        parcel_count: int | None | Unset
        if isinstance(self.parcel_count, Unset):
            parcel_count = UNSET
        else:
            parcel_count = self.parcel_count

        parent_zone_id: None | str | Unset
        if isinstance(self.parent_zone_id, Unset):
            parent_zone_id = UNSET
        elif isinstance(self.parent_zone_id, UUID):
            parent_zone_id = str(self.parent_zone_id)
        else:
            parent_zone_id = self.parent_zone_id

        total_area_ha: float | None | Unset
        if isinstance(self.total_area_ha, Unset):
            total_area_ha = UNSET
        else:
            total_area_ha = self.total_area_ha

        zone_type: None | str | Unset
        if isinstance(self.zone_type, Unset):
            zone_type = UNSET
        else:
            zone_type = self.zone_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if contact_person is not UNSET:
            field_dict["contact_person"] = contact_person
        if contact_phone is not UNSET:
            field_dict["contact_phone"] = contact_phone
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if implausible_parcel_count is not UNSET:
            field_dict["implausible_parcel_count"] = implausible_parcel_count
        if main_crop is not UNSET:
            field_dict["main_crop"] = main_crop
        if name is not UNSET:
            field_dict["name"] = name
        if parcel_area_ha is not UNSET:
            field_dict["parcel_area_ha"] = parcel_area_ha
        if parcel_count is not UNSET:
            field_dict["parcel_count"] = parcel_count
        if parent_zone_id is not UNSET:
            field_dict["parent_zone_id"] = parent_zone_id
        if total_area_ha is not UNSET:
            field_dict["total_area_ha"] = total_area_ha
        if zone_type is not UNSET:
            field_dict["zone_type"] = zone_type

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


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_implausible_parcel_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        implausible_parcel_count = _parse_implausible_parcel_count(d.pop("implausible_parcel_count", UNSET))


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


        def _parse_parcel_area_ha(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        parcel_area_ha = _parse_parcel_area_ha(d.pop("parcel_area_ha", UNSET))


        def _parse_parcel_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parcel_count = _parse_parcel_count(d.pop("parcel_count", UNSET))


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


        def _parse_total_area_ha(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_area_ha = _parse_total_area_ha(d.pop("total_area_ha", UNSET))


        def _parse_zone_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone_type = _parse_zone_type(d.pop("zone_type", UNSET))


        gis_zone_list_item_dto = cls(
            code=code,
            contact_person=contact_person,
            contact_phone=contact_phone,
            description=description,
            id=id,
            implausible_parcel_count=implausible_parcel_count,
            main_crop=main_crop,
            name=name,
            parcel_area_ha=parcel_area_ha,
            parcel_count=parcel_count,
            parent_zone_id=parent_zone_id,
            total_area_ha=total_area_ha,
            zone_type=zone_type,
        )

        return gis_zone_list_item_dto

