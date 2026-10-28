from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.report_trace_graph_edge import ReportTraceGraphEdge
  from ..models.report_trace_graph_node import ReportTraceGraphNode





T = TypeVar("T", bound="ReportTraceGraphResult")



@_attrs_define
class ReportTraceGraphResult:
    

    edges: list[ReportTraceGraphEdge] | None | Unset = UNSET
    nodes: list[ReportTraceGraphNode] | None | Unset = UNSET
    root: None | str | Unset = UNSET
    truncated: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_trace_graph_edge import ReportTraceGraphEdge # noqa: PLC0415
        from ..models.report_trace_graph_node import ReportTraceGraphNode # noqa: PLC0415
        edges: list[dict[str, Any]] | None | Unset
        if isinstance(self.edges, Unset):
            edges = UNSET
        elif isinstance(self.edges, list):
            edges = []
            for edges_type_0_item_data in self.edges:
                edges_type_0_item = edges_type_0_item_data.to_dict()
                edges.append(edges_type_0_item)


        else:
            edges = self.edges

        nodes: list[dict[str, Any]] | None | Unset
        if isinstance(self.nodes, Unset):
            nodes = UNSET
        elif isinstance(self.nodes, list):
            nodes = []
            for nodes_type_0_item_data in self.nodes:
                nodes_type_0_item = nodes_type_0_item_data.to_dict()
                nodes.append(nodes_type_0_item)


        else:
            nodes = self.nodes

        root: None | str | Unset
        if isinstance(self.root, Unset):
            root = UNSET
        else:
            root = self.root

        truncated = self.truncated


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if edges is not UNSET:
            field_dict["edges"] = edges
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if root is not UNSET:
            field_dict["root"] = root
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_trace_graph_edge import ReportTraceGraphEdge # noqa: PLC0415
        from ..models.report_trace_graph_node import ReportTraceGraphNode # noqa: PLC0415
        d = dict(src_dict)
        def _parse_edges(data: object) -> list[ReportTraceGraphEdge] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                edges_type_0 = []
                _edges_type_0 = data
                for edges_type_0_item_data in (_edges_type_0):
                    edges_type_0_item = ReportTraceGraphEdge.from_dict(edges_type_0_item_data)



                    edges_type_0.append(edges_type_0_item)

                return edges_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportTraceGraphEdge] | None | Unset, data)

        edges = _parse_edges(d.pop("edges", UNSET))


        def _parse_nodes(data: object) -> list[ReportTraceGraphNode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nodes_type_0 = []
                _nodes_type_0 = data
                for nodes_type_0_item_data in (_nodes_type_0):
                    nodes_type_0_item = ReportTraceGraphNode.from_dict(nodes_type_0_item_data)



                    nodes_type_0.append(nodes_type_0_item)

                return nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportTraceGraphNode] | None | Unset, data)

        nodes = _parse_nodes(d.pop("nodes", UNSET))


        def _parse_root(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root = _parse_root(d.pop("root", UNSET))


        truncated = d.pop("truncated", UNSET)

        report_trace_graph_result = cls(
            edges=edges,
            nodes=nodes,
            root=root,
            truncated=truncated,
        )

        return report_trace_graph_result

