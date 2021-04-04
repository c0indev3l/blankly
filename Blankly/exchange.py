"""
    Inherited exchange object.
    Copyright (C) 2021  Emerson Dove

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import Blankly
from Blankly.IExchange import IExchange


class Exchange(IExchange):
    def __init__(self, exchange_type, exchange_name):
        self.__name = exchange_name
        self.__type = exchange_type
        self.preferences = Blankly.utils.load_user_preferences()

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_preferences(self):
        return self.preferences

    def start_models(self, coin=None):
        """
        Start all models or a specific one after appending it to to the exchange
        """
        if coin is not None:
            # Run a specific model with the args
            if not self.models[coin]["model"].is_running():
                self.models[coin]["model"].run(self.models[coin]["args"])
            return "Started model attached to: " + coin
        else:
            for coin_iterator in self.models:
                # Start all models
                if not self.models[coin_iterator]["model"].is_running():
                    self.models[coin_iterator]["model"].run(self.models[coin_iterator]["args"])
                else:
                    print("Ignoring the model on " + coin_iterator)
            return "Started all models"

    def get_model(self, coin):
        return self.models[coin]["model"]

    def get_model_state(self, currency):
        """
        Returns JUST the model state, as opposed to all the data returned by get_currency_state()

        Args:
            currency: Currency that the selected model is running on.
        """
        return (self.get_model(currency)).get_state()

    def get_full_state(self, currency):
        """
        Makes API calls to determine the state of the currency. This also returns the state of the model on that currency.

        Args:
            currency: Currency to filter for. This filters model information and the exchange information.
        """
        state = self.get_portfolio_state(currency)

        return {
            "account": state,
            "model": self.get_model_state(currency)
        }
