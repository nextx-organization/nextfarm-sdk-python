from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCourseLessonDto")



@_attrs_define
class OfficeCourseLessonDto:
    

    content: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_completed: bool | Unset = UNSET
    sort_order: int | Unset = UNSET
    title: None | str | Unset = UNSET
    video_embed_url: None | str | Unset = UNSET
    video_provider: None | str | Unset = UNSET
    video_watch_url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_completed = self.is_completed

        sort_order = self.sort_order

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        video_embed_url: None | str | Unset
        if isinstance(self.video_embed_url, Unset):
            video_embed_url = UNSET
        else:
            video_embed_url = self.video_embed_url

        video_provider: None | str | Unset
        if isinstance(self.video_provider, Unset):
            video_provider = UNSET
        else:
            video_provider = self.video_provider

        video_watch_url: None | str | Unset
        if isinstance(self.video_watch_url, Unset):
            video_watch_url = UNSET
        else:
            video_watch_url = self.video_watch_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if id is not UNSET:
            field_dict["id"] = id
        if is_completed is not UNSET:
            field_dict["isCompleted"] = is_completed
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if title is not UNSET:
            field_dict["title"] = title
        if video_embed_url is not UNSET:
            field_dict["videoEmbedUrl"] = video_embed_url
        if video_provider is not UNSET:
            field_dict["videoProvider"] = video_provider
        if video_watch_url is not UNSET:
            field_dict["videoWatchUrl"] = video_watch_url

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


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_completed = d.pop("isCompleted", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_video_embed_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_embed_url = _parse_video_embed_url(d.pop("videoEmbedUrl", UNSET))


        def _parse_video_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_provider = _parse_video_provider(d.pop("videoProvider", UNSET))


        def _parse_video_watch_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_watch_url = _parse_video_watch_url(d.pop("videoWatchUrl", UNSET))


        office_course_lesson_dto = cls(
            content=content,
            id=id,
            is_completed=is_completed,
            sort_order=sort_order,
            title=title,
            video_embed_url=video_embed_url,
            video_provider=video_provider,
            video_watch_url=video_watch_url,
        )

        return office_course_lesson_dto

