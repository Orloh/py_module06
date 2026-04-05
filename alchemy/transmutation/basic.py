# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    basic.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 19:52:17 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 19:56:41 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return (
        f"Lead transmuted to gold using {create_fire()}"
    )


def stone_to_gem() -> str:
    return (
        f"Stone transmuted to gem using {create_earth()}"
    )
