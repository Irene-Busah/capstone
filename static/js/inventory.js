document.addEventListener('DOMContentLoaded', function () {
    const inventoryVsConsumptionCtx = document.getElementById('inventoryVsConsumptionChart').getContext('2d');
    let inventoryVsConsumptionChart;

    function drawChart(data) {
        const categories = Object.keys(data);
        const turnoverRates = categories.map(category => data[category].turnover_rate);
        const purchaseRates = categories.map(category => data[category].purchase_rate);

        if (inventoryVsConsumptionChart) {
            inventoryVsConsumptionChart.destroy(); // Destroy the old chart instance before creating a new one
        }
        inventoryVsConsumptionChart = new Chart(inventoryVsConsumptionCtx, {
            type: 'bar',
            data: {
                labels: categories,
                datasets: [{
                    label: 'Turnover Rates',
                    data: turnoverRates,
                    backgroundColor: '#00AF54',
                    borderRadius: 8,
                    borderWidth: 1,
                    barThickness: 30,
                }, {
                    label: 'Purchase Rates',
                    data: purchaseRates,
                    backgroundColor: '#B8E716',
                    borderRadius: 8,
                    borderWidth: 1,
                    barThickness: 30,
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                hover: {
                    mode: 'index',
                    intersect: false,
                    onHover: (event, chartElement) => {
                        event.native.target.style.cursor = chartElement[0] ? 'pointer' : 'default';
                    }
                },
                plugins: {
                    legend: {
                        display: false, // Set to false to hide the default Chart.js legend
                        position: 'top',
                        align: 'end',
                        labels: {
                            usePointStyle: true,
                            pointStyle: 'circle',
                            padding: 20
                        }
                    },
                    tooltip: {
                        mode: 'index',
                        intersect: false,
                        backgroundColor: '#000'
                    }
                },
            }
        });


        // Update the custom legend
        generateCustomLegend(inventoryVsConsumptionChart);
    }

    // Function to add/update custom legend
    function generateCustomLegend(chart) {
        const legendContainer = document.getElementById('turnover-legend-container');
        legendContainer.innerHTML = chart.data.datasets.map((dataset, index) => {
            return `
                <div class="legend-item">
                    <span class="legend-color" style="background-color: ${dataset.backgroundColor};"></span>
                    <span class="legend-label">${dataset.label}</span>
                </div>
            `;
        }).join('');
    }

    // Fetch data and initialize the chart
    fetch('/api/inventory-purchase-rate/')
        .then(response => response.json())
        .then(data => {
            drawChart(data);
        })
        .catch(error => console.error('Error fetching inventory and purchase rates:', error));
});
