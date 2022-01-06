from bungieapi.generated.components.schemas.user import OptInFlags


def test_can_create_bitmask():
    assert (OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS).value == 8 + 64
    assert (
        OptInFlags.USER_RESEARCH | OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS
    ).value == 8 + 64


def test_can_decompose_type():
    assert {OptInFlags.USER_RESEARCH, OptInFlags.PLAY_TESTS} == set(
        OptInFlags.USER_RESEARCH | OptInFlags.PLAY_TESTS
    )
