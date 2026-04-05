# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_sacred_scroll.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 17:10:30 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 17:59:12 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import alchemy
import alchemy.elements


def main():
    print("=== Sacred Scroll Mastery ===")

    spells = [
        "create_fire",
        "create_water",
        "create_earth",
        "create_air"
    ]

    print("Testing direct module access:")
    for spell in spells:
        func = getattr(alchemy.elements, spell)
        print(f"alchemy.elements.{spell}(): {func()}")
    print()

    print("Testing package-level access (controlled by __init__.py):")
    for spell in spells:
        try:
            func = getattr(alchemy, spell)
            print(f"alchemy.{spell}(): {func()}")
        except AttributeError:
            print(f"alchemy.{spell}(): AttributeError - not exposed")
    print()

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
