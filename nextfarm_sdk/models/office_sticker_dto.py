from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeStickerDto")



@_attrs_define
class OfficeStickerDto:
    

    can_delete: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    pack_id: UUID | Unset = UNSET
    url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        can_delete = self.can_delete

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        pack_id: str | Unset = UNSET
        if not isinstance(self.pack_id, Unset):
            pack_id = str(self.pack_id)

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if can_delete is not UNSET:
            field_dict["canDelete"] = can_delete
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if pack_id is not UNSET:
            field_dict["packId"] = pack_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_delete = d.pop("canDelete", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _pack_id = d.pop("packId", UNSET)
        pack_id: UUID | Unset
        if isinstance(_pack_id,  Unset):
            pack_id = UNSET
        else:
            pack_id = UUID(_pack_id)




        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        office_sticker_dto = cls(
            can_delete=can_delete,
            id=id,
            name=name,
            pack_id=pack_id,
            url=url,
        )

        return office_sticker_dto

