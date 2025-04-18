import sys
import io
from contextlib import contextmanager

class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

    def __enter__(self):
        if self.stdout is not None:
            sys.stdout = self.stdout
        if self.stderr is not None:
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        return False  

if __name__ == '__main__':
    print('Hello stdout')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        try:
            raise Exception('Hello stderr.txt')
        except Exception:
            import traceback
            traceback.print_exc()

    print('Hello stdout again')
    try:
        raise Exception('Hello stderr')
    except Exception:
        import traceback
        traceback.print_exc()

    stdout_file.close()
    stderr_file.close()
