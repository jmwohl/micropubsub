# MicroPubSub

An extremely tiny pubsub module.

## Usage

### Basic Example
```python
import micropubsub as pubsub

# define a callback, aka a handler
def handleStartupEvent():
	print('startup event handled!')

# subscribe the callback to the startup event
pubsub.subscribe('startup', handleStartupEvent)

# when the startup event is published, the callback will be executed
pubsub.publish('startup')

# prints 'startup event handled!'

```

### Example w/ Positional Args
Positional *args supplied to the publish function are passed along to the callbacks

```python
import micropubsub as pubsub

# define a callback, aka a handler
def handleLoginEvent(username, time):
	print(username + ' logged in at ' + time + '.')

# subscribe the callback to the login event
pubsub.subscribe('login', handleLoginEvent)

# when the login event is published, the callback will be called with the supplied *args
pubsub.publish('login', 'richard', '12:45 PM')

# prints 'richard logged in at 12:45 PM.'

```

### Example w/ Keyword Args
Likewise, **kwargs supplied to the publish function are passed along to the callbacks

```python
import micropubsub as pubsub

# define a callback, aka a handler
def handleLoginEvent(username=None):
	print(username + ' logged in.')

# subscribe the callback to the login event
pubsub.subscribe('login', handleLoginEvent)

# when the login event is published, the callback will be called with the supplied **kwargs
pubsub.publish('login', username='richard')

# prints 'richard logged in.'

```

### Example w/ Multiple Subscribers
There is no limit to the number of subscribers that can subscribe to events, within reason.

```python
import micropubsub as pubsub

# define a callback, aka a handler
def handleLoginEvent(username=None):
	print(username + ' logged in.')

# another callback elsewhere in the application
def anotherLoginEventHandler(username=None):
	print(username + ' logged in.')

# subscribe the callbacks to the login event
pubsub.subscribe('login', handleLoginEvent)
pubsub.subscribe('login', anotherLoginEventHandler)

# when the login event is published, both callback will be called with the supplied **kwargs
pubsub.publish('login', username='richard')

# prints 'richard logged in.'

```

### Unsubscribe
You can unsubscribe a subscriber from events whenever you damn well please.

```python
import micropubsub as pubsub

# define a callback, aka a handler
def handleLoginEvent(username=None):
	print(username + ' logged in.')

# subscribe the callbacks to the login event
pubsub.subscribe('login', handleLoginEvent)

# we publish the login event
pubsub.publish('login', username='richard')
# prints 'richard logged in.'

# now we can unsubscribe this handler...
pubsub.unsubscribe('login', handleLoginEvent) 

# and if we publish again
pubsub.publish('login', username='richard')
# we get nothing, since there are no longer any handlers subscribed to the event

```


## Tests
If you want to run the nose tests, first install the testing deps:
```
$ pip install -r requirements-testing.txt
```

Then run 'em:
```
$ nosetests --with-coverage
```