number_of_test_cases = int(input())

output = []
for _ in range(number_of_test_cases):
    number_of_videos,time = list(map(int,input().split()))
    list_of_video_times = list(map(int,input().split()))
    entertainment_values = list(map(int,input().split()))
    temp_output = dict()
    for i,v in enumerate(list_of_video_times):
        if v + i <= time:
            temp_output[entertainment_values[i]] = i+1
    if len(temp_output):
        output.append(temp_output[max(temp_output)])
    else:
        output.append(-1)
for _ in range(number_of_test_cases):
    print(output[_])