from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_send_message_attachment import OfficeSendMessageAttachment





T = TypeVar("T", bound="OfficeChatControllerSendMySupportMessageRequest")



@_attrs_define
class OfficeChatControllerSendMySupportMessageRequest:
    

    attachments: list[OfficeSendMessageAttachment] | None | Unset = UNSET
    client_message_id: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    has_attachment: bool | Unset = UNSET





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

        office_chat_controller_send_my_support_message_request = cls(
            attachments=attachments,
            client_message_id=client_message_id,
            content=content,
            has_attachment=has_attachment,
        )

        return office_chat_controller_send_my_support_message_request

