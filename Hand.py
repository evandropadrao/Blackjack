import main


class Hand:

    def __init__(self):
        self.__cards = []
        self.__value = 0
        self.__ace = False

    def __str__(self):
        hands_comp = ""

        for card in self.__cards:
            card_name = card.__str__();
            hands_comp += " " + card_name

            return "The hands is {}".format(hands_comp)

    def card_add(self, card):
        self.__cards.append(card)

        if card.grab_rank() == 'A':
            self.__ace = True

        self.__value += main.card_val[card.grab_rank()]

    def calc_total_value(self):
        # Tratamento da carta AS que pode se 01 ou 11 (enquanto valor menor que 12 considero o valor 11)
        if self.__ace and (self.__value < 12):
            return self.__value + 10
        else:
            return self.__value

    # Quando o jogador tem uma AS na mao e menos de 12 pontos, o jogador pode considerar o AS valendo 01
    # ou 11 pontos. Quando a pontuacao é superior ou igaual a 12 deve sempre considerar como 01, pela questao logica
    # que se considerar como 11 a mao fica estourada.
    # Como a primeira carta do 'dealer' eh escondida, a pontuacao dela nao deve ser computada
    def calc_current_score(self, hidden):

        calc1 = calc2 = 0
        has_ace = False

        if hidden:
            starting_card = 1
        else:
            starting_card = 0

        for x in range(starting_card, len(self.__cards)):
            if self.__cards[x].grab_rank() == 'A':
                has_ace = True

            calc1 += main.card_val[self.__cards[x].grab_rank()]

        # Tratamento da carta AS que pode se 01 ou 11 (enquanto valor menor que 12 considero o valor 11)
        if has_ace and (calc1 < 12):
            calc2 += 10

        return calc1, calc2

    def draw(self, hidden, playing):
        if hidden and playing:
            starting_card = 1
        else:
            starting_card = 0

        for x in range(starting_card, len(self.__cards)):
            self.__cards[x].draw()
