from collections import defaultdict
tasks = defaultdict(list)
#listに追加
def todo(task):
    tasks['False'].append(task)
    return(tasks)

#listを表示
def list():
    return tasks['False']

#donelistの作成
def done(task):
    tasks['True'].append(task)
    tasks['False'].remove(task)

#donelistを表示
def donelist():
    return tasks['True']

#delsの作成(タスクの削除)
def dels(task):
    if task in tasks['True']:
        tasks['True'].remove(task)
    elif task in tasks['False']:
        tasks['False'].remove(task)

