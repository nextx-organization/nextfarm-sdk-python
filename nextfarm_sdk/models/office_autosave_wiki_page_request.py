from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAutosaveWikiPageRequest")



@_attrs_define
class OfficeAutosaveWikiPageRequest:
    

    content: None | str | Unset = UNSET
    expected_content_revision: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        expected_content_revision: int | None | Unset
        if isinstance(self.expected_content_revision, Unset):
            expected_content_revision = UNSET
        else:
            expected_content_revision = self.expected_content_revision


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if expected_content_revision is not UNSET:
            field_dict["expectedContentRevision"] = expected_content_revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_expected_content_revision(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_content_revision = _parse_expected_content_revision(d.pop("expectedContentRevision", UNSET))


        office_autosave_wiki_page_request = cls(
            content=content,
            expected_content_revision=expected_content_revision,
        )

        return office_autosave_wiki_page_request

