# generated by update to not change manually
import dataclasses as dt
import typing as t

from bungieapi.json import to_json


@dt.dataclass(frozen=True)
class UserTheme:
    user_theme_description: str
    user_theme_id: int
    user_theme_name: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "userThemeId": to_json(self.user_theme_id),
            "userThemeName": to_json(self.user_theme_name),
            "userThemeDescription": to_json(self.user_theme_description),
        }


@dt.dataclass(frozen=True)
class GroupTheme:
    description: str
    folder: str
    name: str

    def to_json(self) -> t.Mapping[str, t.Any]:
        return {
            "name": to_json(self.name),
            "folder": to_json(self.folder),
            "description": to_json(self.description),
        }
