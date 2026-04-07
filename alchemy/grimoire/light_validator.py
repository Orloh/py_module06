# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    light_validator.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 22:21:10 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 22:38:42 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import typing


def validate_ingredients(
        ingredients: str,
        get_allowed_ingredients: typing.Callable[[], list[str]]
) -> str:
    allowed = get_allowed_ingredients()
    is_valid = any(
        item.lower() in ingredients.lower() for item in allowed
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
