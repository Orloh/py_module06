# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    dark_spellbook.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 22:55:34 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 22:57:59 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
