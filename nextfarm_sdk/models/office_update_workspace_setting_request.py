from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeUpdateWorkspaceSettingRequest")



@_attrs_define
class OfficeUpdateWorkspaceSettingRequest:
    

    time_zone_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        time_zone_id: None | str | Unset
        if isinstance(self.time_zone_id, Unset):
            time_zone_id = UNSET
        else:
            time_zone_id = self.time_zone_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if time_zone_id is not UNSET:
            field_dict["timeZoneId"] = time_zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_time_zone_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone_id = _parse_time_zone_id(d.pop("timeZoneId", UNSET))


        office_update_workspace_setting_request = cls(
            time_zone_id=time_zone_id,
        )

        return office_update_workspace_setting_request

