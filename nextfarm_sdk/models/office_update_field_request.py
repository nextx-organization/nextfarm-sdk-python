from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeUpdateFieldRequest")



@_attrs_define
class OfficeUpdateFieldRequest:
    

    description: None | str | Unset = UNSET
    is_hidden: bool | None | Unset = UNSET
    is_primary: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    property_: None | str | Unset = UNSET
    type_: int | None | Unset = UNSET
    ui_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_hidden: bool | None | Unset
        if isinstance(self.is_hidden, Unset):
            is_hidden = UNSET
        else:
            is_hidden = self.is_hidden

        is_primary: bool | None | Unset
        if isinstance(self.is_primary, Unset):
            is_primary = UNSET
        else:
            is_primary = self.is_primary

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        property_: None | str | Unset
        if isinstance(self.property_, Unset):
            property_ = UNSET
        else:
            property_ = self.property_

        type_: int | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        ui_type: None | str | Unset
        if isinstance(self.ui_type, Unset):
            ui_type = UNSET
        else:
            ui_type = self.ui_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if property_ is not UNSET:
            field_dict["property"] = property_
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ui_type is not UNSET:
            field_dict["uiType"] = ui_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_is_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_hidden = _parse_is_hidden(d.pop("isHidden", UNSET))


        def _parse_is_primary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_primary = _parse_is_primary(d.pop("isPrimary", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))


        def _parse_property_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_ = _parse_property_(d.pop("property", UNSET))


        def _parse_type_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_ui_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ui_type = _parse_ui_type(d.pop("uiType", UNSET))


        office_update_field_request = cls(
            description=description,
            is_hidden=is_hidden,
            is_primary=is_primary,
            name=name,
            position=position,
            property_=property_,
            type_=type_,
            ui_type=ui_type,
        )

        return office_update_field_request

