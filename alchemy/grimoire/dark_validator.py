# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    dark_validator.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 22:58:21 by orhernan         #+#    #+#              #
#    Updated: 2026/04/08 00:27:54 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    is_valid = any(
        item.lower() in ingredients.lower() for item in allowed
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} {status}"
