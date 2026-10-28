from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeDocTreeMigrationResultDto")



@_attrs_define
class OfficeDocTreeMigrationResultDto:
    

    docs: int | Unset = UNSET
    dry_run: bool | Unset = UNSET
    files: int | Unset = UNSET
    folders: int | Unset = UNSET
    permissions: int | Unset = UNSET
    skipped_existing: int | Unset = UNSET
    skipped_orphans: int | Unset = UNSET
    spaces: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        docs = self.docs

        dry_run = self.dry_run

        files = self.files

        folders = self.folders

        permissions = self.permissions

        skipped_existing = self.skipped_existing

        skipped_orphans = self.skipped_orphans

        spaces = self.spaces


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if docs is not UNSET:
            field_dict["docs"] = docs
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if files is not UNSET:
            field_dict["files"] = files
        if folders is not UNSET:
            field_dict["folders"] = folders
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if skipped_existing is not UNSET:
            field_dict["skippedExisting"] = skipped_existing
        if skipped_orphans is not UNSET:
            field_dict["skippedOrphans"] = skipped_orphans
        if spaces is not UNSET:
            field_dict["spaces"] = spaces

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        docs = d.pop("docs", UNSET)

        dry_run = d.pop("dryRun", UNSET)

        files = d.pop("files", UNSET)

        folders = d.pop("folders", UNSET)

        permissions = d.pop("permissions", UNSET)

        skipped_existing = d.pop("skippedExisting", UNSET)

        skipped_orphans = d.pop("skippedOrphans", UNSET)

        spaces = d.pop("spaces", UNSET)

        office_doc_tree_migration_result_dto = cls(
            docs=docs,
            dry_run=dry_run,
            files=files,
            folders=folders,
            permissions=permissions,
            skipped_existing=skipped_existing,
            skipped_orphans=skipped_orphans,
            spaces=spaces,
        )

        return office_doc_tree_migration_result_dto

