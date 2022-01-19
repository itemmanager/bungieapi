from bungieapi.generated.components.schemas.user import OptInFlags
from bungieapi.types import decompose


def test_can_create_bitmask():
    assert (OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS).value == 8 + 64
    assert (
        OptInFlags.USER_RESEARCH | OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS
    ).value == 8 + 64


def test_can_decompose_flag():
    assert {OptInFlags.USER_RESEARCH, OptInFlags.PLAY_TESTS} == decompose(
        OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS
    )
