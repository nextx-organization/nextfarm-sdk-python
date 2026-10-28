from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAddChannelMembersResultDto")



@_attrs_define
class OfficeAddChannelMembersResultDto:
    

    added: int | Unset = UNSET
    pending: int | Unset = UNSET
    request_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        added = self.added

        pending = self.pending

        request_ids: list[str] | None | Unset
        if isinstance(self.request_ids, Unset):
            request_ids = UNSET
        elif isinstance(self.request_ids, list):
            request_ids = []
            for request_ids_type_0_item_data in self.request_ids:
                request_ids_type_0_item = str(request_ids_type_0_item_data)
                request_ids.append(request_ids_type_0_item)


        else:
            request_ids = self.request_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if added is not UNSET:
            field_dict["added"] = added
        if pending is not UNSET:
            field_dict["pending"] = pending
        if request_ids is not UNSET:
            field_dict["requestIds"] = request_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added = d.pop("added", UNSET)

        pending = d.pop("pending", UNSET)

        def _parse_request_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                request_ids_type_0 = []
                _request_ids_type_0 = data
                for request_ids_type_0_item_data in (_request_ids_type_0):
                    request_ids_type_0_item = UUID(request_ids_type_0_item_data)



                    request_ids_type_0.append(request_ids_type_0_item)

                return request_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        request_ids = _parse_request_ids(d.pop("requestIds", UNSET))


        office_add_channel_members_result_dto = cls(
            added=added,
            pending=pending,
            request_ids=request_ids,
        )

        return office_add_channel_members_result_dto

