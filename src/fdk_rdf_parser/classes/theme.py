from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConceptSchema:
    id: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    versioninfo: Optional[str] = None
    versionnumber: Optional[str] = None


@dataclass
class ThemeEU:
    id: Optional[str] = None
    code: Optional[str] = None
    startUse: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    conceptSchema: Optional[ConceptSchema] = None

    def addValuesFromDict(self: Any, dict: Dict) -> None:
        self.id = str(dict.get("id")) if dict.get("id") is not None else None
        self.code = str(dict.get("code")) if dict.get("code") is not None else None
        self.startUse = (
            str(dict.get("startUse")) if dict.get("startUse") is not None else None
        )
        self.title = dict.get("title")
        self.conceptSchema = (
            ConceptSchema(
                id=str(dict["conceptSchema"].get("id"))
                if dict["conceptSchema"].get("id") is not None
                else None,
                title=dict["conceptSchema"].get("title"),
                versioninfo=str(dict["conceptSchema"].get("versioninfo"))
                if dict["conceptSchema"].get("versioninfo") is not None
                else None,
                versionnumber=str(dict["conceptSchema"].get("versionnumber"))
                if dict["conceptSchema"].get("versionnumber") is not None
                else None,
            )
            if dict.get("conceptSchema") is not None
            else None
        )


@dataclass
class ThemeLOS:
    children: Optional[List[str]] = None
    parents: Optional[List[str]] = None
    isTema: Optional[bool] = None
    losPaths: Optional[List[str]] = None
    name: Optional[Dict[str, str]] = None
    definition: Optional[Dict[str, str]] = None
    uri: Optional[str] = None
    synonyms: Optional[List[str]] = None
    relatedTerms: Optional[List[str]] = None

    def addValuesFromDict(self: Any, dict: Dict) -> None:
        self.children = dict.get("children")
        self.parents = dict.get("parents")
        self.isTema = dict.get("isTema")
        self.losPaths = dict.get("losPaths")
        self.name = dict.get("name")
        self.definition = dict.get("definition")
        self.uri = str(dict.get("uri")) if dict.get("uri") is not None else None
        self.synonyms = dict.get("synonyms")
        self.relatedTerms = dict.get("relatedTerms")
