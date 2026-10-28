from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_connection_key_dto import OfficeConnectionKeyDto





T = TypeVar("T", bound="OfficeConnectionKeyCreatedDto")



@_attrs_define
class OfficeConnectionKeyCreatedDto:
    

    key: OfficeConnectionKeyDto | Unset = UNSET
    plain_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_connection_key_dto import OfficeConnectionKeyDto # noqa: PLC0415
        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        plain_key: None | str | Unset
        if isinstance(self.plain_key, Unset):
            plain_key = UNSET
        else:
            plain_key = self.plain_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if plain_key is not UNSET:
            field_dict["plainKey"] = plain_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_connection_key_dto import OfficeConnectionKeyDto # noqa: PLC0415
        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: OfficeConnectionKeyDto | Unset
        if isinstance(_key,  Unset):
            key = UNSET
        else:
            key = OfficeConnectionKeyDto.from_dict(_key)




        def _parse_plain_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plain_key = _parse_plain_key(d.pop("plainKey", UNSET))


        office_connection_key_created_dto = cls(
            key=key,
            plain_key=plain_key,
        )

        return office_connection_key_created_dto

