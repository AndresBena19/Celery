from celery import current_app


class Monitor(object):
    app = current_app

    def __init__(self):
        self.state = self.app.events.State()
        self.app.control.enable_events()

    def announce_failed_tasks(self, event):
        self.state.event(event)
        # task name is sent only with -received event, and self.state
        # will keep track of this for us.
        task = self.state.tasks.get(event['uuid'])

        print('TASK FAILED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))

    def announce_received_tasks(self, event):
        self.state.event(event)
        # task name is sent only with -received event, and self.state
        # will keep track of this for us.
        task = self.state.tasks.get(event['uuid'])

        print('TASK RECEIVED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))


    def announce_sent_tasks(self, event):
        self.state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = self.state.tasks.get(event['uuid'])

        print('TASK SEND: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))


    def announce_started_tasks(self, event):
        self.state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = self.state.tasks.get(event['uuid'])

        print('TASK STARTED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))


    def announce_succeded_tasks(self, event):
        self.state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = self.state.tasks.get(event['uuid'])

        print('TASK SUCCEDED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))


    def announce_rejected_tasks(self, event):
        self.state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = self.state.tasks.get(event['uuid'])

        print('TASK REJECTED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))

    def announce_revoked_tasks(self, event):
        self.state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = self.state.tasks.get(event['uuid'])

        print('TASK REVOKED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))


    def announce_retried_tasks(self, event):
        self.state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = self.state.tasks.get(event['uuid'])

        print('TASK RETRIED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))


    def __call__(self, *args, **kwargs):
        with self.app.connection() as connection:
            recv = self.app.events.Receiver(connection,
                                            handlers={
                                                'task-failed': self.announce_failed_tasks,
                                                'task-received' : self.announce_received_tasks,
                                                'task-sent': self.announce_sent_tasks,
                                                'task-started': self.announce_started_tasks,
                                                'task-succeeded':self.announce_succeded_tasks,
                                                'task-rejected': self.announce_rejected_tasks,
                                                'task-revoked': self.announce_revoked_tasks,
                                                'task-retried': self.announce_retried_tasks,
                                            }
                                            )

            recv.capture(limit=None, timeout=None, wakeup=False)


if __name__ == '__main__':
    Monitor()()