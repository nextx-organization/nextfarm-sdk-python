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






T = TypeVar("T", bound="OfficeNotificationInboxItemDto")



@_attrs_define
class OfficeNotificationInboxItemDto:
    

    body: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    deep_link: None | str | Unset = UNSET
    entity_id: None | Unset | UUID = UNSET
    entity_type: None | str | Unset = UNSET
    entity_url: None | str | Unset = UNSET
    group_count: int | None | Unset = UNSET
    id: UUID | Unset = UNSET
    is_batched: bool | Unset = UNSET
    is_read: bool | Unset = UNSET
    list_link: None | str | Unset = UNSET
    notification_type: None | str | Unset = UNSET
    read_at: datetime.datetime | None | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deep_link: None | str | Unset
        if isinstance(self.deep_link, Unset):
            deep_link = UNSET
        else:
            deep_link = self.deep_link

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        entity_url: None | str | Unset
        if isinstance(self.entity_url, Unset):
            entity_url = UNSET
        else:
            entity_url = self.entity_url

        group_count: int | None | Unset
        if isinstance(self.group_count, Unset):
            group_count = UNSET
        else:
            group_count = self.group_count

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_batched = self.is_batched

        is_read = self.is_read

        list_link: None | str | Unset
        if isinstance(self.list_link, Unset):
            list_link = UNSET
        else:
            list_link = self.list_link

        notification_type: None | str | Unset
        if isinstance(self.notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = self.notification_type

        read_at: None | str | Unset
        if isinstance(self.read_at, Unset):
            read_at = UNSET
        elif isinstance(self.read_at, datetime.datetime):
            read_at = self.read_at.isoformat()
        else:
            read_at = self.read_at

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if body is not UNSET:
            field_dict["body"] = body
        if category is not UNSET:
            field_dict["category"] = category
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if deep_link is not UNSET:
            field_dict["deepLink"] = deep_link
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if entity_url is not UNSET:
            field_dict["entityUrl"] = entity_url
        if group_count is not UNSET:
            field_dict["groupCount"] = group_count
        if id is not UNSET:
            field_dict["id"] = id
        if is_batched is not UNSET:
            field_dict["isBatched"] = is_batched
        if is_read is not UNSET:
            field_dict["isRead"] = is_read
        if list_link is not UNSET:
            field_dict["listLink"] = list_link
        if notification_type is not UNSET:
            field_dict["notificationType"] = notification_type
        if read_at is not UNSET:
            field_dict["readAt"] = read_at
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_deep_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deep_link = _parse_deep_link(d.pop("deepLink", UNSET))


        def _parse_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_id_type_0 = UUID(data)



                return entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        entity_id = _parse_entity_id(d.pop("entityId", UNSET))


        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entityType", UNSET))


        def _parse_entity_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_url = _parse_entity_url(d.pop("entityUrl", UNSET))


        def _parse_group_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_count = _parse_group_count(d.pop("groupCount", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_batched = d.pop("isBatched", UNSET)

        is_read = d.pop("isRead", UNSET)

        def _parse_list_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_link = _parse_list_link(d.pop("listLink", UNSET))


        def _parse_notification_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_type = _parse_notification_type(d.pop("notificationType", UNSET))


        def _parse_read_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                read_at_type_0 = datetime.datetime.fromisoformat(data)



                return read_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        read_at = _parse_read_at(d.pop("readAt", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_notification_inbox_item_dto = cls(
            body=body,
            category=category,
            created_at=created_at,
            deep_link=deep_link,
            entity_id=entity_id,
            entity_type=entity_type,
            entity_url=entity_url,
            group_count=group_count,
            id=id,
            is_batched=is_batched,
            is_read=is_read,
            list_link=list_link,
            notification_type=notification_type,
            read_at=read_at,
            title=title,
        )

        return office_notification_inbox_item_dto

