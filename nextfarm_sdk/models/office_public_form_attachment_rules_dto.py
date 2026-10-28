from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficePublicFormAttachmentRulesDto")



@_attrs_define
class OfficePublicFormAttachmentRulesDto:
    

    accept: None | str | Unset = UNSET
    enabled: bool | Unset = UNSET
    max_files: int | Unset = UNSET
    max_mb: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        accept: None | str | Unset
        if isinstance(self.accept, Unset):
            accept = UNSET
        else:
            accept = self.accept

        enabled = self.enabled

        max_files = self.max_files

        max_mb = self.max_mb


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if accept is not UNSET:
            field_dict["accept"] = accept
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_files is not UNSET:
            field_dict["maxFiles"] = max_files
        if max_mb is not UNSET:
            field_dict["maxMb"] = max_mb

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_accept(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accept = _parse_accept(d.pop("accept", UNSET))


        enabled = d.pop("enabled", UNSET)

        max_files = d.pop("maxFiles", UNSET)

        max_mb = d.pop("maxMb", UNSET)

        office_public_form_attachment_rules_dto = cls(
            accept=accept,
            enabled=enabled,
            max_files=max_files,
            max_mb=max_mb,
        )

        return office_public_form_attachment_rules_dto

