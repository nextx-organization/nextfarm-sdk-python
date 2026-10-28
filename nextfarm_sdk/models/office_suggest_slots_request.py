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






T = TypeVar("T", bound="OfficeSuggestSlotsRequest")



@_attrs_define
class OfficeSuggestSlotsRequest:
    

    duration_minutes: int | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    room_ids: list[UUID] | None | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    user_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        duration_minutes = self.duration_minutes

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        room_ids: list[str] | None | Unset
        if isinstance(self.room_ids, Unset):
            room_ids = UNSET
        elif isinstance(self.room_ids, list):
            room_ids = []
            for room_ids_type_0_item_data in self.room_ids:
                room_ids_type_0_item = str(room_ids_type_0_item_data)
                room_ids.append(room_ids_type_0_item)


        else:
            room_ids = self.room_ids

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        user_ids: list[str] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = []
            for user_ids_type_0_item_data in self.user_ids:
                user_ids_type_0_item = str(user_ids_type_0_item_data)
                user_ids.append(user_ids_type_0_item)


        else:
            user_ids = self.user_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if duration_minutes is not UNSET:
            field_dict["durationMinutes"] = duration_minutes
        if from_ is not UNSET:
            field_dict["from"] = from_
        if room_ids is not UNSET:
            field_dict["roomIds"] = room_ids
        if to is not UNSET:
            field_dict["to"] = to
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_minutes = d.pop("durationMinutes", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.datetime.fromisoformat(_from_)




        def _parse_room_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                room_ids_type_0 = []
                _room_ids_type_0 = data
                for room_ids_type_0_item_data in (_room_ids_type_0):
                    room_ids_type_0_item = UUID(room_ids_type_0_item_data)



                    room_ids_type_0.append(room_ids_type_0_item)

                return room_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        room_ids = _parse_room_ids(d.pop("roomIds", UNSET))


        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.datetime.fromisoformat(_to)




        def _parse_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = []
                _user_ids_type_0 = data
                for user_ids_type_0_item_data in (_user_ids_type_0):
                    user_ids_type_0_item = UUID(user_ids_type_0_item_data)



                    user_ids_type_0.append(user_ids_type_0_item)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("userIds", UNSET))


        office_suggest_slots_request = cls(
            duration_minutes=duration_minutes,
            from_=from_,
            room_ids=room_ids,
            to=to,
            user_ids=user_ids,
        )

        return office_suggest_slots_request

