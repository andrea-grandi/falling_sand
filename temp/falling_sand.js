var w = 10;
var width = 40;
var height = 40;
var cols = Math.floor(width / w);
var rows = Math.floor(height / w);
function make2DArray(cols, rows) {
    var arr = new Array(cols);
    for (var i = 0; i < arr.length; i++) {
        arr[i] = new Array(rows);
    }
    return arr;
}
var grid = make2DArray(cols, rows);
function drawGrid() {
    console.clear();
    var topBorder = '+';
    for (var i = 0; i < width; i++) {
        topBorder += '-';
    }
    topBorder += '+';
    console.log(topBorder);
    for (var j = 0; j < rows; j++) {
        var rowStr = '|';
        for (var i = 0; i < cols; i++) {
            rowStr += grid[i][j] ? '■' : ' ';
        }
        rowStr += '|';
        console.log(rowStr);
    }
    // Create bottom border without repeat()
    var bottomBorder = '+';
    for (var i = 0; i < width; i++) {
        bottomBorder += '-';
    }
    bottomBorder += '+';
    console.log(bottomBorder);
}
drawGrid();
