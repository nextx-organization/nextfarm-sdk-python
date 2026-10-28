from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_dashboard_filter_target import OfficeDashboardFilterTarget





T = TypeVar("T", bound="OfficeDashboardFilterDef")



@_attrs_define
class OfficeDashboardFilterDef:
    

    id: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    targets: list[OfficeDashboardFilterTarget] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_dashboard_filter_target import OfficeDashboardFilterTarget # noqa: PLC0415
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        targets: list[dict[str, Any]] | None | Unset
        if isinstance(self.targets, Unset):
            targets = UNSET
        elif isinstance(self.targets, list):
            targets = []
            for targets_type_0_item_data in self.targets:
                targets_type_0_item = targets_type_0_item_data.to_dict()
                targets.append(targets_type_0_item)


        else:
            targets = self.targets


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_dashboard_filter_target import OfficeDashboardFilterTarget # noqa: PLC0415
        d = dict(src_dict)
        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_targets(data: object) -> list[OfficeDashboardFilterTarget] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                targets_type_0 = []
                _targets_type_0 = data
                for targets_type_0_item_data in (_targets_type_0):
                    targets_type_0_item = OfficeDashboardFilterTarget.from_dict(targets_type_0_item_data)



                    targets_type_0.append(targets_type_0_item)

                return targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDashboardFilterTarget] | None | Unset, data)

        targets = _parse_targets(d.pop("targets", UNSET))


        office_dashboard_filter_def = cls(
            id=id,
            kind=kind,
            label=label,
            targets=targets,
        )

        return office_dashboard_filter_def

