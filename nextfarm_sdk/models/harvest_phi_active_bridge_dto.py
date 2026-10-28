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






T = TypeVar("T", bound="HarvestPhiActiveBridgeDto")



@_attrs_define
class HarvestPhiActiveBridgeDto:
    

    parcel_id: UUID | Unset = UNSET
    safe_from: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        safe_from: str | Unset = UNSET
        if not isinstance(self.safe_from, Unset):
            safe_from = self.safe_from.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if safe_from is not UNSET:
            field_dict["safe_from"] = safe_from

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        _safe_from = d.pop("safe_from", UNSET)
        safe_from: datetime.date | Unset
        if isinstance(_safe_from,  Unset):
            safe_from = UNSET
        else:
            safe_from = datetime.date.fromisoformat(_safe_from)




        harvest_phi_active_bridge_dto = cls(
            parcel_id=parcel_id,
            safe_from=safe_from,
        )

        return harvest_phi_active_bridge_dto

