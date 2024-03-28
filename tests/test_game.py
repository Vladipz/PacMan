# import pytest
# from game import Game
#
# @pytest.fixture
# def game():
#     return Game()
#
# def test_score_update(game):
#     initial_score = game.score
#     game.score += 100  # Симулюємо збільшення рахунку
#     game.run()  # Запускаємо гру (спричинить оновлення екрану та перевірку рахунку)
#     assert game.score == initial_score + 100  # Перевіряємо, що рахунок оновився правильно
