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






T = TypeVar("T", bound="HarvestCreateQrCodesRequest")



@_attrs_define
class HarvestCreateQrCodesRequest:
    

    effective_to: datetime.date | Unset = UNSET
    harvest_date: datetime.date | Unset = UNSET
    harvest_record_id: None | Unset | UUID = UNSET
    quantity: int | Unset = UNSET
    season_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        effective_to: str | Unset = UNSET
        if not isinstance(self.effective_to, Unset):
            effective_to = self.effective_to.isoformat()

        harvest_date: str | Unset = UNSET
        if not isinstance(self.harvest_date, Unset):
            harvest_date = self.harvest_date.isoformat()

        harvest_record_id: None | str | Unset
        if isinstance(self.harvest_record_id, Unset):
            harvest_record_id = UNSET
        elif isinstance(self.harvest_record_id, UUID):
            harvest_record_id = str(self.harvest_record_id)
        else:
            harvest_record_id = self.harvest_record_id

        quantity = self.quantity

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if effective_to is not UNSET:
            field_dict["effective_to"] = effective_to
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if harvest_record_id is not UNSET:
            field_dict["harvest_record_id"] = harvest_record_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if season_id is not UNSET:
            field_dict["season_id"] = season_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _effective_to = d.pop("effective_to", UNSET)
        effective_to: datetime.date | Unset
        if isinstance(_effective_to,  Unset):
            effective_to = UNSET
        else:
            effective_to = datetime.date.fromisoformat(_effective_to)




        _harvest_date = d.pop("harvest_date", UNSET)
        harvest_date: datetime.date | Unset
        if isinstance(_harvest_date,  Unset):
            harvest_date = UNSET
        else:
            harvest_date = datetime.date.fromisoformat(_harvest_date)




        def _parse_harvest_record_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                harvest_record_id_type_0 = UUID(data)



                return harvest_record_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        harvest_record_id = _parse_harvest_record_id(d.pop("harvest_record_id", UNSET))


        quantity = d.pop("quantity", UNSET)

        def _parse_season_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_id_type_0 = UUID(data)



                return season_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        season_id = _parse_season_id(d.pop("season_id", UNSET))


        harvest_create_qr_codes_request = cls(
            effective_to=effective_to,
            harvest_date=harvest_date,
            harvest_record_id=harvest_record_id,
            quantity=quantity,
            season_id=season_id,
        )

        return harvest_create_qr_codes_request

