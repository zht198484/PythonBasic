import thread

import SingleThread

thread.start_new_thread(SingleThread.func1(), ())
thread.start_new_thread(SingleThread.func2(), ())
