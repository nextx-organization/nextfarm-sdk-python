from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="GisCreateSyncTokenRequest")



@_attrs_define
class GisCreateSyncTokenRequest:
    

    zone_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        gis_create_sync_token_request = cls(
            zone_id=zone_id,
        )

        return gis_create_sync_token_request

