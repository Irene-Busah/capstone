document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('consumptionRegionChart').getContext('2d');
    var consumptionRegionChart;
    var selectElement = document.getElementById('categorySelect'); // Assume this is the ID of your <select> element

    function drawChart(data, selectedCategory) {
        const categories = Object.keys(data);
        const regions = data[selectedCategory].map(item => item.region);
        const quantities = data[selectedCategory].map(item => item.total_quantity);

        if (consumptionRegionChart) {
            consumptionRegionChart.destroy(); // Destroy the old chart instance before creating a new one
        }

        consumptionRegionChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: regions,
                datasets: [{
                    label: selectedCategory,
                    data: quantities,
                    backgroundColor: '#B8E716',
                    borderColor: '#B8E716',
                    borderWidth: 1,
                    barThickness: 30,
                    borderRadius: 8,
                }]
            },
            options: {
                indexAxis: 'y', // Makes the chart horizontal
                scales: {
                    x: { // Configures the horizontal axis
                        grid: {
                            display: false // Hides the grid lines for the x-axis
                        },
                        beginAtZero: true // Starts the scale at zero
                    },
                    y: { // Configures the vertical axis (categories)
                        grid: {
                            display: false // Hides the grid lines for the y-axis
                        },
                        barPercentage: 0.8, // Sets the thickness of the bars
                        categoryPercentage: 1.0 // Sets the spacing between categories
                    }
                },
                plugins: {
                    legend: {
                        display: false // Hides the legend
                    }
                }
            }
        });
    }

    // Populate the select dropdown with categories and add event listener for changes
    function populateSelect(categories) {
        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.text = category;
            selectElement.appendChild(option);
        });

        selectElement.addEventListener('change', function () {
            const selectedCategory = this.value;
            fetch('/api/frequently-consumed-by-region/')
                .then(response => response.json())
                .then(data => {
                    drawChart(data, selectedCategory);
                })
                .catch(error => console.error('Error fetching data for selected category:', error));
        });
    }

    // Initial fetch to populate the chart and dropdown
    fetch('/api/frequently-consumed-by-region/')
        .then(response => response.json())
        .then(data => {
            const categories = Object.keys(data);
            populateSelect(categories); // Populate the select dropdown with categories
            drawChart(data, categories[0]); // Draw the chart with the first category by default
        })
        .catch(error => console.error('Error fetching inventory and purchase rates:', error));
});
