"""
An extremely tiny pubsub module.
"""

# A dictionary containing lists of callbacks subscribed to a given event.
_subscribers = {}

def subscribe(event, callback):
	"""
	Subscribe the callback to the event.
	"""
	if event in _subscribers:
		_subscribers[event].append(callback)
	else:
		_subscribers[event] = [callback]

def unsubscribe(event, callback):
	"""
	Remove the subscription for the callback to the event.
	"""
	if event in _subscribers:
		_subscribers[event] = [x for x in _subscribers[event] if x != callback]

def publish(event, *args, **kwargs):
	"""
	Publish an event, passing positional and keyword arguments along to the callback.
	"""
	if event in _subscribers:
		for subscriber in _subscribers[event]:
			print("publishing " + event + " to subscriber")
			subscriber(*args, **kwargs)
