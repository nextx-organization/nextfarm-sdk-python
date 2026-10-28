from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_trace_node import HarvestTraceNode
  from ..models.harvest_trace_ref import HarvestTraceRef





T = TypeVar("T", bound="HarvestTraceResolution")



@_attrs_define
class HarvestTraceResolution:
    

    down: list[HarvestTraceRef] | None | Unset = UNSET
    node: HarvestTraceNode | Unset = UNSET
    up: list[HarvestTraceRef] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_trace_node import HarvestTraceNode # noqa: PLC0415
        from ..models.harvest_trace_ref import HarvestTraceRef # noqa: PLC0415
        down: list[dict[str, Any]] | None | Unset
        if isinstance(self.down, Unset):
            down = UNSET
        elif isinstance(self.down, list):
            down = []
            for down_type_0_item_data in self.down:
                down_type_0_item = down_type_0_item_data.to_dict()
                down.append(down_type_0_item)


        else:
            down = self.down

        node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        up: list[dict[str, Any]] | None | Unset
        if isinstance(self.up, Unset):
            up = UNSET
        elif isinstance(self.up, list):
            up = []
            for up_type_0_item_data in self.up:
                up_type_0_item = up_type_0_item_data.to_dict()
                up.append(up_type_0_item)


        else:
            up = self.up


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if down is not UNSET:
            field_dict["down"] = down
        if node is not UNSET:
            field_dict["node"] = node
        if up is not UNSET:
            field_dict["up"] = up

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_trace_node import HarvestTraceNode # noqa: PLC0415
        from ..models.harvest_trace_ref import HarvestTraceRef # noqa: PLC0415
        d = dict(src_dict)
        def _parse_down(data: object) -> list[HarvestTraceRef] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                down_type_0 = []
                _down_type_0 = data
                for down_type_0_item_data in (_down_type_0):
                    down_type_0_item = HarvestTraceRef.from_dict(down_type_0_item_data)



                    down_type_0.append(down_type_0_item)

                return down_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestTraceRef] | None | Unset, data)

        down = _parse_down(d.pop("down", UNSET))


        _node = d.pop("node", UNSET)
        node: HarvestTraceNode | Unset
        if isinstance(_node,  Unset):
            node = UNSET
        else:
            node = HarvestTraceNode.from_dict(_node)




        def _parse_up(data: object) -> list[HarvestTraceRef] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                up_type_0 = []
                _up_type_0 = data
                for up_type_0_item_data in (_up_type_0):
                    up_type_0_item = HarvestTraceRef.from_dict(up_type_0_item_data)



                    up_type_0.append(up_type_0_item)

                return up_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestTraceRef] | None | Unset, data)

        up = _parse_up(d.pop("up", UNSET))


        harvest_trace_resolution = cls(
            down=down,
            node=node,
            up=up,
        )

        return harvest_trace_resolution

