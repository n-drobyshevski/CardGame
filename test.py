from src.Game import Game


def unique_player_hands(game: Game):
    existing_cards = []
    for player in game.players:
        for card in player.hand:
            if card not in existing_cards:
                existing_cards.append(card)
            else:
                return False
    return True
