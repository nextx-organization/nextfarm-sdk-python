from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.office_announcement_attachment_dto import OfficeAnnouncementAttachmentDto
  from ..models.office_announcement_comment_preview_dto import OfficeAnnouncementCommentPreviewDto
  from ..models.office_announcement_dto_reaction_counts_type_0 import OfficeAnnouncementDtoReactionCountsType0





T = TypeVar("T", bound="OfficeAnnouncementDto")



@_attrs_define
class OfficeAnnouncementDto:
    

    acknowledged_count: int | Unset = UNSET
    attachments: list[OfficeAnnouncementAttachmentDto] | None | Unset = UNSET
    audience_group_codes: list[str] | None | Unset = UNSET
    author_id: UUID | Unset = UNSET
    auto_source: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    comment_count: int | Unset = UNSET
    content: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    is_acknowledged: bool | Unset = UNSET
    is_liked: bool | Unset = UNSET
    is_pinned: bool | Unset = UNSET
    is_read: bool | Unset = UNSET
    is_saved: bool | Unset = UNSET
    latest_comments: list[OfficeAnnouncementCommentPreviewDto] | None | Unset = UNSET
    like_count: int | Unset = UNSET
    my_reaction: None | str | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    reaction_counts: None | OfficeAnnouncementDtoReactionCountsType0 | Unset = UNSET
    read_count: int | Unset = UNSET
    requires_acknowledgement: bool | Unset = UNSET
    share_count: int | Unset = UNSET
    status: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_announcement_attachment_dto import OfficeAnnouncementAttachmentDto # noqa: PLC0415
        from ..models.office_announcement_comment_preview_dto import OfficeAnnouncementCommentPreviewDto # noqa: PLC0415
        from ..models.office_announcement_dto_reaction_counts_type_0 import OfficeAnnouncementDtoReactionCountsType0 # noqa: PLC0415
        acknowledged_count = self.acknowledged_count

        attachments: list[dict[str, Any]] | None | Unset
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)


        else:
            attachments = self.attachments

        audience_group_codes: list[str] | None | Unset
        if isinstance(self.audience_group_codes, Unset):
            audience_group_codes = UNSET
        elif isinstance(self.audience_group_codes, list):
            audience_group_codes = self.audience_group_codes


        else:
            audience_group_codes = self.audience_group_codes

        author_id: str | Unset = UNSET
        if not isinstance(self.author_id, Unset):
            author_id = str(self.author_id)

        auto_source: None | str | Unset
        if isinstance(self.auto_source, Unset):
            auto_source = UNSET
        else:
            auto_source = self.auto_source

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        comment_count = self.comment_count

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_acknowledged = self.is_acknowledged

        is_liked = self.is_liked

        is_pinned = self.is_pinned

        is_read = self.is_read

        is_saved = self.is_saved

        latest_comments: list[dict[str, Any]] | None | Unset
        if isinstance(self.latest_comments, Unset):
            latest_comments = UNSET
        elif isinstance(self.latest_comments, list):
            latest_comments = []
            for latest_comments_type_0_item_data in self.latest_comments:
                latest_comments_type_0_item = latest_comments_type_0_item_data.to_dict()
                latest_comments.append(latest_comments_type_0_item)


        else:
            latest_comments = self.latest_comments

        like_count = self.like_count

        my_reaction: None | str | Unset
        if isinstance(self.my_reaction, Unset):
            my_reaction = UNSET
        else:
            my_reaction = self.my_reaction

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        reaction_counts: dict[str, Any] | None | Unset
        if isinstance(self.reaction_counts, Unset):
            reaction_counts = UNSET
        elif isinstance(self.reaction_counts, OfficeAnnouncementDtoReactionCountsType0):
            reaction_counts = self.reaction_counts.to_dict()
        else:
            reaction_counts = self.reaction_counts

        read_count = self.read_count

        requires_acknowledgement = self.requires_acknowledgement

        share_count = self.share_count

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if acknowledged_count is not UNSET:
            field_dict["acknowledgedCount"] = acknowledged_count
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if audience_group_codes is not UNSET:
            field_dict["audienceGroupCodes"] = audience_group_codes
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if auto_source is not UNSET:
            field_dict["autoSource"] = auto_source
        if category is not UNSET:
            field_dict["category"] = category
        if comment_count is not UNSET:
            field_dict["commentCount"] = comment_count
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_acknowledged is not UNSET:
            field_dict["isAcknowledged"] = is_acknowledged
        if is_liked is not UNSET:
            field_dict["isLiked"] = is_liked
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned
        if is_read is not UNSET:
            field_dict["isRead"] = is_read
        if is_saved is not UNSET:
            field_dict["isSaved"] = is_saved
        if latest_comments is not UNSET:
            field_dict["latestComments"] = latest_comments
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if my_reaction is not UNSET:
            field_dict["myReaction"] = my_reaction
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if reaction_counts is not UNSET:
            field_dict["reactionCounts"] = reaction_counts
        if read_count is not UNSET:
            field_dict["readCount"] = read_count
        if requires_acknowledgement is not UNSET:
            field_dict["requiresAcknowledgement"] = requires_acknowledgement
        if share_count is not UNSET:
            field_dict["shareCount"] = share_count
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_announcement_attachment_dto import OfficeAnnouncementAttachmentDto # noqa: PLC0415
        from ..models.office_announcement_comment_preview_dto import OfficeAnnouncementCommentPreviewDto # noqa: PLC0415
        from ..models.office_announcement_dto_reaction_counts_type_0 import OfficeAnnouncementDtoReactionCountsType0 # noqa: PLC0415
        d = dict(src_dict)
        acknowledged_count = d.pop("acknowledgedCount", UNSET)

        def _parse_attachments(data: object) -> list[OfficeAnnouncementAttachmentDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in (_attachments_type_0):
                    attachments_type_0_item = OfficeAnnouncementAttachmentDto.from_dict(attachments_type_0_item_data)



                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAnnouncementAttachmentDto] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))


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


        _author_id = d.pop("authorId", UNSET)
        author_id: UUID | Unset
        if isinstance(_author_id,  Unset):
            author_id = UNSET
        else:
            author_id = UUID(_author_id)




        def _parse_auto_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_source = _parse_auto_source(d.pop("autoSource", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        comment_count = d.pop("commentCount", UNSET)

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_acknowledged = d.pop("isAcknowledged", UNSET)

        is_liked = d.pop("isLiked", UNSET)

        is_pinned = d.pop("isPinned", UNSET)

        is_read = d.pop("isRead", UNSET)

        is_saved = d.pop("isSaved", UNSET)

        def _parse_latest_comments(data: object) -> list[OfficeAnnouncementCommentPreviewDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                latest_comments_type_0 = []
                _latest_comments_type_0 = data
                for latest_comments_type_0_item_data in (_latest_comments_type_0):
                    latest_comments_type_0_item = OfficeAnnouncementCommentPreviewDto.from_dict(latest_comments_type_0_item_data)



                    latest_comments_type_0.append(latest_comments_type_0_item)

                return latest_comments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAnnouncementCommentPreviewDto] | None | Unset, data)

        latest_comments = _parse_latest_comments(d.pop("latestComments", UNSET))


        like_count = d.pop("likeCount", UNSET)

        def _parse_my_reaction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        my_reaction = _parse_my_reaction(d.pop("myReaction", UNSET))


        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)



                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))


        def _parse_reaction_counts(data: object) -> None | OfficeAnnouncementDtoReactionCountsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reaction_counts_type_0 = OfficeAnnouncementDtoReactionCountsType0.from_dict(data)



                return reaction_counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeAnnouncementDtoReactionCountsType0 | Unset, data)

        reaction_counts = _parse_reaction_counts(d.pop("reactionCounts", UNSET))


        read_count = d.pop("readCount", UNSET)

        requires_acknowledgement = d.pop("requiresAcknowledgement", UNSET)

        share_count = d.pop("shareCount", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


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




        office_announcement_dto = cls(
            acknowledged_count=acknowledged_count,
            attachments=attachments,
            audience_group_codes=audience_group_codes,
            author_id=author_id,
            auto_source=auto_source,
            category=category,
            comment_count=comment_count,
            content=content,
            created_at=created_at,
            id=id,
            is_acknowledged=is_acknowledged,
            is_liked=is_liked,
            is_pinned=is_pinned,
            is_read=is_read,
            is_saved=is_saved,
            latest_comments=latest_comments,
            like_count=like_count,
            my_reaction=my_reaction,
            published_at=published_at,
            reaction_counts=reaction_counts,
            read_count=read_count,
            requires_acknowledgement=requires_acknowledgement,
            share_count=share_count,
            status=status,
            title=title,
            updated_at=updated_at,
        )

        return office_announcement_dto

