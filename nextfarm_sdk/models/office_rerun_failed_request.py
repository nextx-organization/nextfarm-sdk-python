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






T = TypeVar("T", bound="OfficeRerunFailedRequest")



@_attrs_define
class OfficeRerunFailedRequest:
    

    automation_id: None | Unset | UUID = UNSET
    from_: datetime.datetime | None | Unset = UNSET
    max_: int | None | Unset = UNSET
    to: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        automation_id: None | str | Unset
        if isinstance(self.automation_id, Unset):
            automation_id = UNSET
        elif isinstance(self.automation_id, UUID):
            automation_id = str(self.automation_id)
        else:
            automation_id = self.automation_id

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, datetime.datetime):
            from_ = self.from_.isoformat()
        else:
            from_ = self.from_

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, datetime.datetime):
            to = self.to.isoformat()
        else:
            to = self.to


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if automation_id is not UNSET:
            field_dict["automationId"] = automation_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_automation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                automation_id_type_0 = UUID(data)



                return automation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        automation_id = _parse_automation_id(d.pop("automationId", UNSET))


        def _parse_from_(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_type_0 = datetime.datetime.fromisoformat(data)



                return from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))


        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))


        def _parse_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_type_0 = datetime.datetime.fromisoformat(data)



                return to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to = _parse_to(d.pop("to", UNSET))


        office_rerun_failed_request = cls(
            automation_id=automation_id,
            from_=from_,
            max_=max_,
            to=to,
        )

        return office_rerun_failed_request

