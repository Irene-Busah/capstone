document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/sales-by-category/') // Make sure to use the correct endpoint for your API
        .then(response => response.json())
        .then(data => {
            // Extract the labels and data for the chart from the API response
            const labels = data.map(item => item.product__category__name);
            const chartData = data.map(item => parseFloat(item.total_revenue));

            // Creating a new chart instance
            var salesCtx = document.getElementById('salesTrendsChart').getContext('2d');
            window.salesTrendsChart = new Chart(salesCtx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        data: chartData,
                        backgroundColor: '#00AF54',
                        borderWidth: 1,
                        barThickness: 50,
                        borderRadius: 8,
                        barPercentage: 0.9,
                        categoryPercentage: 1,
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                }
            });

        })
        .catch(error => {
            console.error('Error fetching sales data:', error);
        });
});




document.addEventListener('DOMContentLoaded', () => {
    const exportButton = document.querySelector('.export-button');
    const exportDropdown = document.querySelector('.export-dropdown');
    const overlay = document.querySelector('.overlay');

    exportButton.addEventListener('click', (event) => {
        event.stopPropagation();
        exportDropdown.classList.toggle('show');
        overlay.classList.toggle('show');
    });

    exportDropdown.addEventListener('click', (event) => {
        event.stopPropagation();
    });

    overlay.addEventListener('click', () => {
        exportDropdown.classList.remove('show');
        overlay.classList.remove('show');
    });
});



