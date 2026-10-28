from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeApprovalsControllerAddSignRequest")



@_attrs_define
class OfficeApprovalsControllerAddSignRequest:
    

    approver_ids: list[UUID] | None | Unset = UNSET
    mode: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        approver_ids: list[str] | None | Unset
        if isinstance(self.approver_ids, Unset):
            approver_ids = UNSET
        elif isinstance(self.approver_ids, list):
            approver_ids = []
            for approver_ids_type_0_item_data in self.approver_ids:
                approver_ids_type_0_item = str(approver_ids_type_0_item_data)
                approver_ids.append(approver_ids_type_0_item)


        else:
            approver_ids = self.approver_ids

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if approver_ids is not UNSET:
            field_dict["approverIds"] = approver_ids
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_approver_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                approver_ids_type_0 = []
                _approver_ids_type_0 = data
                for approver_ids_type_0_item_data in (_approver_ids_type_0):
                    approver_ids_type_0_item = UUID(approver_ids_type_0_item_data)



                    approver_ids_type_0.append(approver_ids_type_0_item)

                return approver_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        approver_ids = _parse_approver_ids(d.pop("approverIds", UNSET))


        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        office_approvals_controller_add_sign_request = cls(
            approver_ids=approver_ids,
            mode=mode,
        )

        return office_approvals_controller_add_sign_request

