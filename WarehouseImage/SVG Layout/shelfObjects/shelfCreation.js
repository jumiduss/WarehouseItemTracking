const newRect = document.createElementNS("http://www.w3.org/2000/svg", "rect");

class Shelf {

    constructor(vaShelf) {
        this.qSh = vaShelf[0];
        this.qSp = vaShelf[1];
        this.wT  = vaShelf[2];
        this.wSh = vaShelf[3];
        this.wSu = vaShelf[4];
        this.hU  = vaShelf[5];
        this.hSh = vaShelf[6];
        this.hB  = vaShelf[7];
        this.hSp = vaShelf[8];
        this.hT  = vaShelf[9];
    }
    // build() {
    //     gsap.set(newRect, {
    //         class:shelf,
    //         x: this.wSu,
    //         y: (this.hSp * (i + 1)) + (i * this.hSh),

    //     });
    // }
}

class StructuretoMake {
    build() {
        
        open()







    }
}


const pShelf = {

       //   qSh, qSp,  wT, wSh, wSu,  hU, hSh,  hB,    hSp,     hT 
    "r4"  :[  2,   3,  54,   3,  48,  84,   4,   0,     38,    122], //Rack 4'
    "r8"  :[  2,   3, 102,   3,  96,  84,   4,   0,     38,    122], //Rack 8'
    "s464":[  4,   4,   2,  44,  48,  72,   2, 2.5,   22.5,  100.5], //Shelf 4x6x4
    "s465":[  5,   5,   2,  44,  48,  72,   2,   2,     17,     97], //Shelf 4x6x5
    "s474":[  4,   4,   3,  42,  48,  84,   3,   0,     27,    120], //Shelf 4x7x4
    "s475":[  5,   5,   3,  42,  48,  84,   3,   0, 200.25, 116.25], //Shelf 4x7x5
    "s564":[  4,   4,   2,  56,  60,  72,   2, 2.5,   22.5,  100.5], //Shelf 5x6x4
    "s565":[  5,   5,   2,  56,  60,  72,   2,   2,     17,     97], //Shelf 5x6x5
    "s574":[  4,   4,   3,  54,  60,  84,   3,   0,     27,    120], //Shelf 5x7x4
    "s575":[  5,   5,   3,  54,  60,  84,   3,   0,  20.25, 116.25]  //Shelf 5x7x5

};

