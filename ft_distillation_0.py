# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_distillation_0.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 20:53:31 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 20:56:07 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    main()
