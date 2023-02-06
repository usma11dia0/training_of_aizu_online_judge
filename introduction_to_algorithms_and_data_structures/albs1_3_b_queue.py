from collections import deque

# 入力データの取得
n, q = map(int, input().split())
process_list = [list(map(str, input().split())) for _ in range(0, n)]

# 初期値設定
process_queue = deque(process_list)
complete_queue = deque()
passed_time = 0

while len(process_queue) > 0:
    # iteration中の要素追加・削除対策
    # process_queueの内容に沿ってprocess_listを更新
    process_list = list(process_queue)
    for process_name, process_time in process_list:
        process_time = int(process_time)
        remaining_time = process_time - q
        if remaining_time <= 0:
            passed_time += process_time
            complete = process_queue.popleft()
            complete[1] = passed_time
            complete_queue.append(complete)
        else:
            passed_time += q
            not_complete = process_queue.popleft()
            not_complete[1] = remaining_time
            process_queue.append(not_complete)

# 結果の出力
for queue in complete_queue:
    print(*queue)
