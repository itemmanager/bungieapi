# generated by update to not change manually
import dataclasses as dt
import typing as t


@dt.dataclass(frozen=True)
class DestinyVendorReceiptsComponent:
    """For now, this isn't used for much: it's a record of the recent
    refundable purchases that the user has made.

    In the future, it could be used for providing refunds/buyback via
    the API. Wouldn't that be fun?
    """

    receipts: t.Sequence[
        "DestinyVendorReceipt"
    ]  # The receipts for refundable purchases made at a vendor.


@dt.dataclass(frozen=True)
class DestinyProfileComponent:
    """The most essential summary information about a Profile (in Destiny 1, we
    called these "Accounts")."""

    user_info: "UserInfoCard"  # If you need to render the Profile (their platform name, icon, etc...) somewhere, this property contains that information.
    date_last_played: str  # The last time the user played with any character on this Profile.
    versions_owned: "DestinyGameVersions"  # If you want to know what expansions they own, this will contain that data.  IMPORTANT: This field may not return the data you're interested in for Cross-Saved users. It returns the last ownership data we saw for this account - which is to say, what they've purchased on the platform on which they last played, which now could be a different platform.  If you don't care about per-platform ownership and only care about whatever platform it seems they are playing on most recently, then this should be "good enough." Otherwise, this should be considered deprecated. We do not have a good alternative to provide at this time with platform specific ownership data for DLC.
    character_ids: t.Sequence[
        int
    ]  # A list of the character IDs, for further querying on your part.
    season_hashes: t.Sequence[
        int
    ]  # A list of seasons that this profile owns. Unlike versionsOwned, these stay with the profile across Platforms, and thus will be valid.  It turns out that Stadia Pro subscriptions will give access to seasons but only while playing on Stadia and with an active subscription. So some users (users who have Stadia Pro but choose to play on some other platform) won't see these as available: it will be whatever seasons are available for the platform on which they last played.
    current_season_hash: int  # If populated, this is a reference to the season that is currently active.
    current_season_reward_power_cap: int  # If populated, this is the reward power cap for the current season.


from bungieapi.generated.types.destiny import DestinyGameVersions  # noqa: E402

# imported at the end to do not case circular imports for type annotations
from bungieapi.generated.types.destiny.vendors import DestinyVendorReceipt  # noqa: E402
from bungieapi.generated.types.user import UserInfoCard  # noqa: E402
