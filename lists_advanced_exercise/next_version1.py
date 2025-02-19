def next_version(data):
    newer_version = int(''.join(data)) + 1
    result = [str(i) for i in str(newer_version)]
    print('.'.join(result))


current_version = input().split('.')
next_version(current_version)