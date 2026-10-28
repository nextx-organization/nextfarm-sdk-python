from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_announcement_feed_group_dto import OfficeAnnouncementFeedGroupDto





T = TypeVar("T", bound="OfficeAnnouncementFeedSummaryDto")



@_attrs_define
class OfficeAnnouncementFeedSummaryDto:
    

    drafts: int | Unset = UNSET
    groups: list[OfficeAnnouncementFeedGroupDto] | None | Unset = UNSET
    pending_acknowledgements: int | Unset = UNSET
    unread_announcements: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_announcement_feed_group_dto import OfficeAnnouncementFeedGroupDto # noqa: PLC0415
        drafts = self.drafts

        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)


        else:
            groups = self.groups

        pending_acknowledgements = self.pending_acknowledgements

        unread_announcements = self.unread_announcements


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if drafts is not UNSET:
            field_dict["drafts"] = drafts
        if groups is not UNSET:
            field_dict["groups"] = groups
        if pending_acknowledgements is not UNSET:
            field_dict["pendingAcknowledgements"] = pending_acknowledgements
        if unread_announcements is not UNSET:
            field_dict["unreadAnnouncements"] = unread_announcements

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_announcement_feed_group_dto import OfficeAnnouncementFeedGroupDto # noqa: PLC0415
        d = dict(src_dict)
        drafts = d.pop("drafts", UNSET)

        def _parse_groups(data: object) -> list[OfficeAnnouncementFeedGroupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in (_groups_type_0):
                    groups_type_0_item = OfficeAnnouncementFeedGroupDto.from_dict(groups_type_0_item_data)



                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAnnouncementFeedGroupDto] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))


        pending_acknowledgements = d.pop("pendingAcknowledgements", UNSET)

        unread_announcements = d.pop("unreadAnnouncements", UNSET)

        office_announcement_feed_summary_dto = cls(
            drafts=drafts,
            groups=groups,
            pending_acknowledgements=pending_acknowledgements,
            unread_announcements=unread_announcements,
        )

        return office_announcement_feed_summary_dto

