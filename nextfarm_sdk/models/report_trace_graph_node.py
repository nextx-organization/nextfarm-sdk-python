from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.report_trace_node import ReportTraceNode





T = TypeVar("T", bound="ReportTraceGraphNode")



@_attrs_define
class ReportTraceGraphNode:
    

    id: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    level: int | Unset = UNSET
    node: ReportTraceNode | Unset = UNSET
    ref: None | str | Unset = UNSET
    restricted: bool | Unset = UNSET
    service: None | str | Unset = UNSET
    source_error: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_trace_node import ReportTraceNode # noqa: PLC0415
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

        level = self.level

        node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        ref: None | str | Unset
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref

        restricted = self.restricted

        service: None | str | Unset
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service

        source_error = self.source_error


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if level is not UNSET:
            field_dict["level"] = level
        if node is not UNSET:
            field_dict["node"] = node
        if ref is not UNSET:
            field_dict["ref"] = ref
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if service is not UNSET:
            field_dict["service"] = service
        if source_error is not UNSET:
            field_dict["sourceError"] = source_error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_trace_node import ReportTraceNode # noqa: PLC0415
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


        level = d.pop("level", UNSET)

        _node = d.pop("node", UNSET)
        node: ReportTraceNode | Unset
        if isinstance(_node,  Unset):
            node = UNSET
        else:
            node = ReportTraceNode.from_dict(_node)




        def _parse_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref = _parse_ref(d.pop("ref", UNSET))


        restricted = d.pop("restricted", UNSET)

        def _parse_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service = _parse_service(d.pop("service", UNSET))


        source_error = d.pop("sourceError", UNSET)

        report_trace_graph_node = cls(
            id=id,
            kind=kind,
            level=level,
            node=node,
            ref=ref,
            restricted=restricted,
            service=service,
            source_error=source_error,
        )

        return report_trace_graph_node

