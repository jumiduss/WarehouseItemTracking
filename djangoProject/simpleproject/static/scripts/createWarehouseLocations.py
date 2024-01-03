from stockmanager.models import Location

shelving_units = [
    #Format
    #[Number of Shelving Units, Default Number of Shelves, Shelving Unit Number that has non-Default Number of Shelves , The Alternative Number of Shelves]
    [9,5,    [0],0],[8,4,[8],5], # Isles 1 & 2
    [8,4,[5,6,7],5],[8,4,[0],0], # Isles 3 & 4
    [8,4,[1,2,3],5],[9,4,[0],0], # Isles 5 & 6
    [8,4,    [0],5],[9,5,[0],0], # Isles 7 & 8
    [8,5,  [7,8],0],[3,4,[3],5], # Isles 9 & 10
    [3,4,    [0],0],[2,4,[0],0], # Isles 11 & 12
    [2,4,    [0],0],[2,4,[0],0], # Isles 13 & 14
    [2,4,    [0],0],[1,5,[0],0], # Isles 15 & 16
    [2,4,    [0],0],[6,3,[0],0], # Isles 17 & 18
    [2,3,    [0],0],[1,1,[0],0]  # Isles 19 & [20-22, Same values for all 3]
]

def createShelf(fnum,mnum,lmax):
    for lnum in range(1,(lmax + 1)): 
        location = Location(f_num=str(fnum).zfill(2),m_num=str(mnum),l_num=str(lnum))
        location.save()
    return

for indexF, nM in enumerate(shelving_units):
    nF = indexF + 1
    if nF < 20:
        for i in range(1, (nM[0] + 1)):
            if i in nM[2]:
                if nF == 9:
                    createShelf(nF,i,4)
                    createShelf(nF,(i + 1),6)
                    break
                else:
                    createShelf(nF,i,nM[3])
            else:
                createShelf(nF,i,nM[1])
    else:
        createShelf(   nF   ,1,1)
        createShelf((nF + 1),1,1)
        createShelf((nF + 2),1,1)
