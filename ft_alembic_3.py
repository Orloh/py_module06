# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 00:01:42 by orhernan         #+#    #+#              #
#    Updated: 2026/04/07 00:02:16 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure"
    )
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
