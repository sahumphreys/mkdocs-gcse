// Get references to the two canvas elements
let bubbleCanvas = document.getElementById("bubbleCanvas");
let insertionCanvas = document.getElementById("insertionCanvas");
const canvas3 = document.getElementById("mycanvas3");

const bubbleSortButton = document.getElementById("btnBubbleSort");
bubbleSortButton.removeEventListener('click', startBubbleSort);
bubbleSortButton.addEventListener('click', startBubbleSort);

const insertionSortButton = document.getElementById("btnInsertionSort");
insertionSortButton.removeEventListener('click', startInsertionSort);
insertionSortButton.addEventListener('click', startInsertionSort);

let bubbleCtx;
let insertionCtx;

let arrayLength = 12; // Length of the array
let max = 100; // Maximum value for the array elements
let swapColour = 'red'; // Highlighting color for swaps
let sortedColour = 'green'; // Color for sorted elements
let firstColour = 'blue'; // Default color for unsorted elements


document.addEventListener("DOMContentLoaded", () => {
    //initializeAlgorithms();
    bubbleCanvas = document.getElementById("bubbleCanvas");
    insertionCanvas = document.getElementById("insertionCanvas");
    // canvas3 = document.getElementById("mycanvas3");
  
    bubbleCtx = bubbleCanvas.getContext("2d");
    insertionCtx = insertionCanvas.getContext("2d");
    // Initialize other canvas contexts as well

    generateAndDrawInitialArray();
  });


// Generate a random array
function generateRandomArray(length) {
    return Array.from({ length }, () => Math.floor(Math.random() * max) + 1);
}

// Generate and draw the random array
function generateAndDrawInitialArray() {
    console.log("Creating and drawing the initial bubble sort array")
    bubbleUnsortedArray = generateRandomArray(arrayLength);
    console.log(bubbleUnsortedArray)
    drawBars(bubbleCtx, bubbleUnsortedArray);

    console.log("Creating and drawing the initial bubble sort array")
    insertionUnsortedArray = generateRandomArray(arrayLength);
    console.log(insertionUnsortedArray)
    drawBars(insertionCtx, insertionUnsortedArray);
  }

// Drawing logic (common to both sorts)
function drawBars(ctx, array, highlightIndices = [], sortedIndices = []) {
    // Ensure that the context exists before drawing
    if (!ctx) {
        console.error("Canvas context is not defined!");
        return;
    }
    
    const barWidth = 40;
    const barSpacing = 10;
    
    array.forEach((value, index) => {
        const x = index * (barWidth + barSpacing);
        const height = value * 2.8;

        // Change color based on highlighting and sorted state
        if (highlightIndices.includes(index)) {
            ctx.fillStyle = swapColour; // Highlighting color
        } else if (sortedIndices.includes(index)) {
            ctx.fillStyle = sortedColour; // Sorted color
        } else {
            ctx.fillStyle = firstColour; // Default color
        }
        
        // Draw the bar
        ctx.fillRect(x + 3, 300 - height, barWidth, height);
        
        // Display the value as text above the bar
        ctx.fillStyle = 'black';
        ctx.font = '12px Arial';
        ctx.fillText(value, x + barWidth / 2 - 5, 300 - height - 5);
    });
}

// Bubble Sort Algorithm
async function bubbleSort(array) {
    const timeout = 50
    console.log("Bubble sort has started with list: " + array);
    for (let i = 0; i < array.length - 1; i++) {
        for (let j = 0; j < array.length - i - 1; j++) {
            // Highlight the pair of bars being compared
            drawBars(bubbleCtx, array, [j, j + 1]);
            await new Promise(resolve => setTimeout(resolve, timeout));
            
            if (array[j] > array[j + 1]) {
                await swapBars(array, j, j + 1);
                bubbleCtx.clearRect(0, 0, bubbleCanvas.width, bubbleCanvas.height); // Clear the canvas
                drawBars(bubbleCtx, array, [j, j + 1]); // Highlight the swapped bars
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
        }
        
        // Mark the last element as sorted
        bubbleSortedIndices.push(array.length - i - 1);
        drawBars(bubbleCtx, array, [], bubbleSortedIndices);
        await new Promise(resolve => setTimeout(resolve, timeout));
    }

    // Mark the first element as sorted (entire array is sorted)
    bubbleSortedIndices.push(0);
    drawBars(bubbleCtx, array, [], bubbleSortedIndices);
}

// Insertion Sort Algorithm
async function insertionSort(array) {
    for (let i = 1; i < array.length; i++) {
        let current = array[i];
        let j = i - 1;

        // Highlight the current element
        drawBars(insertionCtx, array, [i]);
        await new Promise(resolve => setTimeout(resolve, 1000));

        while (j >= 0 && array[j] > current) {
            array[j + 1] = array[j]; // Shift elements
            j--;
            insertionCtx.clearRect(0, 0, insertionCanvas.width, insertionCanvas.height); // Clear the canvas
            drawBars(insertionCtx, array, [j + 1]); // Highlight the shift
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
        
        array[j + 1] = current; // Insert the current element in its place
        insertionSortedIndices.push(i); // Mark it as sorted
        insertionCtx.clearRect(0, 0, insertionCanvas.width, insertionCanvas.height); // Clear the canvas
        drawBars(insertionCtx, array, [], insertionSortedIndices); // Redraw bars with updated sorted state
    }
}

// Swap Bars Utility
async function swapBars(array, index1, index2) {
    const temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
}

// Start Bubble Sort
function startBubbleSort() {
    bubbleSortedIndices = []; // Clear sorted indices
    bubbleSort([...bubbleUnsortedArray]).then(() => {
      console.log('Bubble Sort Completed');
    });
}

function startInsertionSort() {
    insertionSortedIndices = []
    insertionSort([...insertionUnsortedArray]).then(() => {
        console.log("Insertion sort completed")
    });
}

function initializeAlgorithms() {
    bubbleCanvas = document.getElementById("bubbleCanvas");
    insertionCanvas = document.getElementById("insertionCanvas");
    // canvas3 = document.getElementById("mycanvas3");
  
    bubbleCtx = bubbleCanvas.getContext("2d");
    insertionCtx = insertionCanvas.getContext("2d")
    // Initialize other canvas contexts as well
}

