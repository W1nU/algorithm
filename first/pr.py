def solution(tickets):
    answer = ["ICN"]
    
    tickets_dict = {}

    for ticket in tickets:
        if ticket[0] in tickets_dict.keys():
            tickets_dict[ticket[0]].append(ticket[1])
        else:
            tickets_dict[ticket[0]] = [ticket[1]]
    
    for key in tickets_dict:
        tickets_dict[key].sort(reverse=True)

    stack = tickets_dict["ICN"]

    times = 0

    while stack:
        current_location = stack.pop()

        answer.append(current_location)

        if current_location in tickets_dict.keys():
            next_locations = tickets_dict[current_location]
        
            if len(next_locations) > 0:
                next_location = next_locations.pop()
                stack.append(next_location)
        
        else:
            break
        
    return answer
 
solution([['ICN', 'BBB'], ['BBB', 'AAA'], ['AAA', 'BBB'], ['BBB', 'ICN'], ['ICN','AAA'], ['AAA', 'ICN']])