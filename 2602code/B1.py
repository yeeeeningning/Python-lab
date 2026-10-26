def clean(lines: list[str]) -> list[list]:
    col_result = []
    for line in lines:
        parts = line.split()
        if len(parts) != 5:
            continue
        col_result.append(parts)  #除掉列数不等于五的行
    
    
    result = []
    seen_ids =[]
    for lin in col_result:
        a = lin
        stu_id = a[0]
        name = a[1]
        score_result = []
        is_valid_line =True
        for scores in a[2:]:
            if  scores == "-":
                scores = "0"
            if not scores.isdigit():
                is_valid_line = False
                break 
            b = int(scores)
            if b > 100 or b < 0:
                is_valid_line = False
                break
            score_result.append(b)
        if not is_valid_line:
            continue      #去除不合法成绩
        if stu_id in seen_ids :
            continue
        seen_ids.append(stu_id)
        rec = [stu_id , name, score_result]
        result.append(rec)
    return result


            

            

        
        
        
        


