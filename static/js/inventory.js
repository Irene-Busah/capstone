document.addEventListener('DOMContentLoaded', function () {
    const inventoryVsConsumptionCtx = document.getElementById('inventoryVsConsumptionChart').getContext('2d');
    const inventoryVsConsumptionChart = new Chart(inventoryVsConsumptionCtx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: []
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
                    display: false,
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

    // Fetch data and update the chart
    fetch('/api/inventory-purchase-rate/')
        .then(response => response.json())
        .then(data => {
            // Check if the data is in the expected structure, otherwise log and return
            if (!Array.isArray(data)) {
                console.error('Data received is not an array:', data);
                return;
            }

            const categories = data.map(d => d.category);
            const turnoverRates = data.map(d => d.turnover_rate);
            const purchaseRates = data.map(d => d.acquisition_rate);

            // Update chart
            inventoryVsConsumptionChart.data.labels = categories;
            inventoryVsConsumptionChart.data.datasets = [
                {
                    label: 'Turnover Rates',
                    data: turnoverRates,
                    backgroundColor: '#00AF54',
                    borderRadius: 8,
                    borderWidth: 1,
                    barThickness: 30,
                },
                {
                    label: 'Purchase Rates',
                    data: purchaseRates,
                    backgroundColor: '#B8E716',
                    borderRadius: 8,
                    borderWidth: 1,
                    barThickness: 30,
                }
            ];
            inventoryVsConsumptionChart.update();

            // Update the custom legend
            generateCustomLegend(inventoryVsConsumptionChart);
        })
        .catch(error => console.error('Error fetching inventory and purchase rates:', error));
});



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

generateCustomLegend(inventoryVsConsumptionChart);
