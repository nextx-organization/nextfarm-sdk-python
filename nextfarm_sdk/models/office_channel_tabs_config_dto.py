from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_channel_tab_config_item_dto import OfficeChannelTabConfigItemDto
  from ..models.office_channel_tab_preference_dto import OfficeChannelTabPreferenceDto





T = TypeVar("T", bound="OfficeChannelTabsConfigDto")



@_attrs_define
class OfficeChannelTabsConfigDto:
    

    can_manage_shared: bool | Unset = UNSET
    my: OfficeChannelTabPreferenceDto | Unset = UNSET
    shared: list[OfficeChannelTabConfigItemDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_channel_tab_config_item_dto import OfficeChannelTabConfigItemDto # noqa: PLC0415
        from ..models.office_channel_tab_preference_dto import OfficeChannelTabPreferenceDto # noqa: PLC0415
        can_manage_shared = self.can_manage_shared

        my: dict[str, Any] | Unset = UNSET
        if not isinstance(self.my, Unset):
            my = self.my.to_dict()

        shared: list[dict[str, Any]] | None | Unset
        if isinstance(self.shared, Unset):
            shared = UNSET
        elif isinstance(self.shared, list):
            shared = []
            for shared_type_0_item_data in self.shared:
                shared_type_0_item = shared_type_0_item_data.to_dict()
                shared.append(shared_type_0_item)


        else:
            shared = self.shared


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if can_manage_shared is not UNSET:
            field_dict["canManageShared"] = can_manage_shared
        if my is not UNSET:
            field_dict["my"] = my
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_channel_tab_config_item_dto import OfficeChannelTabConfigItemDto # noqa: PLC0415
        from ..models.office_channel_tab_preference_dto import OfficeChannelTabPreferenceDto # noqa: PLC0415
        d = dict(src_dict)
        can_manage_shared = d.pop("canManageShared", UNSET)

        _my = d.pop("my", UNSET)
        my: OfficeChannelTabPreferenceDto | Unset
        if isinstance(_my,  Unset):
            my = UNSET
        else:
            my = OfficeChannelTabPreferenceDto.from_dict(_my)




        def _parse_shared(data: object) -> list[OfficeChannelTabConfigItemDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                shared_type_0 = []
                _shared_type_0 = data
                for shared_type_0_item_data in (_shared_type_0):
                    shared_type_0_item = OfficeChannelTabConfigItemDto.from_dict(shared_type_0_item_data)



                    shared_type_0.append(shared_type_0_item)

                return shared_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChannelTabConfigItemDto] | None | Unset, data)

        shared = _parse_shared(d.pop("shared", UNSET))


        office_channel_tabs_config_dto = cls(
            can_manage_shared=can_manage_shared,
            my=my,
            shared=shared,
        )

        return office_channel_tabs_config_dto

