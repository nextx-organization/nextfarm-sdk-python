from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeViewDto")



@_attrs_define
class OfficeViewDto:
    

    id: UUID | Unset = UNSET
    is_public: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    property_: None | str | Unset = UNSET
    public_token: None | str | Unset = UNSET
    table_id: UUID | Unset = UNSET
    view_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_public = self.is_public

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        property_: None | str | Unset
        if isinstance(self.property_, Unset):
            property_ = UNSET
        else:
            property_ = self.property_

        public_token: None | str | Unset
        if isinstance(self.public_token, Unset):
            public_token = UNSET
        else:
            public_token = self.public_token

        table_id: str | Unset = UNSET
        if not isinstance(self.table_id, Unset):
            table_id = str(self.table_id)

        view_type: None | str | Unset
        if isinstance(self.view_type, Unset):
            view_type = UNSET
        else:
            view_type = self.view_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if property_ is not UNSET:
            field_dict["property"] = property_
        if public_token is not UNSET:
            field_dict["publicToken"] = public_token
        if table_id is not UNSET:
            field_dict["tableId"] = table_id
        if view_type is not UNSET:
            field_dict["viewType"] = view_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_public = d.pop("isPublic", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_property_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_ = _parse_property_(d.pop("property", UNSET))


        def _parse_public_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_token = _parse_public_token(d.pop("publicToken", UNSET))


        _table_id = d.pop("tableId", UNSET)
        table_id: UUID | Unset
        if isinstance(_table_id,  Unset):
            table_id = UNSET
        else:
            table_id = UUID(_table_id)




        def _parse_view_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view_type = _parse_view_type(d.pop("viewType", UNSET))


        office_view_dto = cls(
            id=id,
            is_public=is_public,
            name=name,
            property_=property_,
            public_token=public_token,
            table_id=table_id,
            view_type=view_type,
        )

        return office_view_dto

