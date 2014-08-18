# API of Board RDF022

## Usage

Download this repository and put directory `rdf022` along with `your_prog.py`.

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
