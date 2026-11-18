ns = {}
exec(compile(open('src/privileged_write.py').read(), 'src/privileged_write.py', 'exec'), ns)
audit = []
assert ns['write']('privileged', audit) == 'privileged'
assert audit == ['privileged'], 'R3-AUDIT: every privileged write needs an audit event'
print('accepted-audit-negative-passed')
