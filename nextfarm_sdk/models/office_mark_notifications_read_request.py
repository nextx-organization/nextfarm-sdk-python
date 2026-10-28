from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeMarkNotificationsReadRequest")



@_attrs_define
class OfficeMarkNotificationsReadRequest:
    

    ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ids: list[str] | None | Unset
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = []
            for ids_type_0_item_data in self.ids:
                ids_type_0_item = str(ids_type_0_item_data)
                ids.append(ids_type_0_item)


        else:
            ids = self.ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = []
                _ids_type_0 = data
                for ids_type_0_item_data in (_ids_type_0):
                    ids_type_0_item = UUID(ids_type_0_item_data)



                    ids_type_0.append(ids_type_0_item)

                return ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        ids = _parse_ids(d.pop("ids", UNSET))


        office_mark_notifications_read_request = cls(
            ids=ids,
        )

        return office_mark_notifications_read_request

