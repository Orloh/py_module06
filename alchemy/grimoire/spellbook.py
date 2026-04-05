# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    spellbook.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 21:00:20 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 21:05:24 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

# Method 2: dependency injection being used
def record_spell(spell_name: str, ingredients: str, validator_func) -> str:
    """
    Records a spell, using dependency injection to avoid a circular dependency.
    """
    validation_result = validator_func(ingredients)

    if "VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"

    return f"Spell rejected: {spell_name} ({validation_result})"
