// Пример товаров
const products = [
    { id: 1, name: 'Smartphone', price: 500 },
    { id: 2, name: 'Headphones', price: 100 },
    { id: 3, name: 'Laptop', price: 1200 },
    { id: 4, name: 'Smart Watch', price: 200 },
    { id: 5, name: 'Bluetooth Speaker', price: 150 },
    { id: 6, name: 'Tablet', price: 350 }
];

// Массив для заказанных товаров
let order = [];

// Функция для отображения списка товаров
function displayProducts() {
    const productContainer = document.getElementById('products');
    productContainer.innerHTML = '';

    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.innerHTML = `${product.name} - $${product.price} 
            <button onclick="addToOrder(${product.id})">Add to Order</button>`;
        productContainer.appendChild(productDiv);
    });
}

// Функция для добавления товара в заказ
function addToOrder(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        order.push(product);
        updateOrderSummary();
    }
}

// Функция для обновления сводки по заказу
function updateOrderSummary() {
    const orderSummary = document.getElementById('order-summary');
    orderSummary.innerHTML = '';
    
    let total = 0;
    order.forEach(item => {
        orderSummary.innerHTML += `${item.name} - $${item.price}<br>`;
        total += item.price;
    });

    orderSummary.innerHTML += `<strong>Total: $${total}</strong>`;
}

// Функция для обработки платежа (мок-сервис)
function processPayment(paymentMethod) {
    if (order.length === 0) {
        alert("Please add some products to the order!");
        return;
    }

    // Мок-обработка платежа
    setTimeout(() => {
        const totalPrice = order.reduce((total, item) => total + item.price, 0);
        alert(`Payment of $${totalPrice} processed successfully with ${paymentMethod}.`);
        order = []; // Очистка заказа после успешного платежа
        updateOrderSummary(); // Обновление сводки заказа
    }, 1000); // Имитируем задержку при обработке платежа
}

// Инициализация страницы
displayProducts();
