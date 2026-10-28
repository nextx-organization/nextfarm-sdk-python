from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestEudrDeclareRequest")



@_attrs_define
class HarvestEudrDeclareRequest:
    

    deforestation: None | str | Unset = UNSET
    deforestation_evidence: None | str | Unset = UNSET
    legality: None | str | Unset = UNSET
    legality_evidence: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deforestation: None | str | Unset
        if isinstance(self.deforestation, Unset):
            deforestation = UNSET
        else:
            deforestation = self.deforestation

        deforestation_evidence: None | str | Unset
        if isinstance(self.deforestation_evidence, Unset):
            deforestation_evidence = UNSET
        else:
            deforestation_evidence = self.deforestation_evidence

        legality: None | str | Unset
        if isinstance(self.legality, Unset):
            legality = UNSET
        else:
            legality = self.legality

        legality_evidence: None | str | Unset
        if isinstance(self.legality_evidence, Unset):
            legality_evidence = UNSET
        else:
            legality_evidence = self.legality_evidence


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deforestation is not UNSET:
            field_dict["deforestation"] = deforestation
        if deforestation_evidence is not UNSET:
            field_dict["deforestation_evidence"] = deforestation_evidence
        if legality is not UNSET:
            field_dict["legality"] = legality
        if legality_evidence is not UNSET:
            field_dict["legality_evidence"] = legality_evidence

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_deforestation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deforestation = _parse_deforestation(d.pop("deforestation", UNSET))


        def _parse_deforestation_evidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deforestation_evidence = _parse_deforestation_evidence(d.pop("deforestation_evidence", UNSET))


        def _parse_legality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legality = _parse_legality(d.pop("legality", UNSET))


        def _parse_legality_evidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legality_evidence = _parse_legality_evidence(d.pop("legality_evidence", UNSET))


        harvest_eudr_declare_request = cls(
            deforestation=deforestation,
            deforestation_evidence=deforestation_evidence,
            legality=legality,
            legality_evidence=legality_evidence,
        )

        return harvest_eudr_declare_request

