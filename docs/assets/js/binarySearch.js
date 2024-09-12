const numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const binarySearchKey = 7;

// Populate the list of numbers on the page
function populateList() {
    const container = document.getElementById('number-list');
    if (container) {
        numberList.forEach(number => {
            const div = document.createElement('div');
            div.className = 'binary-item';
            div.textContent = number;
            container.appendChild(div);
        });
    }
}

// Perform the binary search and animate the process
async function startBinarySearch() {
    const items = document.querySelectorAll('#number-list .binary-item');
    let low = 0;
    let high = numberList.length - 1;
    let found = false;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);

        // Highlight the middle element
        items[mid].classList.add('highlight');
        await new Promise(resolve => setTimeout(resolve, 1000)); // Pause for 1 second

        if (numberList[mid] === binarySearchKey) {
            items[mid].classList.remove('highlight');
            items[mid].classList.add('found');
            found = true;
            break;
        } else if (numberList[mid] < binarySearchKey) {
            // Narrow down the range by ignoring the left half
            items[mid].classList.add('searched');
            low = mid + 1;
        } else {
            // Narrow down the range by ignoring the right half
            items[mid].classList.add('searched');
            high = mid - 1;
        }

        await new Promise(resolve => setTimeout(resolve, 500)); // Pause for half a second to reset highlight
        items[mid].classList.remove('highlight');
    }

    // If the number is not found (this won't happen in this case since 7 is in the list)
    if (!found) {
        items.forEach(item => item.classList.add('not-found'));
    }
}

// Initialize the number list
if (document.getElementById('number-list')) {
    populateList();
}