# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    recipes.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 21:21:27 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 21:44:15 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ..potions import strength_potion
from ..elements import create_air
import elements


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
        f"'{strength_potion()}' mixed with '{elements.create_fire()}'"
    )
