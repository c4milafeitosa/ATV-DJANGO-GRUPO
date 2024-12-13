document.addEventListener('DOMContentLoaded', () => {
    // Adiciona funcionalidade de pesquisa para todas as tabelas
    const searchInput = document.querySelector('#searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function () {
            const filter = searchInput.value.toLowerCase();
            const rows = document.querySelectorAll('table tbody tr');
            rows.forEach(row => {
                const cells = row.querySelectorAll('td');
                const match = Array.from(cells).some(cell => 
                    cell.textContent.toLowerCase().includes(filter)
                );
                row.style.display = match ? '' : 'none';
            });
        });
    }
});
