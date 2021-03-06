# API of Board RDF022

## Usage

Download this repository and put `rdf022.py` along with `your_prog.py`, just like `sample.py`.

### LCM

To show messages on the LCM, simply assign them to `lcm.messages` before `lcm.refresh()`.

```py
import rdf022


msgs = ('Hello', 'World')

lcm = rdf022.get_lcm()
lcm.messages = msgs
lcm.refresh()
```

Output:

```text
Hello
World
```

**N.B.**

* `get_lcm().messages` should be an iterable object and contains only 2 items.

* `get_lcm()` returns an instance of Singleton, so `lcm_1` and `lcm_2` in the following block are the same:

```py
lcm_1 = rdf022.get_lcm()
lcm_2 = rdf022.get_lcm()
```

* The library is multiple-access safed, in case you have a multithreaded process.

### Brightness control

To show messages on the LCM, simply assign them to `lcm.messages` before `lcm.refresh()`.

```py
import rdf022
import time

lcm = rdf022.get_lcm()

def sparkle():
    while True:
        for i in range(lcm.brightness_depth):
            lcm.decrease_brightness()
            time.sleep(0.1)
        for i in range(lcm.brightness_depth):
            lcm.increase_brightness()
            time.sleep(0.1)

import threading
threading.Thread(target=sparkle).start()
```

**N.B.**

* `decrease_brightness()` should be decrease brightness slowly.

* `increase_brightness` should be increase brightness slowly.

* The library is multiple-access safed, in case you have a multithreaded process.

