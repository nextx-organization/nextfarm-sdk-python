from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeUpdateAnnouncementRequest")



@_attrs_define
class OfficeUpdateAnnouncementRequest:
    

    audience_group_codes: list[str] | None | Unset = UNSET
    category: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    requires_acknowledgement: bool | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        audience_group_codes: list[str] | None | Unset
        if isinstance(self.audience_group_codes, Unset):
            audience_group_codes = UNSET
        elif isinstance(self.audience_group_codes, list):
            audience_group_codes = self.audience_group_codes


        else:
            audience_group_codes = self.audience_group_codes

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        requires_acknowledgement = self.requires_acknowledgement

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if audience_group_codes is not UNSET:
            field_dict["audienceGroupCodes"] = audience_group_codes
        if category is not UNSET:
            field_dict["category"] = category
        if content is not UNSET:
            field_dict["content"] = content
        if requires_acknowledgement is not UNSET:
            field_dict["requiresAcknowledgement"] = requires_acknowledgement
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_audience_group_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                audience_group_codes_type_0 = cast(list[str], data)

                return audience_group_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        audience_group_codes = _parse_audience_group_codes(d.pop("audienceGroupCodes", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        requires_acknowledgement = d.pop("requiresAcknowledgement", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_update_announcement_request = cls(
            audience_group_codes=audience_group_codes,
            category=category,
            content=content,
            requires_acknowledgement=requires_acknowledgement,
            title=title,
        )

        return office_update_announcement_request

