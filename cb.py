# -*- coding: utf-8 -*-
import os
import ansible.plugins.callback as callback

class CallbackModule(callback.CallbackBase):
    def __init__(self, display=None):
        super(CallbackModule, self).__init__(display)
        self.execution_id = os.environ.get("TASK_ID")
        self.playbook = None

    def v2_playbook_on_play_start(self, play):
        self.playbook = play
        return super(CallbackModule, self).v2_playbook_on_play_start(play)

    def v2_playbook_on_task_start(self, task, is_conditional):
        return super(CallbackModule, self).v2_playbook_on_task_start(
            task, is_conditional)

    def v2_runner_on_ok(self, result, **kwargs):
        print(result._host.get_name())
        print(result._task.get_name())
        return super(CallbackModule, self).v2_runner_on_ok(result, **kwargs)

    def v2_runner_on_failed(self, result, **kwargs):
        return super(CallbackModule, self).v2_runner_on_failed(
            result, **kwargs)

    def v2_runner_on_unreachable(self, result, **kwargs):
        return super(CallbackModule, self).v2_runner_on_unreachable(
            result, **kwargs)

    def v2_runner_on_skipped(self, result, **kwargs):
        return super(CallbackModule, self).v2_runner_on_skipped(
            result, **kwargs)
