participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
participant.sort()
completion.sort()
for p,c in zip(participant, completion):
    print(p,c)
    if p != c:
        print(p)
print(participant.pop())