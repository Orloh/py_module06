#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_alembic_5.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 00:06:19 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 00:08:04 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
