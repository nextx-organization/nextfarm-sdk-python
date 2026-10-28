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






T = TypeVar("T", bound="OfficeChannelMemberWorkloadDto")



@_attrs_define
class OfficeChannelMemberWorkloadDto:
    

    done_count: int | Unset = UNSET
    longest_in_progress_since: datetime.datetime | None | Unset = UNSET
    oldest_open_since: datetime.datetime | None | Unset = UNSET
    open_count: int | Unset = UNSET
    overdue_count: int | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        done_count = self.done_count

        longest_in_progress_since: None | str | Unset
        if isinstance(self.longest_in_progress_since, Unset):
            longest_in_progress_since = UNSET
        elif isinstance(self.longest_in_progress_since, datetime.datetime):
            longest_in_progress_since = self.longest_in_progress_since.isoformat()
        else:
            longest_in_progress_since = self.longest_in_progress_since

        oldest_open_since: None | str | Unset
        if isinstance(self.oldest_open_since, Unset):
            oldest_open_since = UNSET
        elif isinstance(self.oldest_open_since, datetime.datetime):
            oldest_open_since = self.oldest_open_since.isoformat()
        else:
            oldest_open_since = self.oldest_open_since

        open_count = self.open_count

        overdue_count = self.overdue_count

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if done_count is not UNSET:
            field_dict["doneCount"] = done_count
        if longest_in_progress_since is not UNSET:
            field_dict["longestInProgressSince"] = longest_in_progress_since
        if oldest_open_since is not UNSET:
            field_dict["oldestOpenSince"] = oldest_open_since
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if overdue_count is not UNSET:
            field_dict["overdueCount"] = overdue_count
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        done_count = d.pop("doneCount", UNSET)

        def _parse_longest_in_progress_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                longest_in_progress_since_type_0 = datetime.datetime.fromisoformat(data)



                return longest_in_progress_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        longest_in_progress_since = _parse_longest_in_progress_since(d.pop("longestInProgressSince", UNSET))


        def _parse_oldest_open_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oldest_open_since_type_0 = datetime.datetime.fromisoformat(data)



                return oldest_open_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        oldest_open_since = _parse_oldest_open_since(d.pop("oldestOpenSince", UNSET))


        open_count = d.pop("openCount", UNSET)

        overdue_count = d.pop("overdueCount", UNSET)

        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_channel_member_workload_dto = cls(
            done_count=done_count,
            longest_in_progress_since=longest_in_progress_since,
            oldest_open_since=oldest_open_since,
            open_count=open_count,
            overdue_count=overdue_count,
            user_id=user_id,
        )

        return office_channel_member_workload_dto

