document.addEventListener('DOMContentLoaded', () => {
    const deleteLinks = document.querySelectorAll('a[href*="delete"]');
    deleteLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            if (!confirm('Você tem certeza que deseja excluir este item?')) {
                event.preventDefault();
            }
        });
    });
});
