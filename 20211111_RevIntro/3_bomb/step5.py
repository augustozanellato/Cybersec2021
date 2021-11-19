target = "flyers"
s = "maduiersnfotvbyl"

sol = ""
int_to_ch = "pqrstuvwxyzklmno"
for idx, ch in enumerate(target):
    print(f"{ch=} {s.find(ch)=}")
    sol += int_to_ch[s.find(ch)]
print(sol)
