from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_pending_anchor_bundle_dto import HarvestPendingAnchorBundleDto
  from ..models.harvest_workspace_anchor_dto import HarvestWorkspaceAnchorDto





T = TypeVar("T", bound="HarvestTraceAnchorsResponse")



@_attrs_define
class HarvestTraceAnchorsResponse:
    

    anchor_schedule_local: None | str | Unset = UNSET
    anchors: list[HarvestWorkspaceAnchorDto] | None | Unset = UNSET
    pending: list[HarvestPendingAnchorBundleDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_pending_anchor_bundle_dto import HarvestPendingAnchorBundleDto # noqa: PLC0415
        from ..models.harvest_workspace_anchor_dto import HarvestWorkspaceAnchorDto # noqa: PLC0415
        anchor_schedule_local: None | str | Unset
        if isinstance(self.anchor_schedule_local, Unset):
            anchor_schedule_local = UNSET
        else:
            anchor_schedule_local = self.anchor_schedule_local

        anchors: list[dict[str, Any]] | None | Unset
        if isinstance(self.anchors, Unset):
            anchors = UNSET
        elif isinstance(self.anchors, list):
            anchors = []
            for anchors_type_0_item_data in self.anchors:
                anchors_type_0_item = anchors_type_0_item_data.to_dict()
                anchors.append(anchors_type_0_item)


        else:
            anchors = self.anchors

        pending: list[dict[str, Any]] | None | Unset
        if isinstance(self.pending, Unset):
            pending = UNSET
        elif isinstance(self.pending, list):
            pending = []
            for pending_type_0_item_data in self.pending:
                pending_type_0_item = pending_type_0_item_data.to_dict()
                pending.append(pending_type_0_item)


        else:
            pending = self.pending


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchor_schedule_local is not UNSET:
            field_dict["anchor_schedule_local"] = anchor_schedule_local
        if anchors is not UNSET:
            field_dict["anchors"] = anchors
        if pending is not UNSET:
            field_dict["pending"] = pending

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_pending_anchor_bundle_dto import HarvestPendingAnchorBundleDto # noqa: PLC0415
        from ..models.harvest_workspace_anchor_dto import HarvestWorkspaceAnchorDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_anchor_schedule_local(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anchor_schedule_local = _parse_anchor_schedule_local(d.pop("anchor_schedule_local", UNSET))


        def _parse_anchors(data: object) -> list[HarvestWorkspaceAnchorDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                anchors_type_0 = []
                _anchors_type_0 = data
                for anchors_type_0_item_data in (_anchors_type_0):
                    anchors_type_0_item = HarvestWorkspaceAnchorDto.from_dict(anchors_type_0_item_data)



                    anchors_type_0.append(anchors_type_0_item)

                return anchors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestWorkspaceAnchorDto] | None | Unset, data)

        anchors = _parse_anchors(d.pop("anchors", UNSET))


        def _parse_pending(data: object) -> list[HarvestPendingAnchorBundleDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pending_type_0 = []
                _pending_type_0 = data
                for pending_type_0_item_data in (_pending_type_0):
                    pending_type_0_item = HarvestPendingAnchorBundleDto.from_dict(pending_type_0_item_data)



                    pending_type_0.append(pending_type_0_item)

                return pending_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestPendingAnchorBundleDto] | None | Unset, data)

        pending = _parse_pending(d.pop("pending", UNSET))


        harvest_trace_anchors_response = cls(
            anchor_schedule_local=anchor_schedule_local,
            anchors=anchors,
            pending=pending,
        )

        return harvest_trace_anchors_response

