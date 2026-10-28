from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_chat_message_dto import OfficeChatMessageDto
  from ..models.office_chat_search_channel_dto import OfficeChatSearchChannelDto
  from ..models.office_chat_search_contact_dto import OfficeChatSearchContactDto
  from ..models.office_chat_search_file_dto import OfficeChatSearchFileDto





T = TypeVar("T", bound="OfficeChatSearchResultDto")



@_attrs_define
class OfficeChatSearchResultDto:
    

    channels: list[OfficeChatSearchChannelDto] | None | Unset = UNSET
    contacts: list[OfficeChatSearchContactDto] | None | Unset = UNSET
    files: list[OfficeChatSearchFileDto] | None | Unset = UNSET
    messages: list[OfficeChatMessageDto] | None | Unset = UNSET
    source: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chat_message_dto import OfficeChatMessageDto # noqa: PLC0415
        from ..models.office_chat_search_channel_dto import OfficeChatSearchChannelDto # noqa: PLC0415
        from ..models.office_chat_search_contact_dto import OfficeChatSearchContactDto # noqa: PLC0415
        from ..models.office_chat_search_file_dto import OfficeChatSearchFileDto # noqa: PLC0415
        channels: list[dict[str, Any]] | None | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        elif isinstance(self.channels, list):
            channels = []
            for channels_type_0_item_data in self.channels:
                channels_type_0_item = channels_type_0_item_data.to_dict()
                channels.append(channels_type_0_item)


        else:
            channels = self.channels

        contacts: list[dict[str, Any]] | None | Unset
        if isinstance(self.contacts, Unset):
            contacts = UNSET
        elif isinstance(self.contacts, list):
            contacts = []
            for contacts_type_0_item_data in self.contacts:
                contacts_type_0_item = contacts_type_0_item_data.to_dict()
                contacts.append(contacts_type_0_item)


        else:
            contacts = self.contacts

        files: list[dict[str, Any]] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_dict()
                files.append(files_type_0_item)


        else:
            files = self.files

        messages: list[dict[str, Any]] | None | Unset
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = []
            for messages_type_0_item_data in self.messages:
                messages_type_0_item = messages_type_0_item_data.to_dict()
                messages.append(messages_type_0_item)


        else:
            messages = self.messages

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channels is not UNSET:
            field_dict["channels"] = channels
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if files is not UNSET:
            field_dict["files"] = files
        if messages is not UNSET:
            field_dict["messages"] = messages
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chat_message_dto import OfficeChatMessageDto # noqa: PLC0415
        from ..models.office_chat_search_channel_dto import OfficeChatSearchChannelDto # noqa: PLC0415
        from ..models.office_chat_search_contact_dto import OfficeChatSearchContactDto # noqa: PLC0415
        from ..models.office_chat_search_file_dto import OfficeChatSearchFileDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_channels(data: object) -> list[OfficeChatSearchChannelDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channels_type_0 = []
                _channels_type_0 = data
                for channels_type_0_item_data in (_channels_type_0):
                    channels_type_0_item = OfficeChatSearchChannelDto.from_dict(channels_type_0_item_data)



                    channels_type_0.append(channels_type_0_item)

                return channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatSearchChannelDto] | None | Unset, data)

        channels = _parse_channels(d.pop("channels", UNSET))


        def _parse_contacts(data: object) -> list[OfficeChatSearchContactDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contacts_type_0 = []
                _contacts_type_0 = data
                for contacts_type_0_item_data in (_contacts_type_0):
                    contacts_type_0_item = OfficeChatSearchContactDto.from_dict(contacts_type_0_item_data)



                    contacts_type_0.append(contacts_type_0_item)

                return contacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatSearchContactDto] | None | Unset, data)

        contacts = _parse_contacts(d.pop("contacts", UNSET))


        def _parse_files(data: object) -> list[OfficeChatSearchFileDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in (_files_type_0):
                    files_type_0_item = OfficeChatSearchFileDto.from_dict(files_type_0_item_data)



                    files_type_0.append(files_type_0_item)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatSearchFileDto] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))


        def _parse_messages(data: object) -> list[OfficeChatMessageDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = []
                _messages_type_0 = data
                for messages_type_0_item_data in (_messages_type_0):
                    messages_type_0_item = OfficeChatMessageDto.from_dict(messages_type_0_item_data)



                    messages_type_0.append(messages_type_0_item)

                return messages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatMessageDto] | None | Unset, data)

        messages = _parse_messages(d.pop("messages", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        office_chat_search_result_dto = cls(
            channels=channels,
            contacts=contacts,
            files=files,
            messages=messages,
            source=source,
        )

        return office_chat_search_result_dto

