#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_kaboom_0.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 22:41:40 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 22:51:01 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print(
        f"Testing record light spell: "
        f"{alchemy.grimoire.light_spell_record('Fantasy', 'Earth, air, FiRe')}"
    )
    pass


if __name__ == "__main__":
    main()
