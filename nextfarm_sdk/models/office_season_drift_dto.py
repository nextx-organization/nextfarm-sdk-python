from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeSeasonDriftDto")



@_attrs_define
class OfficeSeasonDriftDto:
    

    changed: bool | Unset = UNSET
    current_end: datetime.date | None | Unset = UNSET
    current_start: datetime.date | None | Unset = UNSET
    error_key: None | str | Unset = UNSET
    stored_end: datetime.date | Unset = UNSET
    stored_start: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        current_end: None | str | Unset
        if isinstance(self.current_end, Unset):
            current_end = UNSET
        elif isinstance(self.current_end, datetime.date):
            current_end = self.current_end.isoformat()
        else:
            current_end = self.current_end

        current_start: None | str | Unset
        if isinstance(self.current_start, Unset):
            current_start = UNSET
        elif isinstance(self.current_start, datetime.date):
            current_start = self.current_start.isoformat()
        else:
            current_start = self.current_start

        error_key: None | str | Unset
        if isinstance(self.error_key, Unset):
            error_key = UNSET
        else:
            error_key = self.error_key

        stored_end: str | Unset = UNSET
        if not isinstance(self.stored_end, Unset):
            stored_end = self.stored_end.isoformat()

        stored_start: str | Unset = UNSET
        if not isinstance(self.stored_start, Unset):
            stored_start = self.stored_start.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if changed is not UNSET:
            field_dict["changed"] = changed
        if current_end is not UNSET:
            field_dict["currentEnd"] = current_end
        if current_start is not UNSET:
            field_dict["currentStart"] = current_start
        if error_key is not UNSET:
            field_dict["errorKey"] = error_key
        if stored_end is not UNSET:
            field_dict["storedEnd"] = stored_end
        if stored_start is not UNSET:
            field_dict["storedStart"] = stored_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changed = d.pop("changed", UNSET)

        def _parse_current_end(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_end_type_0 = datetime.date.fromisoformat(data)



                return current_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        current_end = _parse_current_end(d.pop("currentEnd", UNSET))


        def _parse_current_start(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_start_type_0 = datetime.date.fromisoformat(data)



                return current_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        current_start = _parse_current_start(d.pop("currentStart", UNSET))


        def _parse_error_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_key = _parse_error_key(d.pop("errorKey", UNSET))


        _stored_end = d.pop("storedEnd", UNSET)
        stored_end: datetime.date | Unset
        if isinstance(_stored_end,  Unset):
            stored_end = UNSET
        else:
            stored_end = datetime.date.fromisoformat(_stored_end)




        _stored_start = d.pop("storedStart", UNSET)
        stored_start: datetime.date | Unset
        if isinstance(_stored_start,  Unset):
            stored_start = UNSET
        else:
            stored_start = datetime.date.fromisoformat(_stored_start)




        office_season_drift_dto = cls(
            changed=changed,
            current_end=current_end,
            current_start=current_start,
            error_key=error_key,
            stored_end=stored_end,
            stored_start=stored_start,
        )

        return office_season_drift_dto

