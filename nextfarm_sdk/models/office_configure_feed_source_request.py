from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeConfigureFeedSourceRequest")



@_attrs_define
class OfficeConfigureFeedSourceRequest:
    

    content_template: None | str | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    title_template: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content_template: None | str | Unset
        if isinstance(self.content_template, Unset):
            content_template = UNSET
        else:
            content_template = self.content_template

        is_enabled = self.is_enabled

        title_template: None | str | Unset
        if isinstance(self.title_template, Unset):
            title_template = UNSET
        else:
            title_template = self.title_template


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_template is not UNSET:
            field_dict["contentTemplate"] = content_template
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if title_template is not UNSET:
            field_dict["titleTemplate"] = title_template

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_content_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_template = _parse_content_template(d.pop("contentTemplate", UNSET))


        is_enabled = d.pop("isEnabled", UNSET)

        def _parse_title_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_template = _parse_title_template(d.pop("titleTemplate", UNSET))


        office_configure_feed_source_request = cls(
            content_template=content_template,
            is_enabled=is_enabled,
            title_template=title_template,
        )

        return office_configure_feed_source_request

