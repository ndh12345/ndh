from pynput.keyboard import Listener, Key, KeyCode, Controller
store= set()
def he():
    print('hello')
HOT_KEYS= {
    he: set([Key.alt_l, KeyCode(char= '1')])
}
def ha(key):
    store.add(key)
def a(key):
    for action, trigger in HOT_KEYS.items():
        CHECK= all([True if triggerKey in store else False for triggerKey in trigger])
        if CHECK:
            action()
    if key in store:
        store.remove(key)
    if key==Key.esc:
        return False
with Listener(on_press= ha, on_release= a) as ls:
    ls.join()
