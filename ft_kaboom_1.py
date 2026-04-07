# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_kaboom_1.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 00:29:17 by orhernan         #+#    #+#              #
#    Updated: 2026/04/08 00:32:44 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now... THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Curse", "bats and frogs"))


if __name__ == "__main__":
    main()
