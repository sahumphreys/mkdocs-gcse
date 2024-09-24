// bubble-sort.js

let canvas;
let ctx;
const firstColour = "#336699";
const swapColour = "#990000";
const sortedColour = "#009900";
const arrayLength = 12;
const max = 30;

const unsortedArray = generateRandomArray(arrayLength);

function generateRandomArray(length) {
    return Array.from({ length }, () => Math.floor(Math.random() * max) + 1);
}

const sortedIndices = [];

function drawBars(array, highlightIndices = []) {
    const barWidth = 40;
    const barSpacing = 10;
    
    array.forEach((value, index) => {
        const x = index * (barWidth + barSpacing);
        const height = value * 9;

        // Change color based on highlighting and sorted state
        if (highlightIndices.includes(index)) {
            ctx.fillStyle = swapColour; // Highlighting color
        } else if (sortedIndices.includes(index)) {
            ctx.fillStyle = sortedColour; // Sorted color
        } else {
            ctx.fillStyle = firstColour; // Default color
        }

        // Draw the bar
        ctx.fillRect(x+5, 300 - height, barWidth, height);

        // Display the value as text above the bar
        ctx.fillStyle = 'black';
        ctx.font = '12px Arial';
        ctx.fillText(value, x + barWidth / 2 - 5, 300 - height - 5);
    });
}

async function bubbleSort(array) {
    for (let i = 0; i < array.length - 1; i++) {
        for (let j = 0; j < array.length - i - 1; j++) {
            // Highlight the pair of bars being compared
            drawBars(array, [j, j + 1]);
            await new Promise(resolve => setTimeout(resolve, 1000));

            if (array[j] > array[j + 1]) {
                await swapBars(array, j, j + 1);
                ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
                drawBars(array, [j, j + 1]); // Highlight the swapped bars
                // Add a delay to visualize the swapping
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
        }

        // Mark the last element as sorted
        sortedIndices.push(array.length - i - 1);
        drawBars(array, [], [array.length - i - 1]);
        await new Promise(resolve => setTimeout(resolve, 1000));
    }

    // Mark the first element as sorted (entire array is sorted)
    sortedIndices.push(0);
    drawBars(array, []);
}

async function swapBars(array, index1, index2) {
    const temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
}

function startBubbleSort() {
    const sortedArray = [...unsortedArray]; // Create a copy for sorting
    bubbleSort(sortedArray).then(() => {
        console.log('Bubble Sort Completed');
    });
}

document.addEventListener('DOMContentLoaded', function () {
    canvas = document.getElementById('sortCanvas');
    ctx = canvas.getContext('2d');

    drawBars(unsortedArray);
});