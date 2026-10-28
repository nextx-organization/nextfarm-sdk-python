from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_spotlight_hit import HarvestSpotlightHit





T = TypeVar("T", bound="HarvestHarvestSearchResult")



@_attrs_define
class HarvestHarvestSearchResult:
    

    certifications: list[HarvestSpotlightHit] | None | Unset = UNSET
    harvests: list[HarvestSpotlightHit] | None | Unset = UNSET
    qr_codes: list[HarvestSpotlightHit] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_spotlight_hit import HarvestSpotlightHit # noqa: PLC0415
        certifications: list[dict[str, Any]] | None | Unset
        if isinstance(self.certifications, Unset):
            certifications = UNSET
        elif isinstance(self.certifications, list):
            certifications = []
            for certifications_type_0_item_data in self.certifications:
                certifications_type_0_item = certifications_type_0_item_data.to_dict()
                certifications.append(certifications_type_0_item)


        else:
            certifications = self.certifications

        harvests: list[dict[str, Any]] | None | Unset
        if isinstance(self.harvests, Unset):
            harvests = UNSET
        elif isinstance(self.harvests, list):
            harvests = []
            for harvests_type_0_item_data in self.harvests:
                harvests_type_0_item = harvests_type_0_item_data.to_dict()
                harvests.append(harvests_type_0_item)


        else:
            harvests = self.harvests

        qr_codes: list[dict[str, Any]] | None | Unset
        if isinstance(self.qr_codes, Unset):
            qr_codes = UNSET
        elif isinstance(self.qr_codes, list):
            qr_codes = []
            for qr_codes_type_0_item_data in self.qr_codes:
                qr_codes_type_0_item = qr_codes_type_0_item_data.to_dict()
                qr_codes.append(qr_codes_type_0_item)


        else:
            qr_codes = self.qr_codes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if harvests is not UNSET:
            field_dict["harvests"] = harvests
        if qr_codes is not UNSET:
            field_dict["qr_codes"] = qr_codes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_spotlight_hit import HarvestSpotlightHit # noqa: PLC0415
        d = dict(src_dict)
        def _parse_certifications(data: object) -> list[HarvestSpotlightHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                certifications_type_0 = []
                _certifications_type_0 = data
                for certifications_type_0_item_data in (_certifications_type_0):
                    certifications_type_0_item = HarvestSpotlightHit.from_dict(certifications_type_0_item_data)



                    certifications_type_0.append(certifications_type_0_item)

                return certifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestSpotlightHit] | None | Unset, data)

        certifications = _parse_certifications(d.pop("certifications", UNSET))


        def _parse_harvests(data: object) -> list[HarvestSpotlightHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                harvests_type_0 = []
                _harvests_type_0 = data
                for harvests_type_0_item_data in (_harvests_type_0):
                    harvests_type_0_item = HarvestSpotlightHit.from_dict(harvests_type_0_item_data)



                    harvests_type_0.append(harvests_type_0_item)

                return harvests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestSpotlightHit] | None | Unset, data)

        harvests = _parse_harvests(d.pop("harvests", UNSET))


        def _parse_qr_codes(data: object) -> list[HarvestSpotlightHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                qr_codes_type_0 = []
                _qr_codes_type_0 = data
                for qr_codes_type_0_item_data in (_qr_codes_type_0):
                    qr_codes_type_0_item = HarvestSpotlightHit.from_dict(qr_codes_type_0_item_data)



                    qr_codes_type_0.append(qr_codes_type_0_item)

                return qr_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestSpotlightHit] | None | Unset, data)

        qr_codes = _parse_qr_codes(d.pop("qr_codes", UNSET))


        harvest_harvest_search_result = cls(
            certifications=certifications,
            harvests=harvests,
            qr_codes=qr_codes,
        )

        return harvest_harvest_search_result

