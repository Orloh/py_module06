# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 21:05:52 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 21:10:32 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import alchemy.grimoire


def main() -> None:
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    val1 = alchemy.grimoire.validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {val1}')

    val2 = alchemy.grimoire.validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {val2}')

    print("\nTesting spell recording with validation:")
    spell1 = alchemy.grimoire.record_spell("Fireball", "fire air")
    print(f'record_spell("Fireball", "fire air"): {spell1}')

    spell2 = alchemy.grimoire.record_spell("Dark Magic", "shadow")
    print(f'record_spell("Dark Magic", "shadow"): {spell2}')

    print("\nTesting late import technique:")
    spell3 = alchemy.grimoire.record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {spell3}')

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
