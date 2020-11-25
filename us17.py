from project03 import indi_list,fam_list,calculateAge

def us17(indi,fam):
    parents=dict()
    for f in fam:
        for child in f[5]:
            parents[child]=(f[1],f[2])
    
    for f in fam:
        if parents.__contains__(f[2])== True and f[1] in parents[f[2]]:
           print("Error US17 {f[0]}: husand {f[1]} is married to child {f[2]}") 
           print("US17 complete")
           return False
        elif parents.__contains__(f[1])== True and f[2] in parents[f[1]]:
            print("ERROR us17 {f[0]}: wife {f[2]} is mariied to child {f[1]}")
            print("US17 complete")
            return False
    return True

def main()->None:
    us17(indi_list,fam_list)

if __name__ == "__main__":
    main()