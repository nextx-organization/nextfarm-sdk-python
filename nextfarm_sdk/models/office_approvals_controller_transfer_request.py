from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeApprovalsControllerTransferRequest")



@_attrs_define
class OfficeApprovalsControllerTransferRequest:
    

    comment: None | str | Unset = UNSET
    receiver_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        receiver_id: str | Unset = UNSET
        if not isinstance(self.receiver_id, Unset):
            receiver_id = str(self.receiver_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if comment is not UNSET:
            field_dict["comment"] = comment
        if receiver_id is not UNSET:
            field_dict["receiverId"] = receiver_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        _receiver_id = d.pop("receiverId", UNSET)
        receiver_id: UUID | Unset
        if isinstance(_receiver_id,  Unset):
            receiver_id = UNSET
        else:
            receiver_id = UUID(_receiver_id)




        office_approvals_controller_transfer_request = cls(
            comment=comment,
            receiver_id=receiver_id,
        )

        return office_approvals_controller_transfer_request

