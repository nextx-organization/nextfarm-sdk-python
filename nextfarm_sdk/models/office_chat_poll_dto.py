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
  from ..models.office_chat_poll_option_dto import OfficeChatPollOptionDto





T = TypeVar("T", bound="OfficeChatPollDto")



@_attrs_define
class OfficeChatPollDto:
    

    allow_multiple: bool | Unset = UNSET
    can_close: bool | Unset = UNSET
    can_vote: bool | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    is_anonymous: bool | Unset = UNSET
    message_id: None | Unset | UUID = UNSET
    my_option_ids: list[UUID] | None | Unset = UNSET
    options: list[OfficeChatPollOptionDto] | None | Unset = UNSET
    question: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    total_voters: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chat_poll_option_dto import OfficeChatPollOptionDto # noqa: PLC0415
        allow_multiple = self.allow_multiple

        can_close = self.can_close

        can_vote = self.can_vote

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_anonymous = self.is_anonymous

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        elif isinstance(self.message_id, UUID):
            message_id = str(self.message_id)
        else:
            message_id = self.message_id

        my_option_ids: list[str] | None | Unset
        if isinstance(self.my_option_ids, Unset):
            my_option_ids = UNSET
        elif isinstance(self.my_option_ids, list):
            my_option_ids = []
            for my_option_ids_type_0_item_data in self.my_option_ids:
                my_option_ids_type_0_item = str(my_option_ids_type_0_item_data)
                my_option_ids.append(my_option_ids_type_0_item)


        else:
            my_option_ids = self.my_option_ids

        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)


        else:
            options = self.options

        question: None | str | Unset
        if isinstance(self.question, Unset):
            question = UNSET
        else:
            question = self.question

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        total_voters = self.total_voters


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allow_multiple is not UNSET:
            field_dict["allowMultiple"] = allow_multiple
        if can_close is not UNSET:
            field_dict["canClose"] = can_close
        if can_vote is not UNSET:
            field_dict["canVote"] = can_vote
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if id is not UNSET:
            field_dict["id"] = id
        if is_anonymous is not UNSET:
            field_dict["isAnonymous"] = is_anonymous
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if my_option_ids is not UNSET:
            field_dict["myOptionIds"] = my_option_ids
        if options is not UNSET:
            field_dict["options"] = options
        if question is not UNSET:
            field_dict["question"] = question
        if status is not UNSET:
            field_dict["status"] = status
        if total_voters is not UNSET:
            field_dict["totalVoters"] = total_voters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chat_poll_option_dto import OfficeChatPollOptionDto # noqa: PLC0415
        d = dict(src_dict)
        allow_multiple = d.pop("allowMultiple", UNSET)

        can_close = d.pop("canClose", UNSET)

        can_vote = d.pop("canVote", UNSET)

        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)



                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closedAt", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _created_by = d.pop("createdBy", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_anonymous = d.pop("isAnonymous", UNSET)

        def _parse_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                message_id_type_0 = UUID(data)



                return message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        message_id = _parse_message_id(d.pop("messageId", UNSET))


        def _parse_my_option_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                my_option_ids_type_0 = []
                _my_option_ids_type_0 = data
                for my_option_ids_type_0_item_data in (_my_option_ids_type_0):
                    my_option_ids_type_0_item = UUID(my_option_ids_type_0_item_data)



                    my_option_ids_type_0.append(my_option_ids_type_0_item)

                return my_option_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        my_option_ids = _parse_my_option_ids(d.pop("myOptionIds", UNSET))


        def _parse_options(data: object) -> list[OfficeChatPollOptionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in (_options_type_0):
                    options_type_0_item = OfficeChatPollOptionDto.from_dict(options_type_0_item_data)



                    options_type_0.append(options_type_0_item)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatPollOptionDto] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        def _parse_question(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        question = _parse_question(d.pop("question", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        total_voters = d.pop("totalVoters", UNSET)

        office_chat_poll_dto = cls(
            allow_multiple=allow_multiple,
            can_close=can_close,
            can_vote=can_vote,
            channel_id=channel_id,
            closed_at=closed_at,
            created_at=created_at,
            created_by=created_by,
            id=id,
            is_anonymous=is_anonymous,
            message_id=message_id,
            my_option_ids=my_option_ids,
            options=options,
            question=question,
            status=status,
            total_voters=total_voters,
        )

        return office_chat_poll_dto

