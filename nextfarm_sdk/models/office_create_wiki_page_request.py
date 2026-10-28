from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_create_wiki_page_request_kind import check_office_create_wiki_page_request_kind
from ..models.office_create_wiki_page_request_kind import OfficeCreateWikiPageRequestKind
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCreateWikiPageRequest")



@_attrs_define
class OfficeCreateWikiPageRequest:
    

    content: None | str | Unset = UNSET
    kind: OfficeCreateWikiPageRequestKind | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    space_id: None | Unset | UUID = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind


        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        space_id: None | str | Unset
        if isinstance(self.space_id, Unset):
            space_id = UNSET
        elif isinstance(self.space_id, UUID):
            space_id = str(self.space_id)
        else:
            space_id = self.space_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if kind is not UNSET:
            field_dict["kind"] = kind
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id
        if title is not UNSET:
            field_dict["title"] = title

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


        _kind = d.pop("kind", UNSET)
        kind: OfficeCreateWikiPageRequestKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = check_office_create_wiki_page_request_kind(_kind)




        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)



                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        def _parse_space_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                space_id_type_0 = UUID(data)



                return space_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        space_id = _parse_space_id(d.pop("spaceId", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_create_wiki_page_request = cls(
            content=content,
            kind=kind,
            parent_id=parent_id,
            space_id=space_id,
            title=title,
        )

        return office_create_wiki_page_request

