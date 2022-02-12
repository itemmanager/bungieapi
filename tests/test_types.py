import dataclasses as dt

from bungieapi.forge import forge
from bungieapi.generated.components.schemas.user import OptInFlags
from bungieapi.types import ManifestReference, decompose


def test_can_create_bitmask():
    assert (OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS).value == 8 + 64
    assert (
        OptInFlags.USER_RESEARCH | OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS
    ).value == 8 + 64


def test_can_decompose_flag():
    assert {OptInFlags.USER_RESEARCH, OptInFlags.PLAY_TESTS} == decompose(
        OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS
    )


def test_manifest_reference_can_be_structured():
    @dt.dataclass
    class A:
        pass

    @dt.dataclass
    class B:
        a: ManifestReference[A]

    forged = forge(B, {"a": "42"})
    assert forged.a.type == A
    assert forged.a.hash == "42"


def test_manifest_reference_can_be_structured_with_forward_ref():
    @dt.dataclass
    class A:
        pass

    globals()["A"] = A

    @dt.dataclass
    class B:
        a: ManifestReference["A"]

    forged = forge(B, {"a": "42"})
    assert forged.a.type == A
    assert forged.a.hash == "42"
