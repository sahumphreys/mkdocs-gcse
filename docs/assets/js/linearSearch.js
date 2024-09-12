const shoppingList = ["Milk", "Eggs", "Tomatoes", "Mince", "Flour"];
const searchKey = "Mince";

// Populate the shopping list items on the page
function populateList() {
    const container = document.getElementById('shopping-list');
    if (container) {

        shoppingList.forEach(item => {
            const div = document.createElement('div');
            div.className = 'linear-item';
            div.textContent = item;
            container.appendChild(div);
        });
    }
}

// Perform the linear search and animate the process
async function startLinearSearch() {
    const items = document.querySelectorAll('#shopping-list .linear-item');
    let found = false;

    for (let i = 0; i < items.length; i++) {
        items[i].classList.add('highlight');
        await new Promise(resolve => setTimeout(resolve, 1000)); // Pause for 1 second

        if (items[i].textContent === searchKey) {
            items[i].classList.add('found');
            found = true;
            break;
        } else {
            items[i].classList.remove('highlight');
        }
    }

    if (!found) {
        items[items.length - 1].classList.add('not-found');
    }
}

// Initialize the shopping list
if (document.getElementById('shopping-list')) {
    populateList();
}