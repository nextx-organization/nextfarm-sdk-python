from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerCreateApprovalFromMessageRequest")



@_attrs_define
class OfficeChatControllerCreateApprovalFromMessageRequest:
    

    definition_code: None | str | Unset = UNSET
    form_value: None | str | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        definition_code: None | str | Unset
        if isinstance(self.definition_code, Unset):
            definition_code = UNSET
        else:
            definition_code = self.definition_code

        form_value: None | str | Unset
        if isinstance(self.form_value, Unset):
            form_value = UNSET
        else:
            form_value = self.form_value

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if definition_code is not UNSET:
            field_dict["definitionCode"] = definition_code
        if form_value is not UNSET:
            field_dict["formValue"] = form_value
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_definition_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        definition_code = _parse_definition_code(d.pop("definitionCode", UNSET))


        def _parse_form_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_value = _parse_form_value(d.pop("formValue", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_chat_controller_create_approval_from_message_request = cls(
            definition_code=definition_code,
            form_value=form_value,
            title=title,
        )

        return office_chat_controller_create_approval_from_message_request

