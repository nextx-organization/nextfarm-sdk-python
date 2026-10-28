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






T = TypeVar("T", bound="HarvestEudrDeliveryStatusDto")



@_attrs_define
class HarvestEudrDeliveryStatusDto:
    

    content_hash: None | str | Unset = UNSET
    dossier_id: UUID | Unset = UNSET
    locked_at: datetime.datetime | None | Unset = UNSET
    net_kg: float | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content_hash: None | str | Unset
        if isinstance(self.content_hash, Unset):
            content_hash = UNSET
        else:
            content_hash = self.content_hash

        dossier_id: str | Unset = UNSET
        if not isinstance(self.dossier_id, Unset):
            dossier_id = str(self.dossier_id)

        locked_at: None | str | Unset
        if isinstance(self.locked_at, Unset):
            locked_at = UNSET
        elif isinstance(self.locked_at, datetime.datetime):
            locked_at = self.locked_at.isoformat()
        else:
            locked_at = self.locked_at

        net_kg = self.net_kg

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash
        if dossier_id is not UNSET:
            field_dict["dossier_id"] = dossier_id
        if locked_at is not UNSET:
            field_dict["locked_at"] = locked_at
        if net_kg is not UNSET:
            field_dict["net_kg"] = net_kg
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_hash = _parse_content_hash(d.pop("content_hash", UNSET))


        _dossier_id = d.pop("dossier_id", UNSET)
        dossier_id: UUID | Unset
        if isinstance(_dossier_id,  Unset):
            dossier_id = UNSET
        else:
            dossier_id = UUID(_dossier_id)




        def _parse_locked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locked_at_type_0 = datetime.datetime.fromisoformat(data)



                return locked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        locked_at = _parse_locked_at(d.pop("locked_at", UNSET))


        net_kg = d.pop("net_kg", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        harvest_eudr_delivery_status_dto = cls(
            content_hash=content_hash,
            dossier_id=dossier_id,
            locked_at=locked_at,
            net_kg=net_kg,
            status=status,
        )

        return harvest_eudr_delivery_status_dto

