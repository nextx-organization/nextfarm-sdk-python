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

if TYPE_CHECKING:
  from ..models.harvest_phi_block_dto import HarvestPhiBlockDto





T = TypeVar("T", bound="HarvestPhiStatusDto")



@_attrs_define
class HarvestPhiStatusDto:
    

    active: bool | Unset = UNSET
    blocking: HarvestPhiBlockDto | Unset = UNSET
    on_date: datetime.date | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    safe_from: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_phi_block_dto import HarvestPhiBlockDto # noqa: PLC0415
        active = self.active

        blocking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blocking, Unset):
            blocking = self.blocking.to_dict()

        on_date: str | Unset = UNSET
        if not isinstance(self.on_date, Unset):
            on_date = self.on_date.isoformat()

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        safe_from: None | str | Unset
        if isinstance(self.safe_from, Unset):
            safe_from = UNSET
        elif isinstance(self.safe_from, datetime.date):
            safe_from = self.safe_from.isoformat()
        else:
            safe_from = self.safe_from


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active is not UNSET:
            field_dict["active"] = active
        if blocking is not UNSET:
            field_dict["blocking"] = blocking
        if on_date is not UNSET:
            field_dict["on_date"] = on_date
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if safe_from is not UNSET:
            field_dict["safe_from"] = safe_from

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_phi_block_dto import HarvestPhiBlockDto # noqa: PLC0415
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        _blocking = d.pop("blocking", UNSET)
        blocking: HarvestPhiBlockDto | Unset
        if isinstance(_blocking,  Unset):
            blocking = UNSET
        else:
            blocking = HarvestPhiBlockDto.from_dict(_blocking)




        _on_date = d.pop("on_date", UNSET)
        on_date: datetime.date | Unset
        if isinstance(_on_date,  Unset):
            on_date = UNSET
        else:
            on_date = datetime.date.fromisoformat(_on_date)




        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        def _parse_safe_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                safe_from_type_0 = datetime.date.fromisoformat(data)



                return safe_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        safe_from = _parse_safe_from(d.pop("safe_from", UNSET))


        harvest_phi_status_dto = cls(
            active=active,
            blocking=blocking,
            on_date=on_date,
            parcel_id=parcel_id,
            safe_from=safe_from,
        )

        return harvest_phi_status_dto

