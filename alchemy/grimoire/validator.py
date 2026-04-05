# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    validator.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 20:54:13 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 21:04:20 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def validate_ingredients(ingredients: str) -> str:
    """Checks if the ingredientes contain valid elements."""
    valid_elements = {"fire", "water", "earth", "air"}

    if any(element in ingredients for element in valid_elements):
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
