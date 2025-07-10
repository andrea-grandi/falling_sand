
const w = 10;
const width = 40;
const height = 40;
const cols = Math.floor(width/w);
const rows = Math.floor(height/w);


function make2DArray(cols: number, rows: number){
	let arr = new Array(cols);
	for (let i = 0; i < arr.length; i++){
		arr[i] = new Array(rows);
	}
	return arr;
}

let grid = make2DArray(cols, rows);

function drawGrid(){
	console.clear();
	
	let topBorder = '+';
	for (let i = 0; i < width; i++) {
	        topBorder += '-';
	}
	topBorder += '+';
	console.log(topBorder);
	
	for (let j = 0; j < rows; j++) {
	        let rowStr = '|';
	        for (let i = 0; i < cols; i++) {
	            rowStr += grid[i][j] ? '■' : ' ';
		}
	        rowStr += '|';
	        console.log(rowStr);
	}
	
	    // Create bottom border without repeat()
	let bottomBorder = '+';
	for (let i = 0; i < width; i++) {
	        bottomBorder += '-';
	}
	bottomBorder += '+';
	console.log(bottomBorder);
}

drawGrid();

