# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 19:21:11 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 19:34:56 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_water, create_earth
from alchemy.potions import strength_potion


def main() -> None:
    print("=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print()

    print("Method 2- Specific function import:")
    print(f"create_water(): {create_water()}")
    print()

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()

    print("Method 4 - Multiple imports")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")
    print()

    print("All impport transmutation methods mastered!")


if __name__ == "__main__":
    main()
