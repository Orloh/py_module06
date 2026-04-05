# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    potions.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 18:15:59 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 19:18:04 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from alchemy.elements import (
    create_fire,
    create_water,
    create_earth,
    create_air
)


def healing_potion() -> str:
    return (
        f"Healing potion brewed with {create_fire()} "
        f"and {create_water()}"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with {create_earth()} "
        f"and {create_fire()}"
    )


def invisibility_potion() -> str:
    return (
        f"Invisibility potion brewed with {create_air()} "
        f"and {create_water()}"
    )


def wisdom_potion() -> str:
    return (
        f"Wisdom potion brewed with all elements: "
        f"{create_fire()}, {create_water()}, "
        f"{create_earth()}, {create_air()}"
    )
