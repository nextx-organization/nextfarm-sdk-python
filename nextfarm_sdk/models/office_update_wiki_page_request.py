from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeUpdateWikiPageRequest")



@_attrs_define
class OfficeUpdateWikiPageRequest:
    

    change_note: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    expected_content_revision: int | None | Unset = UNSET
    expected_version: int | None | Unset = UNSET
    live_session: bool | None | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        change_note: None | str | Unset
        if isinstance(self.change_note, Unset):
            change_note = UNSET
        else:
            change_note = self.change_note

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

        expected_version: int | None | Unset
        if isinstance(self.expected_version, Unset):
            expected_version = UNSET
        else:
            expected_version = self.expected_version

        live_session: bool | None | Unset
        if isinstance(self.live_session, Unset):
            live_session = UNSET
        else:
            live_session = self.live_session

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if change_note is not UNSET:
            field_dict["changeNote"] = change_note
        if content is not UNSET:
            field_dict["content"] = content
        if expected_content_revision is not UNSET:
            field_dict["expectedContentRevision"] = expected_content_revision
        if expected_version is not UNSET:
            field_dict["expectedVersion"] = expected_version
        if live_session is not UNSET:
            field_dict["liveSession"] = live_session
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_change_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        change_note = _parse_change_note(d.pop("changeNote", UNSET))


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


        def _parse_expected_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_version = _parse_expected_version(d.pop("expectedVersion", UNSET))


        def _parse_live_session(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        live_session = _parse_live_session(d.pop("liveSession", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_update_wiki_page_request = cls(
            change_note=change_note,
            content=content,
            expected_content_revision=expected_content_revision,
            expected_version=expected_version,
            live_session=live_session,
            title=title,
        )

        return office_update_wiki_page_request

