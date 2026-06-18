/* ==========================================================
   DASHBOARD.JS
   ==========================================================
   Fetches category totals from our Django JSON endpoint
   (/api/chart-data/) and draws a pie chart with Chart.js.
   This is the JS-talks-to-Django piece that makes this a
   full-stack feature rather than a plain server-rendered page.
   ========================================================== */

const LEDGER_COLORS = [
    '#2F5D4F', '#B5562D', '#7A6A4F', '#5C7A8A',
    '#9C7A3C', '#6B5B95', '#4F6D5C', '#A85C5C'
];

async function loadChart() {
    try {
        const res = await fetch('/api/chart-data/');
        if (!res.ok) throw new Error('Failed to load chart data');
        const data = await res.json();

        if (!data.labels || data.labels.length === 0) return;

        const ctx = document.getElementById('categoryChart');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.totals,
                    backgroundColor: LEDGER_COLORS,
                    borderColor: '#FCFAF3',
                    borderWidth: 2,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                cutout: '62%',
            }
        });

        renderLegend(data.labels, data.totals);
    } catch (err) {
        console.error('Chart load error:', err);
    }
}

function renderLegend(labels, totals) {
    const legendEl = document.getElementById('legendList');
    if (!legendEl) return;

    legendEl.innerHTML = labels.map((label, i) => `
        <div class="legend-item">
            <span class="legend-dot" style="background:${LEDGER_COLORS[i % LEDGER_COLORS.length]}"></span>
            <span class="legend-label">${label}</span>
            <span class="legend-value">&#8377;${totals[i].toFixed(2)}</span>
        </div>
    `).join('');
}

loadChart();
