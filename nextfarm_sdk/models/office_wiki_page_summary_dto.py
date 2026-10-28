from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_wiki_page_summary_dto_kind import check_office_wiki_page_summary_dto_kind
from ..models.office_wiki_page_summary_dto_kind import OfficeWikiPageSummaryDtoKind
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeWikiPageSummaryDto")



@_attrs_define
class OfficeWikiPageSummaryDto:
    

    created_by: UUID | Unset = UNSET
    excerpt: None | str | Unset = UNSET
    excerpt_html: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    kind: OfficeWikiPageSummaryDtoKind | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    space_id: None | Unset | UUID = UNSET
    tags: list[str] | None | Unset = UNSET
    title: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    updated_by: None | Unset | UUID = UNSET
    version: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        excerpt: None | str | Unset
        if isinstance(self.excerpt, Unset):
            excerpt = UNSET
        else:
            excerpt = self.excerpt

        excerpt_html: None | str | Unset
        if isinstance(self.excerpt_html, Unset):
            excerpt_html = UNSET
        else:
            excerpt_html = self.excerpt_html

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags


        else:
            tags = self.tags

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

        version = self.version


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt
        if excerpt_html is not UNSET:
            field_dict["excerptHtml"] = excerpt_html
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_by = d.pop("createdBy", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)




        def _parse_excerpt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        excerpt = _parse_excerpt(d.pop("excerpt", UNSET))


        def _parse_excerpt_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        excerpt_html = _parse_excerpt_html(d.pop("excerptHtml", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _kind = d.pop("kind", UNSET)
        kind: OfficeWikiPageSummaryDtoKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = check_office_wiki_page_summary_dto_kind(_kind)




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


        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)



                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updatedBy", UNSET))


        version = d.pop("version", UNSET)

        office_wiki_page_summary_dto = cls(
            created_by=created_by,
            excerpt=excerpt,
            excerpt_html=excerpt_html,
            id=id,
            kind=kind,
            parent_id=parent_id,
            space_id=space_id,
            tags=tags,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            version=version,
        )

        return office_wiki_page_summary_dto

