# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_transmutation_1.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 21:51:51 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 21:55:00 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from alchemy import transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {transmutation.lead_to_gold()}")


if __name__ == "__main__":
    main()
