subjects = {}
with open('fail_6.txt', 'r', encoding='utf-8') as my_subj:
    line = my_subj.readlines()
    for i in line:
        sub, lab, pr, lec = i.split()
        subjects[sub] = int(lab) + int(pr) + int(lec)
    print(subjects)
