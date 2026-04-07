# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_transmutation_0.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 21:50:29 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 21:51:04 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()
