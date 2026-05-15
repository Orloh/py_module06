#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_distillation_1.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 20:56:31 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 20:59:42 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
