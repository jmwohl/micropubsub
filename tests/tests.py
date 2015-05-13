import micropubsub as ps


def test_subscribe_and_publish():
	
	# define a callback, aka a handler
	def handleStartupEvent():
		assert True

	# subscribe the callback to the startup event
	ps.subscribe('startup', handleStartupEvent)

	# when the startup event is published, the callback will be executed
	ps.publish('startup')


def test_subscribe_and_unsubscribe():
	should_be_called = 1
	called = 0

	# define a callback, aka a handler
	def handleEvent():
		nonlocal called
		called += 1

	# subscribe the callback to the event
	ps.subscribe('some:event', handleEvent)

	# when the some:event event is published, the callback will be executed
	ps.publish('some:event')

	# unsubscribe the callback to the some:event event
	ps.unsubscribe('some:event', handleEvent)

	# when the some:event event is published, the callback will NOT be executed again
	ps.publish('some:event')

	assert should_be_called == called


def test_multiple_subscriptions():
	should_be_called = 2
	called = 0

	# define a callback, aka a handler
	def handleEvent():
		nonlocal called
		called += 1

	# subscribe the callback to the event TWICE
	ps.subscribe('some:event', handleEvent)
	ps.subscribe('some:event', handleEvent)

	# when the some:event event is published, the callback will be executed
	ps.publish('some:event')

	assert should_be_called == called


def test_multiple_subscriptions_and_unsubscribe():
	should_be_called = 0
	called = 0

	# define a callback, aka a handler
	def handleEvent():
		nonlocal called
		called += 1

	# subscribe the callback to the event TWICE
	ps.subscribe('some:event', handleEvent)
	ps.subscribe('some:event', handleEvent)

	# should remove all subscriptions to some:event for handleEvent
	ps.unsubscribe('some:event', handleEvent)

	# when the some:event event is published, the callback will NOT be executed, since it's already unsubscribed
	ps.publish('some:event')

	assert should_be_called == called


def test_positional_args():
	expected_total = 5
	total = 0

	# define a callback, aka a handler
	def handleEvent(num_one, num_two):
		nonlocal total
		total = num_one + num_two

	# subscribe the callback to the event TWICE
	ps.subscribe('add_numbers', handleEvent)

	# when the add_numbers event is published, the callback will be executed
	ps.publish('add_numbers', 2, 3)

	assert expected_total == total


def test_keyword_args():
	expected_name = 'Jonny'
	actual_name = ''

	# define a callback, aka a handler
	def handleEvent(name=None):
		nonlocal actual_name
		actual_name = name

	# subscribe the callback to the event TWICE
	ps.subscribe('name', handleEvent)

	# when the add_numbers event is published, the callback will be executed
	ps.publish('name', name='Jonny')

	assert expected_name == actual_name