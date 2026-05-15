#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_transmutation_2.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 21:58:14 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 22:08:34 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import alchemy


def main() -> str:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    return f"{alchemy.transmutation.lead_to_gold()}"


if __name__ == "__main__":
    main()
