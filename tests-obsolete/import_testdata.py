"""
Import simple test data for testing getting itemrec
"""
import predictionio

APP_KEY = "gDx1XuMUC9vu1YWWPRZkLRTftoq7m73mlj2MtnZEjncPlZ1JxUS2s7oajwP9xrZQ"
API_URL = "http://localhost:7070"

MIN_VERSION = '0.5.0'
if predictionio.__version__ < MIN_VERSION:
    err = "Require PredictionIO Python SDK version >= %s" % MIN_VERSION
    raise Exception(err)

if __name__ == "__main__":
    client = predictionio.Client(APP_KEY, 1, API_URL)

    client.create_user("u0")
    client.create_user("u1")
    client.create_user("u2")
    client.create_user("u3")

    client.create_item("i0", ("t1",), {"custom1": "i0c1"})
    client.create_item("i1", ("t1", "t2"), {"custom1": "i1c1", "custom2": "i1c2"})
    client.create_item("i2", ("t1", "t2"), {"custom2": "i2c2"})
    client.create_item("i3", ("t1",))

    client.identify("u0")
    client.record_action_on_item("rate", "i0", {"pio_rate": 2})
    client.record_action_on_item("rate", "i1", {"pio_rate": 3})
    client.record_action_on_item("rate", "i2", {"pio_rate": 4})

    client.identify("u1")
    client.record_action_on_item("rate", "i2", {"pio_rate": 4})
    client.record_action_on_item("rate", "i3", {"pio_rate": 1})

    client.identify("u2")
    client.record_action_on_item("rate", "i1", {"pio_rate": 2})
    client.record_action_on_item("rate", "i2", {"pio_rate": 1})
    client.record_action_on_item("rate", "i3", {"pio_rate": 3})

    client.identify("u3")
    client.record_action_on_item("rate", "i0", {"pio_rate": 5})
    client.record_action_on_item("rate", "i1", {"pio_rate": 3})
    client.record_action_on_item("rate", "i3", {"pio_rate": 2})

    client.close()
