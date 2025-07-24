async function analyze() {
    const text = document.getElementById("textInput").value;
    const res = await fetch("/analyze", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ text: text })
    });
    const result = await res.json();
    document.getElementById("result").innerText =
        `Sentiment: ${result.label} (Score: ${result.score})`;
    loadChart();
}

async function loadChart() {
    const res = await fetch("/chart-data");
    const data = await res.json();

    const ctx = document.getElementById("myChart").getContext("2d");
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: 'Sentiment Count',
                data: Object.values(data),
                backgroundColor: ['green', 'red', 'blue']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                title: { display: true, text: 'Sentiment Distribution' }
            }
        }
    });
}
