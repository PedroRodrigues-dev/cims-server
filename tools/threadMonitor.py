from time import sleep


threads = {"threads": {}, "threadsName": {}}


def threadsMonitor():
    while True:
        threads_to_remove = []

        for thread_id, thread in threads["threads"].items():
            if not thread.is_alive():
                threads_to_remove.append(thread_id)

        for thread_id in threads_to_remove:
            threads["threads"].pop(thread_id)
            threads["threadsName"].pop(thread_id)

        sleep(1)
