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
  from ..models.harvest_anchored_bundle_dto import HarvestAnchoredBundleDto





T = TypeVar("T", bound="HarvestWorkspaceAnchorDto")



@_attrs_define
class HarvestWorkspaceAnchorDto:
    

    anchor_date: datetime.date | Unset = UNSET
    attempts: int | Unset = UNSET
    bitcoin_block_height: int | None | Unset = UNSET
    bitcoin_confirmed_at: datetime.datetime | None | Unset = UNSET
    bundles: list[HarvestAnchoredBundleDto] | None | Unset = UNSET
    confirmed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    is_backfill: bool | Unset = UNSET
    leaf_count: int | Unset = UNSET
    merkle_root: None | str | Unset = UNSET
    polygon_chain_id: int | None | Unset = UNSET
    polygon_confirmed_at: datetime.datetime | None | Unset = UNSET
    polygon_tx_hash: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_anchored_bundle_dto import HarvestAnchoredBundleDto # noqa: PLC0415
        anchor_date: str | Unset = UNSET
        if not isinstance(self.anchor_date, Unset):
            anchor_date = self.anchor_date.isoformat()

        attempts = self.attempts

        bitcoin_block_height: int | None | Unset
        if isinstance(self.bitcoin_block_height, Unset):
            bitcoin_block_height = UNSET
        else:
            bitcoin_block_height = self.bitcoin_block_height

        bitcoin_confirmed_at: None | str | Unset
        if isinstance(self.bitcoin_confirmed_at, Unset):
            bitcoin_confirmed_at = UNSET
        elif isinstance(self.bitcoin_confirmed_at, datetime.datetime):
            bitcoin_confirmed_at = self.bitcoin_confirmed_at.isoformat()
        else:
            bitcoin_confirmed_at = self.bitcoin_confirmed_at

        bundles: list[dict[str, Any]] | None | Unset
        if isinstance(self.bundles, Unset):
            bundles = UNSET
        elif isinstance(self.bundles, list):
            bundles = []
            for bundles_type_0_item_data in self.bundles:
                bundles_type_0_item = bundles_type_0_item_data.to_dict()
                bundles.append(bundles_type_0_item)


        else:
            bundles = self.bundles

        confirmed_at: None | str | Unset
        if isinstance(self.confirmed_at, Unset):
            confirmed_at = UNSET
        elif isinstance(self.confirmed_at, datetime.datetime):
            confirmed_at = self.confirmed_at.isoformat()
        else:
            confirmed_at = self.confirmed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_backfill = self.is_backfill

        leaf_count = self.leaf_count

        merkle_root: None | str | Unset
        if isinstance(self.merkle_root, Unset):
            merkle_root = UNSET
        else:
            merkle_root = self.merkle_root

        polygon_chain_id: int | None | Unset
        if isinstance(self.polygon_chain_id, Unset):
            polygon_chain_id = UNSET
        else:
            polygon_chain_id = self.polygon_chain_id

        polygon_confirmed_at: None | str | Unset
        if isinstance(self.polygon_confirmed_at, Unset):
            polygon_confirmed_at = UNSET
        elif isinstance(self.polygon_confirmed_at, datetime.datetime):
            polygon_confirmed_at = self.polygon_confirmed_at.isoformat()
        else:
            polygon_confirmed_at = self.polygon_confirmed_at

        polygon_tx_hash: None | str | Unset
        if isinstance(self.polygon_tx_hash, Unset):
            polygon_tx_hash = UNSET
        else:
            polygon_tx_hash = self.polygon_tx_hash

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchor_date is not UNSET:
            field_dict["anchor_date"] = anchor_date
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if bitcoin_block_height is not UNSET:
            field_dict["bitcoin_block_height"] = bitcoin_block_height
        if bitcoin_confirmed_at is not UNSET:
            field_dict["bitcoin_confirmed_at"] = bitcoin_confirmed_at
        if bundles is not UNSET:
            field_dict["bundles"] = bundles
        if confirmed_at is not UNSET:
            field_dict["confirmed_at"] = confirmed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_backfill is not UNSET:
            field_dict["is_backfill"] = is_backfill
        if leaf_count is not UNSET:
            field_dict["leaf_count"] = leaf_count
        if merkle_root is not UNSET:
            field_dict["merkle_root"] = merkle_root
        if polygon_chain_id is not UNSET:
            field_dict["polygon_chain_id"] = polygon_chain_id
        if polygon_confirmed_at is not UNSET:
            field_dict["polygon_confirmed_at"] = polygon_confirmed_at
        if polygon_tx_hash is not UNSET:
            field_dict["polygon_tx_hash"] = polygon_tx_hash
        if status is not UNSET:
            field_dict["status"] = status
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_anchored_bundle_dto import HarvestAnchoredBundleDto # noqa: PLC0415
        d = dict(src_dict)
        _anchor_date = d.pop("anchor_date", UNSET)
        anchor_date: datetime.date | Unset
        if isinstance(_anchor_date,  Unset):
            anchor_date = UNSET
        else:
            anchor_date = datetime.date.fromisoformat(_anchor_date)




        attempts = d.pop("attempts", UNSET)

        def _parse_bitcoin_block_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bitcoin_block_height = _parse_bitcoin_block_height(d.pop("bitcoin_block_height", UNSET))


        def _parse_bitcoin_confirmed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bitcoin_confirmed_at_type_0 = datetime.datetime.fromisoformat(data)



                return bitcoin_confirmed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        bitcoin_confirmed_at = _parse_bitcoin_confirmed_at(d.pop("bitcoin_confirmed_at", UNSET))


        def _parse_bundles(data: object) -> list[HarvestAnchoredBundleDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bundles_type_0 = []
                _bundles_type_0 = data
                for bundles_type_0_item_data in (_bundles_type_0):
                    bundles_type_0_item = HarvestAnchoredBundleDto.from_dict(bundles_type_0_item_data)



                    bundles_type_0.append(bundles_type_0_item)

                return bundles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestAnchoredBundleDto] | None | Unset, data)

        bundles = _parse_bundles(d.pop("bundles", UNSET))


        def _parse_confirmed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmed_at_type_0 = datetime.datetime.fromisoformat(data)



                return confirmed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        confirmed_at = _parse_confirmed_at(d.pop("confirmed_at", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_backfill = d.pop("is_backfill", UNSET)

        leaf_count = d.pop("leaf_count", UNSET)

        def _parse_merkle_root(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        merkle_root = _parse_merkle_root(d.pop("merkle_root", UNSET))


        def _parse_polygon_chain_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        polygon_chain_id = _parse_polygon_chain_id(d.pop("polygon_chain_id", UNSET))


        def _parse_polygon_confirmed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                polygon_confirmed_at_type_0 = datetime.datetime.fromisoformat(data)



                return polygon_confirmed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        polygon_confirmed_at = _parse_polygon_confirmed_at(d.pop("polygon_confirmed_at", UNSET))


        def _parse_polygon_tx_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polygon_tx_hash = _parse_polygon_tx_hash(d.pop("polygon_tx_hash", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = datetime.datetime.fromisoformat(data)



                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))


        harvest_workspace_anchor_dto = cls(
            anchor_date=anchor_date,
            attempts=attempts,
            bitcoin_block_height=bitcoin_block_height,
            bitcoin_confirmed_at=bitcoin_confirmed_at,
            bundles=bundles,
            confirmed_at=confirmed_at,
            created_at=created_at,
            id=id,
            is_backfill=is_backfill,
            leaf_count=leaf_count,
            merkle_root=merkle_root,
            polygon_chain_id=polygon_chain_id,
            polygon_confirmed_at=polygon_confirmed_at,
            polygon_tx_hash=polygon_tx_hash,
            status=status,
            submitted_at=submitted_at,
        )

        return harvest_workspace_anchor_dto

