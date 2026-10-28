from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.harvest_ics_result_item import HarvestIcsResultItem





T = TypeVar("T", bound="HarvestIcsInspectionRequest")



@_attrs_define
class HarvestIcsInspectionRequest:
    

    checklist_id: UUID | Unset = UNSET
    client_key: None | str | Unset = UNSET
    farmer_acknowledged: bool | Unset = UNSET
    inspected_on: datetime.date | Unset = UNSET
    inspector_name: None | str | Unset = UNSET
    member_id: UUID | Unset = UNSET
    note: None | str | Unset = UNSET
    results: list[HarvestIcsResultItem] | None | Unset = UNSET
    submit: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_ics_result_item import HarvestIcsResultItem # noqa: PLC0415
        checklist_id: str | Unset = UNSET
        if not isinstance(self.checklist_id, Unset):
            checklist_id = str(self.checklist_id)

        client_key: None | str | Unset
        if isinstance(self.client_key, Unset):
            client_key = UNSET
        else:
            client_key = self.client_key

        farmer_acknowledged = self.farmer_acknowledged

        inspected_on: str | Unset = UNSET
        if not isinstance(self.inspected_on, Unset):
            inspected_on = self.inspected_on.isoformat()

        inspector_name: None | str | Unset
        if isinstance(self.inspector_name, Unset):
            inspector_name = UNSET
        else:
            inspector_name = self.inspector_name

        member_id: str | Unset = UNSET
        if not isinstance(self.member_id, Unset):
            member_id = str(self.member_id)

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)


        else:
            results = self.results

        submit = self.submit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if checklist_id is not UNSET:
            field_dict["checklist_id"] = checklist_id
        if client_key is not UNSET:
            field_dict["client_key"] = client_key
        if farmer_acknowledged is not UNSET:
            field_dict["farmer_acknowledged"] = farmer_acknowledged
        if inspected_on is not UNSET:
            field_dict["inspected_on"] = inspected_on
        if inspector_name is not UNSET:
            field_dict["inspector_name"] = inspector_name
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if note is not UNSET:
            field_dict["note"] = note
        if results is not UNSET:
            field_dict["results"] = results
        if submit is not UNSET:
            field_dict["submit"] = submit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_ics_result_item import HarvestIcsResultItem # noqa: PLC0415
        d = dict(src_dict)
        _checklist_id = d.pop("checklist_id", UNSET)
        checklist_id: UUID | Unset
        if isinstance(_checklist_id,  Unset):
            checklist_id = UNSET
        else:
            checklist_id = UUID(_checklist_id)




        def _parse_client_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_key = _parse_client_key(d.pop("client_key", UNSET))


        farmer_acknowledged = d.pop("farmer_acknowledged", UNSET)

        _inspected_on = d.pop("inspected_on", UNSET)
        inspected_on: datetime.date | Unset
        if isinstance(_inspected_on,  Unset):
            inspected_on = UNSET
        else:
            inspected_on = datetime.date.fromisoformat(_inspected_on)




        def _parse_inspector_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inspector_name = _parse_inspector_name(d.pop("inspector_name", UNSET))


        _member_id = d.pop("member_id", UNSET)
        member_id: UUID | Unset
        if isinstance(_member_id,  Unset):
            member_id = UNSET
        else:
            member_id = UUID(_member_id)




        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_results(data: object) -> list[HarvestIcsResultItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in (_results_type_0):
                    results_type_0_item = HarvestIcsResultItem.from_dict(results_type_0_item_data)



                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestIcsResultItem] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))


        submit = d.pop("submit", UNSET)

        harvest_ics_inspection_request = cls(
            checklist_id=checklist_id,
            client_key=client_key,
            farmer_acknowledged=farmer_acknowledged,
            inspected_on=inspected_on,
            inspector_name=inspector_name,
            member_id=member_id,
            note=note,
            results=results,
            submit=submit,
        )

        return harvest_ics_inspection_request

