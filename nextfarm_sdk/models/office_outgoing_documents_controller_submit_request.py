from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeOutgoingDocumentsControllerSubmitRequest")



@_attrs_define
class OfficeOutgoingDocumentsControllerSubmitRequest:
    

    approval_definition_code: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        approval_definition_code: None | str | Unset
        if isinstance(self.approval_definition_code, Unset):
            approval_definition_code = UNSET
        else:
            approval_definition_code = self.approval_definition_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if approval_definition_code is not UNSET:
            field_dict["approvalDefinitionCode"] = approval_definition_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_approval_definition_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approval_definition_code = _parse_approval_definition_code(d.pop("approvalDefinitionCode", UNSET))


        office_outgoing_documents_controller_submit_request = cls(
            approval_definition_code=approval_definition_code,
        )

        return office_outgoing_documents_controller_submit_request

