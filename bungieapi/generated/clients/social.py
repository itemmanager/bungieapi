# generated by update to not change manually
from bungieapi.base import BaseClient
from bungieapi.forge import forge
from bungieapi.generated.components.responses import booleanClientResponse
from bungieapi.generated.components.responses.social.friends import (
    BungieFriendListClientResponse,
    BungieFriendRequestListClientResponse,
    PlatformFriendClientResponse,
)
from bungieapi.generated.components.schemas.social.friends import PlatformFriendType


class Client(BaseClient):
    async def get_friend_list(
        self,
    ) -> BungieFriendListClientResponse:
        """Returns your Bungie Friend list."""
        query = None
        result = await self.get(path="/Social/Friends/", query=query)
        return forge(BungieFriendListClientResponse, result)

    async def get_friend_request_list(
        self,
    ) -> BungieFriendRequestListClientResponse:
        """Returns your friend request queue."""
        query = None
        result = await self.get(path="/Social/Friends/Requests/", query=query)
        return forge(BungieFriendRequestListClientResponse, result)

    async def issue_friend_request(
        self,
        membership_id: str,
    ) -> booleanClientResponse:
        """Requests a friend relationship with the target user.

        Any of the target user's linked membership ids are valid inputs.
        Parameters:
            membership_id: The membership id of the user you wish to add.
        """
        query = None
        result = await self.post(
            path=f"/Social/Friends/Add/{membership_id}/", query=query
        )
        return forge(booleanClientResponse, result)

    async def accept_friend_request(
        self,
        membership_id: str,
    ) -> booleanClientResponse:
        """Accepts a friend relationship with the target user.

        The user must be on your incoming friend request list, though no error will occur if they are not.
        Parameters:
            membership_id: The membership id of the user you wish to accept.
        """
        query = None
        result = await self.post(
            path=f"/Social/Friends/Requests/Accept/{membership_id}/", query=query
        )
        return forge(booleanClientResponse, result)

    async def decline_friend_request(
        self,
        membership_id: str,
    ) -> booleanClientResponse:
        """Declines a friend relationship with the target user.

        The user must be on your incoming friend request list, though no error will occur if they are not.
        Parameters:
            membership_id: The membership id of the user you wish to decline.
        """
        query = None
        result = await self.post(
            path=f"/Social/Friends/Requests/Decline/{membership_id}/", query=query
        )
        return forge(booleanClientResponse, result)

    async def remove_friend(
        self,
        membership_id: str,
    ) -> booleanClientResponse:
        """Remove a friend relationship with the target user.

        The user must be on your friend list, though no error will occur if they are not.
        Parameters:
            membership_id: The membership id of the user you wish to remove.
        """
        query = None
        result = await self.post(
            path=f"/Social/Friends/Remove/{membership_id}/", query=query
        )
        return forge(booleanClientResponse, result)

    async def remove_friend_request(
        self,
        membership_id: str,
    ) -> booleanClientResponse:
        """Remove a friend relationship with the target user.

        The user must be on your outgoing request friend list, though no error will occur if they are not.
        Parameters:
            membership_id: The membership id of the user you wish to remove.
        """
        query = None
        result = await self.post(
            path=f"/Social/Friends/Requests/Remove/{membership_id}/", query=query
        )
        return forge(booleanClientResponse, result)

    async def get_platform_friend_list(
        self,
        friend_platform: "PlatformFriendType",
        page: str,
    ) -> PlatformFriendClientResponse:
        """Gets the platform friend of the requested type, with additional
        information if they have Bungie accounts.

        Must have a recent login session with said platform.
        Parameters:
            friend_platform: The platform friend type.
            page: The zero based page to return. Page size is 100.
        """
        query = None
        result = await self.get(
            path=f"/Social/PlatformFriends/{friend_platform}/{page}/", query=query
        )
        return forge(PlatformFriendClientResponse, result)
