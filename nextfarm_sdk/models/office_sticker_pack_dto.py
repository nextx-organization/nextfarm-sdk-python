from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_sticker_dto import OfficeStickerDto





T = TypeVar("T", bound="OfficeStickerPackDto")



@_attrs_define
class OfficeStickerPackDto:
    

    can_delete: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    stickers: list[OfficeStickerDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_sticker_dto import OfficeStickerDto # noqa: PLC0415
        can_delete = self.can_delete

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        stickers: list[dict[str, Any]] | None | Unset
        if isinstance(self.stickers, Unset):
            stickers = UNSET
        elif isinstance(self.stickers, list):
            stickers = []
            for stickers_type_0_item_data in self.stickers:
                stickers_type_0_item = stickers_type_0_item_data.to_dict()
                stickers.append(stickers_type_0_item)


        else:
            stickers = self.stickers


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if can_delete is not UNSET:
            field_dict["canDelete"] = can_delete
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if stickers is not UNSET:
            field_dict["stickers"] = stickers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_sticker_dto import OfficeStickerDto # noqa: PLC0415
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


        def _parse_stickers(data: object) -> list[OfficeStickerDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stickers_type_0 = []
                _stickers_type_0 = data
                for stickers_type_0_item_data in (_stickers_type_0):
                    stickers_type_0_item = OfficeStickerDto.from_dict(stickers_type_0_item_data)



                    stickers_type_0.append(stickers_type_0_item)

                return stickers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeStickerDto] | None | Unset, data)

        stickers = _parse_stickers(d.pop("stickers", UNSET))


        office_sticker_pack_dto = cls(
            can_delete=can_delete,
            id=id,
            name=name,
            stickers=stickers,
        )

        return office_sticker_pack_dto

