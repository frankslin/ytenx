import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_sha_file = os.path.join(BASE_DIR, 'ytenx', 'commit_sha.txt')

try:
    with open(_sha_file) as f:
        _COMMIT_SHA = f.read().strip()
except OSError:
    _COMMIT_SHA = None


def commit_sha(request):
    return {'COMMIT_SHA': _COMMIT_SHA}
