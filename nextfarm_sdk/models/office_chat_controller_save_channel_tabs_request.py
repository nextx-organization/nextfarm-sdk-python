from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_chat_controller_channel_tab_request_item import OfficeChatControllerChannelTabRequestItem





T = TypeVar("T", bound="OfficeChatControllerSaveChannelTabsRequest")



@_attrs_define
class OfficeChatControllerSaveChannelTabsRequest:
    

    tabs: list[OfficeChatControllerChannelTabRequestItem] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chat_controller_channel_tab_request_item import OfficeChatControllerChannelTabRequestItem # noqa: PLC0415
        tabs: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabs, Unset):
            tabs = UNSET
        elif isinstance(self.tabs, list):
            tabs = []
            for tabs_type_0_item_data in self.tabs:
                tabs_type_0_item = tabs_type_0_item_data.to_dict()
                tabs.append(tabs_type_0_item)


        else:
            tabs = self.tabs


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if tabs is not UNSET:
            field_dict["tabs"] = tabs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chat_controller_channel_tab_request_item import OfficeChatControllerChannelTabRequestItem # noqa: PLC0415
        d = dict(src_dict)
        def _parse_tabs(data: object) -> list[OfficeChatControllerChannelTabRequestItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabs_type_0 = []
                _tabs_type_0 = data
                for tabs_type_0_item_data in (_tabs_type_0):
                    tabs_type_0_item = OfficeChatControllerChannelTabRequestItem.from_dict(tabs_type_0_item_data)



                    tabs_type_0.append(tabs_type_0_item)

                return tabs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatControllerChannelTabRequestItem] | None | Unset, data)

        tabs = _parse_tabs(d.pop("tabs", UNSET))


        office_chat_controller_save_channel_tabs_request = cls(
            tabs=tabs,
        )

        return office_chat_controller_save_channel_tabs_request

