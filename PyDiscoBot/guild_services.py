#!/usr/bin/env python
""" guild services
# Author: irox_rl
# Purpose: provide common services to guild attributes (server stuff)
# Version 1.0.5
#
#       v1.0.5 - include BotNotLoaded err for predicate checks on commands
"""

# local imports #

# non-local imports
import discord


def get_member_by_id(guild: discord.Guild, member_id: str) -> discord.Member | None:
    return next((x for x in guild.members if x.id.__str__() == member_id), None)


def get_members_by_role(guild: discord.Guild, role: discord.Role):
    return [member for member in guild.members if role in member.roles]


def get_role_by_name(guild: discord.Guild, name: str) -> discord.Role | None:
    if not name:
        return None
    return next((x for x in guild.roles if x.name.__str__() == name), None)