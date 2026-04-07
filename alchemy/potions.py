# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    potions.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 20:42:41 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 20:50:30 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import elements

from .elements import create_earth, create_air


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with "
        f"'{elements.create_fire()}' and '{elements.create_water()}'"
    )
