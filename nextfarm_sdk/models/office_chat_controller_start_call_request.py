from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatControllerStartCallRequest")



@_attrs_define
class OfficeChatControllerStartCallRequest:
    

    callee_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        callee_ids: list[str] | None | Unset
        if isinstance(self.callee_ids, Unset):
            callee_ids = UNSET
        elif isinstance(self.callee_ids, list):
            callee_ids = []
            for callee_ids_type_0_item_data in self.callee_ids:
                callee_ids_type_0_item = str(callee_ids_type_0_item_data)
                callee_ids.append(callee_ids_type_0_item)


        else:
            callee_ids = self.callee_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if callee_ids is not UNSET:
            field_dict["calleeIds"] = callee_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_callee_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                callee_ids_type_0 = []
                _callee_ids_type_0 = data
                for callee_ids_type_0_item_data in (_callee_ids_type_0):
                    callee_ids_type_0_item = UUID(callee_ids_type_0_item_data)



                    callee_ids_type_0.append(callee_ids_type_0_item)

                return callee_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        callee_ids = _parse_callee_ids(d.pop("calleeIds", UNSET))


        office_chat_controller_start_call_request = cls(
            callee_ids=callee_ids,
        )

        return office_chat_controller_start_call_request

