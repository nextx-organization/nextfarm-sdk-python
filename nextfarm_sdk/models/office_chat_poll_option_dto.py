from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatPollOptionDto")



@_attrs_define
class OfficeChatPollOptionDto:
    

    id: UUID | Unset = UNSET
    sort_order: int | Unset = UNSET
    text: None | str | Unset = UNSET
    vote_count: int | Unset = UNSET
    voter_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        sort_order = self.sort_order

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        vote_count = self.vote_count

        voter_ids: list[str] | None | Unset
        if isinstance(self.voter_ids, Unset):
            voter_ids = UNSET
        elif isinstance(self.voter_ids, list):
            voter_ids = []
            for voter_ids_type_0_item_data in self.voter_ids:
                voter_ids_type_0_item = str(voter_ids_type_0_item_data)
                voter_ids.append(voter_ids_type_0_item)


        else:
            voter_ids = self.voter_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if text is not UNSET:
            field_dict["text"] = text
        if vote_count is not UNSET:
            field_dict["voteCount"] = vote_count
        if voter_ids is not UNSET:
            field_dict["voterIds"] = voter_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        sort_order = d.pop("sortOrder", UNSET)

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        vote_count = d.pop("voteCount", UNSET)

        def _parse_voter_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                voter_ids_type_0 = []
                _voter_ids_type_0 = data
                for voter_ids_type_0_item_data in (_voter_ids_type_0):
                    voter_ids_type_0_item = UUID(voter_ids_type_0_item_data)



                    voter_ids_type_0.append(voter_ids_type_0_item)

                return voter_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        voter_ids = _parse_voter_ids(d.pop("voterIds", UNSET))


        office_chat_poll_option_dto = cls(
            id=id,
            sort_order=sort_order,
            text=text,
            vote_count=vote_count,
            voter_ids=voter_ids,
        )

        return office_chat_poll_option_dto

