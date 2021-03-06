# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class DestinyManifest:
    """DestinyManifest is the external-facing contract for just the properties
    needed by those calling the Destiny Platform."""

    icon_image_pyramid_info: t.Sequence["ImagePyramidEntry"] = dt.field(
        metadata={
            "description": 'Information about the "Image Pyramid" for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the "original/full size" Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable)'
        }
    )
    json_world_component_content_paths: t.Mapping[str, t.Mapping[str, str]] = dt.field(
        metadata={
            "description": "This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term."
        }
    )
    json_world_content_paths: t.Mapping[str, str] = dt.field(
        metadata={
            "description": "This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!)"
        }
    )
    mobile_asset_content_path: str
    mobile_clan_banner_database_path: str
    mobile_gear_asset_data_bases: t.Sequence["GearAssetDataBaseDefinition"]
    mobile_gear_cdn: t.Mapping[str, str]
    mobile_world_content_paths: t.Mapping[str, str]
    version: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "version": to_json(self.version),
            "mobileAssetContentPath": to_json(self.mobile_asset_content_path),
            "mobileGearAssetDataBases": to_json(self.mobile_gear_asset_data_bases),
            "mobileWorldContentPaths": to_json(self.mobile_world_content_paths),
            "jsonWorldContentPaths": to_json(self.json_world_content_paths),
            "jsonWorldComponentContentPaths": to_json(
                self.json_world_component_content_paths
            ),
            "mobileClanBannerDatabasePath": to_json(
                self.mobile_clan_banner_database_path
            ),
            "mobileGearCDN": to_json(self.mobile_gear_cdn),
            "iconImagePyramidInfo": to_json(self.icon_image_pyramid_info),
        }


@dt.dataclass(frozen=True)
class GearAssetDataBaseDefinition:
    path: str
    version: int

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "version": to_json(self.version),
            "path": to_json(self.path),
        }


@dt.dataclass(frozen=True)
class ImagePyramidEntry:
    factor: float = dt.field(
        metadata={
            "description": "The factor by which the original image size has been reduced."
        }
    )
    name: str = dt.field(
        metadata={
            "description": "The name of the subfolder where these images are located."
        }
    )

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "name": to_json(self.name),
            "factor": to_json(self.factor),
        }
