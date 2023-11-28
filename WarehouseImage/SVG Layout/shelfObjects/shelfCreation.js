// Array Format ["nShelf", "nSpace", "wTotal", "hTotal", "wSupport", "wCenter", "hSpace", "hShelf"]
const shelfArray = fetch('shelfCoord.json'[shelfClass]);

nShelf = shelfArray[0];
nSpace = shelfArray[1];
wTotal = shelfArray[2];
hTotal = shelfArray[3];
wSupport = shelfArray[4];
wCenter = shelfArray[5];
hSpace = shelfArray[6];
hShelf = shelfArray[7];

const viewPort = (wTotal,hTotal);
var xStart = 0;
var yStart = 0;

// Side Supports
const hSupport = hTotal - 
createRectangle(xStart, hSpace, wSupport, hTotal - hSpace);
createRectangle(wSupport + wCenter, hSpace, wSupport, hTotal-hSpace);
// Top Space
yStart += createRectangle(xStart, yStart, wTotal, hSpace, nShelf);
xStart += wSupport;
// Top Shelf
yStart += createRectangle(wSupport, xStart, wCenter, hShelf);

// Only Applies to Pallet Racks which have nSpace = 3, nShelf = 2, group is always 1 and Shelf Class is Split (true)
if (nShelf !== nSpace) {
    // Space Above Shelf 1
    yStart += createRectangle(xStart,yStart,wCenter,hSpace,1,true);
    // Shelf 1
    yStart += createRectangle(xStart,yStart,wCenter,hShelf,1,true);
    // Space Below Shelf 1
    createRectangle(xStart,yStart,wCenter,hSpace,1,true);
}
else {
    for (i == 2; i <= arrShelf[1]; i ++) {
        var numOfGroup = nSpace + 1 - i;
        //Space
        yStart += createRectangle(xStart,yStart,wCenter,hSpace,numOfGroup);
        //Shelf
        yStart += createRectangle(xStart,yStart,wCenter,hShelf,numOfGroup);
    }    
}


function createRectangle(startX, startY, width, height, groupNum, splitShelf = false) {


    return height;
}

