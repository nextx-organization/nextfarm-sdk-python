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
  from ..models.harvest_create_field_log_input_request import HarvestCreateFieldLogInputRequest





T = TypeVar("T", bound="HarvestCreateFieldLogRequest")



@_attrs_define
class HarvestCreateFieldLogRequest:
    

    client_request_id: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    for_owner_id: None | Unset | UUID = UNSET
    inputs: list[HarvestCreateFieldLogInputRequest] | None | Unset = UNSET
    organism_ids: list[UUID] | None | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    photo_paths: list[str] | None | Unset = UNSET
    recorded_via: None | str | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    spray_active_ingredient: None | str | Unset = UNSET
    spray_phi_days: int | None | Unset = UNSET
    spray_product_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    work_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_create_field_log_input_request import HarvestCreateFieldLogInputRequest # noqa: PLC0415
        client_request_id: None | str | Unset
        if isinstance(self.client_request_id, Unset):
            client_request_id = UNSET
        else:
            client_request_id = self.client_request_id

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        for_owner_id: None | str | Unset
        if isinstance(self.for_owner_id, Unset):
            for_owner_id = UNSET
        elif isinstance(self.for_owner_id, UUID):
            for_owner_id = str(self.for_owner_id)
        else:
            for_owner_id = self.for_owner_id

        inputs: list[dict[str, Any]] | None | Unset
        if isinstance(self.inputs, Unset):
            inputs = UNSET
        elif isinstance(self.inputs, list):
            inputs = []
            for inputs_type_0_item_data in self.inputs:
                inputs_type_0_item = inputs_type_0_item_data.to_dict()
                inputs.append(inputs_type_0_item)


        else:
            inputs = self.inputs

        organism_ids: list[str] | None | Unset
        if isinstance(self.organism_ids, Unset):
            organism_ids = UNSET
        elif isinstance(self.organism_ids, list):
            organism_ids = []
            for organism_ids_type_0_item_data in self.organism_ids:
                organism_ids_type_0_item = str(organism_ids_type_0_item_data)
                organism_ids.append(organism_ids_type_0_item)


        else:
            organism_ids = self.organism_ids

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        photo_paths: list[str] | None | Unset
        if isinstance(self.photo_paths, Unset):
            photo_paths = UNSET
        elif isinstance(self.photo_paths, list):
            photo_paths = self.photo_paths


        else:
            photo_paths = self.photo_paths

        recorded_via: None | str | Unset
        if isinstance(self.recorded_via, Unset):
            recorded_via = UNSET
        else:
            recorded_via = self.recorded_via

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        spray_active_ingredient: None | str | Unset
        if isinstance(self.spray_active_ingredient, Unset):
            spray_active_ingredient = UNSET
        else:
            spray_active_ingredient = self.spray_active_ingredient

        spray_phi_days: int | None | Unset
        if isinstance(self.spray_phi_days, Unset):
            spray_phi_days = UNSET
        else:
            spray_phi_days = self.spray_phi_days

        spray_product_name: None | str | Unset
        if isinstance(self.spray_product_name, Unset):
            spray_product_name = UNSET
        else:
            spray_product_name = self.spray_product_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        work_type: None | str | Unset
        if isinstance(self.work_type, Unset):
            work_type = UNSET
        else:
            work_type = self.work_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if client_request_id is not UNSET:
            field_dict["client_request_id"] = client_request_id
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if for_owner_id is not UNSET:
            field_dict["for_owner_id"] = for_owner_id
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if organism_ids is not UNSET:
            field_dict["organism_ids"] = organism_ids
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if photo_paths is not UNSET:
            field_dict["photo_paths"] = photo_paths
        if recorded_via is not UNSET:
            field_dict["recorded_via"] = recorded_via
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if spray_active_ingredient is not UNSET:
            field_dict["spray_active_ingredient"] = spray_active_ingredient
        if spray_phi_days is not UNSET:
            field_dict["spray_phi_days"] = spray_phi_days
        if spray_product_name is not UNSET:
            field_dict["spray_product_name"] = spray_product_name
        if title is not UNSET:
            field_dict["title"] = title
        if work_type is not UNSET:
            field_dict["work_type"] = work_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_create_field_log_input_request import HarvestCreateFieldLogInputRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_client_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_request_id = _parse_client_request_id(d.pop("client_request_id", UNSET))


        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))


        def _parse_for_owner_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                for_owner_id_type_0 = UUID(data)



                return for_owner_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        for_owner_id = _parse_for_owner_id(d.pop("for_owner_id", UNSET))


        def _parse_inputs(data: object) -> list[HarvestCreateFieldLogInputRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inputs_type_0 = []
                _inputs_type_0 = data
                for inputs_type_0_item_data in (_inputs_type_0):
                    inputs_type_0_item = HarvestCreateFieldLogInputRequest.from_dict(inputs_type_0_item_data)



                    inputs_type_0.append(inputs_type_0_item)

                return inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestCreateFieldLogInputRequest] | None | Unset, data)

        inputs = _parse_inputs(d.pop("inputs", UNSET))


        def _parse_organism_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organism_ids_type_0 = []
                _organism_ids_type_0 = data
                for organism_ids_type_0_item_data in (_organism_ids_type_0):
                    organism_ids_type_0_item = UUID(organism_ids_type_0_item_data)



                    organism_ids_type_0.append(organism_ids_type_0_item)

                return organism_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        organism_ids = _parse_organism_ids(d.pop("organism_ids", UNSET))


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        def _parse_photo_paths(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                photo_paths_type_0 = cast(list[str], data)

                return photo_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        photo_paths = _parse_photo_paths(d.pop("photo_paths", UNSET))


        def _parse_recorded_via(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recorded_via = _parse_recorded_via(d.pop("recorded_via", UNSET))


        def _parse_season_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_id_type_0 = UUID(data)



                return season_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        season_id = _parse_season_id(d.pop("season_id", UNSET))


        def _parse_spray_active_ingredient(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spray_active_ingredient = _parse_spray_active_ingredient(d.pop("spray_active_ingredient", UNSET))


        def _parse_spray_phi_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spray_phi_days = _parse_spray_phi_days(d.pop("spray_phi_days", UNSET))


        def _parse_spray_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spray_product_name = _parse_spray_product_name(d.pop("spray_product_name", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_work_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_type = _parse_work_type(d.pop("work_type", UNSET))


        harvest_create_field_log_request = cls(
            client_request_id=client_request_id,
            completed_at=completed_at,
            for_owner_id=for_owner_id,
            inputs=inputs,
            organism_ids=organism_ids,
            parcel_id=parcel_id,
            photo_paths=photo_paths,
            recorded_via=recorded_via,
            season_id=season_id,
            spray_active_ingredient=spray_active_ingredient,
            spray_phi_days=spray_phi_days,
            spray_product_name=spray_product_name,
            title=title,
            work_type=work_type,
        )

        return harvest_create_field_log_request

