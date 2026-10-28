from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeSetTaskListTemplateRequest")



@_attrs_define
class OfficeSetTaskListTemplateRequest:
    

    is_template: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_template = self.is_template


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_template is not UNSET:
            field_dict["isTemplate"] = is_template

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_template = d.pop("isTemplate", UNSET)

        office_set_task_list_template_request = cls(
            is_template=is_template,
        )

        return office_set_task_list_template_request

