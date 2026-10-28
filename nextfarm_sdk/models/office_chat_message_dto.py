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
  from ..models.office_action_card_dto import OfficeActionCardDto
  from ..models.office_chat_folder_dto import OfficeChatFolderDto
  from ..models.office_linked_task_dto import OfficeLinkedTaskDto
  from ..models.office_message_attachment_dto import OfficeMessageAttachmentDto
  from ..models.office_message_reaction_dto import OfficeMessageReactionDto
  from ..models.office_quoted_message_dto import OfficeQuotedMessageDto





T = TypeVar("T", bound="OfficeChatMessageDto")



@_attrs_define
class OfficeChatMessageDto:
    

    attachments: list[OfficeMessageAttachmentDto] | None | Unset = UNSET
    card: OfficeActionCardDto | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    client_message_id: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    edited_at: datetime.datetime | None | Unset = UNSET
    folder: OfficeChatFolderDto | Unset = UNSET
    forwarded_from_sender_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    is_ai_pending: bool | Unset = UNSET
    is_pinned: bool | Unset = UNSET
    is_recalled: bool | Unset = UNSET
    is_starred: bool | Unset = UNSET
    last_reply_at: datetime.datetime | None | Unset = UNSET
    linked_tasks: list[OfficeLinkedTaskDto] | None | Unset = UNSET
    mentioned_user_ids: list[UUID] | None | Unset = UNSET
    mentions_everyone: bool | Unset = UNSET
    message_type: None | str | Unset = UNSET
    parent_message_id: None | Unset | UUID = UNSET
    quoted: OfficeQuotedMessageDto | Unset = UNSET
    reactions: list[OfficeMessageReactionDto] | None | Unset = UNSET
    reply_count: int | Unset = UNSET
    sender_id: UUID | Unset = UNSET
    sender_org_id: None | Unset | UUID = UNSET
    system_args: list[str] | None | Unset = UNSET
    system_key: None | str | Unset = UNSET
    system_text: None | str | Unset = UNSET
    via_webhook_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_action_card_dto import OfficeActionCardDto # noqa: PLC0415
        from ..models.office_chat_folder_dto import OfficeChatFolderDto # noqa: PLC0415
        from ..models.office_linked_task_dto import OfficeLinkedTaskDto # noqa: PLC0415
        from ..models.office_message_attachment_dto import OfficeMessageAttachmentDto # noqa: PLC0415
        from ..models.office_message_reaction_dto import OfficeMessageReactionDto # noqa: PLC0415
        from ..models.office_quoted_message_dto import OfficeQuotedMessageDto # noqa: PLC0415
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

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

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

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        edited_at: None | str | Unset
        if isinstance(self.edited_at, Unset):
            edited_at = UNSET
        elif isinstance(self.edited_at, datetime.datetime):
            edited_at = self.edited_at.isoformat()
        else:
            edited_at = self.edited_at

        folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.to_dict()

        forwarded_from_sender_id: None | str | Unset
        if isinstance(self.forwarded_from_sender_id, Unset):
            forwarded_from_sender_id = UNSET
        elif isinstance(self.forwarded_from_sender_id, UUID):
            forwarded_from_sender_id = str(self.forwarded_from_sender_id)
        else:
            forwarded_from_sender_id = self.forwarded_from_sender_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_ai_pending = self.is_ai_pending

        is_pinned = self.is_pinned

        is_recalled = self.is_recalled

        is_starred = self.is_starred

        last_reply_at: None | str | Unset
        if isinstance(self.last_reply_at, Unset):
            last_reply_at = UNSET
        elif isinstance(self.last_reply_at, datetime.datetime):
            last_reply_at = self.last_reply_at.isoformat()
        else:
            last_reply_at = self.last_reply_at

        linked_tasks: list[dict[str, Any]] | None | Unset
        if isinstance(self.linked_tasks, Unset):
            linked_tasks = UNSET
        elif isinstance(self.linked_tasks, list):
            linked_tasks = []
            for linked_tasks_type_0_item_data in self.linked_tasks:
                linked_tasks_type_0_item = linked_tasks_type_0_item_data.to_dict()
                linked_tasks.append(linked_tasks_type_0_item)


        else:
            linked_tasks = self.linked_tasks

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

        message_type: None | str | Unset
        if isinstance(self.message_type, Unset):
            message_type = UNSET
        else:
            message_type = self.message_type

        parent_message_id: None | str | Unset
        if isinstance(self.parent_message_id, Unset):
            parent_message_id = UNSET
        elif isinstance(self.parent_message_id, UUID):
            parent_message_id = str(self.parent_message_id)
        else:
            parent_message_id = self.parent_message_id

        quoted: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quoted, Unset):
            quoted = self.quoted.to_dict()

        reactions: list[dict[str, Any]] | None | Unset
        if isinstance(self.reactions, Unset):
            reactions = UNSET
        elif isinstance(self.reactions, list):
            reactions = []
            for reactions_type_0_item_data in self.reactions:
                reactions_type_0_item = reactions_type_0_item_data.to_dict()
                reactions.append(reactions_type_0_item)


        else:
            reactions = self.reactions

        reply_count = self.reply_count

        sender_id: str | Unset = UNSET
        if not isinstance(self.sender_id, Unset):
            sender_id = str(self.sender_id)

        sender_org_id: None | str | Unset
        if isinstance(self.sender_org_id, Unset):
            sender_org_id = UNSET
        elif isinstance(self.sender_org_id, UUID):
            sender_org_id = str(self.sender_org_id)
        else:
            sender_org_id = self.sender_org_id

        system_args: list[str] | None | Unset
        if isinstance(self.system_args, Unset):
            system_args = UNSET
        elif isinstance(self.system_args, list):
            system_args = self.system_args


        else:
            system_args = self.system_args

        system_key: None | str | Unset
        if isinstance(self.system_key, Unset):
            system_key = UNSET
        else:
            system_key = self.system_key

        system_text: None | str | Unset
        if isinstance(self.system_text, Unset):
            system_text = UNSET
        else:
            system_text = self.system_text

        via_webhook_name: None | str | Unset
        if isinstance(self.via_webhook_name, Unset):
            via_webhook_name = UNSET
        else:
            via_webhook_name = self.via_webhook_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if card is not UNSET:
            field_dict["card"] = card
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if client_message_id is not UNSET:
            field_dict["clientMessageId"] = client_message_id
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if edited_at is not UNSET:
            field_dict["editedAt"] = edited_at
        if folder is not UNSET:
            field_dict["folder"] = folder
        if forwarded_from_sender_id is not UNSET:
            field_dict["forwardedFromSenderId"] = forwarded_from_sender_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_ai_pending is not UNSET:
            field_dict["isAiPending"] = is_ai_pending
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned
        if is_recalled is not UNSET:
            field_dict["isRecalled"] = is_recalled
        if is_starred is not UNSET:
            field_dict["isStarred"] = is_starred
        if last_reply_at is not UNSET:
            field_dict["lastReplyAt"] = last_reply_at
        if linked_tasks is not UNSET:
            field_dict["linkedTasks"] = linked_tasks
        if mentioned_user_ids is not UNSET:
            field_dict["mentionedUserIds"] = mentioned_user_ids
        if mentions_everyone is not UNSET:
            field_dict["mentionsEveryone"] = mentions_everyone
        if message_type is not UNSET:
            field_dict["messageType"] = message_type
        if parent_message_id is not UNSET:
            field_dict["parentMessageId"] = parent_message_id
        if quoted is not UNSET:
            field_dict["quoted"] = quoted
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if reply_count is not UNSET:
            field_dict["replyCount"] = reply_count
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if sender_org_id is not UNSET:
            field_dict["senderOrgId"] = sender_org_id
        if system_args is not UNSET:
            field_dict["systemArgs"] = system_args
        if system_key is not UNSET:
            field_dict["systemKey"] = system_key
        if system_text is not UNSET:
            field_dict["systemText"] = system_text
        if via_webhook_name is not UNSET:
            field_dict["viaWebhookName"] = via_webhook_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_action_card_dto import OfficeActionCardDto # noqa: PLC0415
        from ..models.office_chat_folder_dto import OfficeChatFolderDto # noqa: PLC0415
        from ..models.office_linked_task_dto import OfficeLinkedTaskDto # noqa: PLC0415
        from ..models.office_message_attachment_dto import OfficeMessageAttachmentDto # noqa: PLC0415
        from ..models.office_message_reaction_dto import OfficeMessageReactionDto # noqa: PLC0415
        from ..models.office_quoted_message_dto import OfficeQuotedMessageDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_attachments(data: object) -> list[OfficeMessageAttachmentDto] | None | Unset:
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
                    attachments_type_0_item = OfficeMessageAttachmentDto.from_dict(attachments_type_0_item_data)



                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeMessageAttachmentDto] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))


        _card = d.pop("card", UNSET)
        card: OfficeActionCardDto | Unset
        if isinstance(_card,  Unset):
            card = UNSET
        else:
            card = OfficeActionCardDto.from_dict(_card)




        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




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


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_edited_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                edited_at_type_0 = datetime.datetime.fromisoformat(data)



                return edited_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        edited_at = _parse_edited_at(d.pop("editedAt", UNSET))


        _folder = d.pop("folder", UNSET)
        folder: OfficeChatFolderDto | Unset
        if isinstance(_folder,  Unset):
            folder = UNSET
        else:
            folder = OfficeChatFolderDto.from_dict(_folder)




        def _parse_forwarded_from_sender_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                forwarded_from_sender_id_type_0 = UUID(data)



                return forwarded_from_sender_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        forwarded_from_sender_id = _parse_forwarded_from_sender_id(d.pop("forwardedFromSenderId", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_ai_pending = d.pop("isAiPending", UNSET)

        is_pinned = d.pop("isPinned", UNSET)

        is_recalled = d.pop("isRecalled", UNSET)

        is_starred = d.pop("isStarred", UNSET)

        def _parse_last_reply_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_reply_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_reply_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_reply_at = _parse_last_reply_at(d.pop("lastReplyAt", UNSET))


        def _parse_linked_tasks(data: object) -> list[OfficeLinkedTaskDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linked_tasks_type_0 = []
                _linked_tasks_type_0 = data
                for linked_tasks_type_0_item_data in (_linked_tasks_type_0):
                    linked_tasks_type_0_item = OfficeLinkedTaskDto.from_dict(linked_tasks_type_0_item_data)



                    linked_tasks_type_0.append(linked_tasks_type_0_item)

                return linked_tasks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeLinkedTaskDto] | None | Unset, data)

        linked_tasks = _parse_linked_tasks(d.pop("linkedTasks", UNSET))


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

        def _parse_message_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_type = _parse_message_type(d.pop("messageType", UNSET))


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


        _quoted = d.pop("quoted", UNSET)
        quoted: OfficeQuotedMessageDto | Unset
        if isinstance(_quoted,  Unset):
            quoted = UNSET
        else:
            quoted = OfficeQuotedMessageDto.from_dict(_quoted)




        def _parse_reactions(data: object) -> list[OfficeMessageReactionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reactions_type_0 = []
                _reactions_type_0 = data
                for reactions_type_0_item_data in (_reactions_type_0):
                    reactions_type_0_item = OfficeMessageReactionDto.from_dict(reactions_type_0_item_data)



                    reactions_type_0.append(reactions_type_0_item)

                return reactions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeMessageReactionDto] | None | Unset, data)

        reactions = _parse_reactions(d.pop("reactions", UNSET))


        reply_count = d.pop("replyCount", UNSET)

        _sender_id = d.pop("senderId", UNSET)
        sender_id: UUID | Unset
        if isinstance(_sender_id,  Unset):
            sender_id = UNSET
        else:
            sender_id = UUID(_sender_id)




        def _parse_sender_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_org_id_type_0 = UUID(data)



                return sender_org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sender_org_id = _parse_sender_org_id(d.pop("senderOrgId", UNSET))


        def _parse_system_args(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                system_args_type_0 = cast(list[str], data)

                return system_args_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        system_args = _parse_system_args(d.pop("systemArgs", UNSET))


        def _parse_system_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_key = _parse_system_key(d.pop("systemKey", UNSET))


        def _parse_system_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_text = _parse_system_text(d.pop("systemText", UNSET))


        def _parse_via_webhook_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        via_webhook_name = _parse_via_webhook_name(d.pop("viaWebhookName", UNSET))


        office_chat_message_dto = cls(
            attachments=attachments,
            card=card,
            channel_id=channel_id,
            client_message_id=client_message_id,
            content=content,
            created_at=created_at,
            edited_at=edited_at,
            folder=folder,
            forwarded_from_sender_id=forwarded_from_sender_id,
            id=id,
            is_ai_pending=is_ai_pending,
            is_pinned=is_pinned,
            is_recalled=is_recalled,
            is_starred=is_starred,
            last_reply_at=last_reply_at,
            linked_tasks=linked_tasks,
            mentioned_user_ids=mentioned_user_ids,
            mentions_everyone=mentions_everyone,
            message_type=message_type,
            parent_message_id=parent_message_id,
            quoted=quoted,
            reactions=reactions,
            reply_count=reply_count,
            sender_id=sender_id,
            sender_org_id=sender_org_id,
            system_args=system_args,
            system_key=system_key,
            system_text=system_text,
            via_webhook_name=via_webhook_name,
        )

        return office_chat_message_dto

