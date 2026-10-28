from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_link_input import OfficeTaskLinkInput





T = TypeVar("T", bound="OfficeSetTaskLinksRequest")



@_attrs_define
class OfficeSetTaskLinksRequest:
    

    links: list[OfficeTaskLinkInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_link_input import OfficeTaskLinkInput # noqa: PLC0415
        links: list[dict[str, Any]] | None | Unset
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)


        else:
            links = self.links


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_link_input import OfficeTaskLinkInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_links(data: object) -> list[OfficeTaskLinkInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in (_links_type_0):
                    links_type_0_item = OfficeTaskLinkInput.from_dict(links_type_0_item_data)



                    links_type_0.append(links_type_0_item)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskLinkInput] | None | Unset, data)

        links = _parse_links(d.pop("links", UNSET))


        office_set_task_links_request = cls(
            links=links,
        )

        return office_set_task_links_request

