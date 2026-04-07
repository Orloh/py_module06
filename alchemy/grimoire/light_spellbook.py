# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    light_spellbook.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 22:13:45 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 22:20:52 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(
        ingredients,
        light_spell_allowed_ingredients
    )
    return f"Spell recorded: {spell_name} ({validation})"
