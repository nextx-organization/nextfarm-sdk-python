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






T = TypeVar("T", bound="GisCareGenerationDto")



@_attrs_define
class GisCareGenerationDto:
    

    activation_id: UUID | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    delivery: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    item_count: int | Unset = UNSET
    week_end: None | str | Unset = UNSET
    week_start: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        activation_id: str | Unset = UNSET
        if not isinstance(self.activation_id, Unset):
            activation_id = str(self.activation_id)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        delivery: None | str | Unset
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        else:
            delivery = self.delivery

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        item_count = self.item_count

        week_end: None | str | Unset
        if isinstance(self.week_end, Unset):
            week_end = UNSET
        else:
            week_end = self.week_end

        week_start: None | str | Unset
        if isinstance(self.week_start, Unset):
            week_start = UNSET
        else:
            week_start = self.week_start


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if activation_id is not UNSET:
            field_dict["activation_id"] = activation_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if id is not UNSET:
            field_dict["id"] = id
        if item_count is not UNSET:
            field_dict["item_count"] = item_count
        if week_end is not UNSET:
            field_dict["week_end"] = week_end
        if week_start is not UNSET:
            field_dict["week_start"] = week_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _activation_id = d.pop("activation_id", UNSET)
        activation_id: UUID | Unset
        if isinstance(_activation_id,  Unset):
            activation_id = UNSET
        else:
            activation_id = UUID(_activation_id)




        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_delivery(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        item_count = d.pop("item_count", UNSET)

        def _parse_week_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        week_end = _parse_week_end(d.pop("week_end", UNSET))


        def _parse_week_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        week_start = _parse_week_start(d.pop("week_start", UNSET))


        gis_care_generation_dto = cls(
            activation_id=activation_id,
            created_at=created_at,
            delivery=delivery,
            id=id,
            item_count=item_count,
            week_end=week_end,
            week_start=week_start,
        )

        return gis_care_generation_dto

