# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/05 20:04:04 by orhernan         #+#    #+#              #
#    Updated: 2026/04/05 20:28:01 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import alchemy.transmutation.basic as basic
import alchemy.transmutation.advanced as advanced
import alchemy.transmutation


def main() -> None:
    print("=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py)")
    print(f"lead_to_gold(): {basic.lead_to_gold()}")
    print(f"stone_to_gem(): {basic.stone_to_gem()}")
    print()

    print("Testing Relative Imports (from advanced.py)")
    print(f"philosopers_stone(): {advanced.philosophers_stone()}")
    print(f"elixir_of_life(): {advanced.elixir_of_life()}")
    print()

    print("Testing Package Access:")
    print(
        f"alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}"
    )
    print(
        f"alchemy.transmutation.philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}"
    )
    print()

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
