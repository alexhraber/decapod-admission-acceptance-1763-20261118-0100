def write(value, audit):
    audit.append(value)
    return value
if __name__ == '__main__':
    assert write('privileged', []) == 'privileged'
    print('agent-positive-tests-passed')
