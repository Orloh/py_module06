# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    advanced.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 19:57:06 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 20:01:38 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return (
        f"Philosopher's stone created using "
        f"{lead_to_gold()} and {healing_potion()}"
    )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
