from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_send_message_attachment import OfficeSendMessageAttachment





T = TypeVar("T", bound="OfficeChatControllerSendMessageRequest")



@_attrs_define
class OfficeChatControllerSendMessageRequest:
    

    attachments: list[OfficeSendMessageAttachment] | None | Unset = UNSET
    client_message_id: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    has_attachment: bool | Unset = UNSET
    mentioned_user_ids: list[UUID] | None | Unset = UNSET
    mentions_everyone: bool | Unset = UNSET
    parent_message_id: None | Unset | UUID = UNSET
    quoted_message_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_send_message_attachment import OfficeSendMessageAttachment # noqa: PLC0415
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

        client_message_id: None | str | Unset
        if isinstance(self.client_message_id, Unset):
            client_message_id = UNSET
        else:
            client_message_id = self.client_message_id

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        has_attachment = self.has_attachment

        mentioned_user_ids: list[str] | None | Unset
        if isinstance(self.mentioned_user_ids, Unset):
            mentioned_user_ids = UNSET
        elif isinstance(self.mentioned_user_ids, list):
            mentioned_user_ids = []
            for mentioned_user_ids_type_0_item_data in self.mentioned_user_ids:
                mentioned_user_ids_type_0_item = str(mentioned_user_ids_type_0_item_data)
                mentioned_user_ids.append(mentioned_user_ids_type_0_item)


        else:
            mentioned_user_ids = self.mentioned_user_ids

        mentions_everyone = self.mentions_everyone

        parent_message_id: None | str | Unset
        if isinstance(self.parent_message_id, Unset):
            parent_message_id = UNSET
        elif isinstance(self.parent_message_id, UUID):
            parent_message_id = str(self.parent_message_id)
        else:
            parent_message_id = self.parent_message_id

        quoted_message_id: None | str | Unset
        if isinstance(self.quoted_message_id, Unset):
            quoted_message_id = UNSET
        elif isinstance(self.quoted_message_id, UUID):
            quoted_message_id = str(self.quoted_message_id)
        else:
            quoted_message_id = self.quoted_message_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if client_message_id is not UNSET:
            field_dict["clientMessageId"] = client_message_id
        if content is not UNSET:
            field_dict["content"] = content
        if has_attachment is not UNSET:
            field_dict["hasAttachment"] = has_attachment
        if mentioned_user_ids is not UNSET:
            field_dict["mentionedUserIds"] = mentioned_user_ids
        if mentions_everyone is not UNSET:
            field_dict["mentionsEveryone"] = mentions_everyone
        if parent_message_id is not UNSET:
            field_dict["parentMessageId"] = parent_message_id
        if quoted_message_id is not UNSET:
            field_dict["quotedMessageId"] = quoted_message_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_send_message_attachment import OfficeSendMessageAttachment # noqa: PLC0415
        d = dict(src_dict)
        def _parse_attachments(data: object) -> list[OfficeSendMessageAttachment] | None | Unset:
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
                    attachments_type_0_item = OfficeSendMessageAttachment.from_dict(attachments_type_0_item_data)



                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeSendMessageAttachment] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))


        def _parse_client_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_message_id = _parse_client_message_id(d.pop("clientMessageId", UNSET))


        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        has_attachment = d.pop("hasAttachment", UNSET)

        def _parse_mentioned_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mentioned_user_ids_type_0 = []
                _mentioned_user_ids_type_0 = data
                for mentioned_user_ids_type_0_item_data in (_mentioned_user_ids_type_0):
                    mentioned_user_ids_type_0_item = UUID(mentioned_user_ids_type_0_item_data)



                    mentioned_user_ids_type_0.append(mentioned_user_ids_type_0_item)

                return mentioned_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        mentioned_user_ids = _parse_mentioned_user_ids(d.pop("mentionedUserIds", UNSET))


        mentions_everyone = d.pop("mentionsEveryone", UNSET)

        def _parse_parent_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_message_id_type_0 = UUID(data)



                return parent_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_message_id = _parse_parent_message_id(d.pop("parentMessageId", UNSET))


        def _parse_quoted_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quoted_message_id_type_0 = UUID(data)



                return quoted_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        quoted_message_id = _parse_quoted_message_id(d.pop("quotedMessageId", UNSET))


        office_chat_controller_send_message_request = cls(
            attachments=attachments,
            client_message_id=client_message_id,
            content=content,
            has_attachment=has_attachment,
            mentioned_user_ids=mentioned_user_ids,
            mentions_everyone=mentions_everyone,
            parent_message_id=parent_message_id,
            quoted_message_id=quoted_message_id,
        )

        return office_chat_controller_send_message_request

