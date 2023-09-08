// Função para excluir uma tarefa
function deleteTarefa(tarefaId) {
     // Envia uma requisição POST para o servidor para excluir a tarefa com o ID especificado
    fetch("/delete-Tarefa", {
        method: "POST",
        body: JSON.stringify({tarefaId: tarefaId}), // Envio do ID da tarefa como JSON
    }).then(() => {
        // Após a conclusão da exclusão, redireciona o usuário de volta para a página inicial
        window.location.href = "/"
    });
}

// Função para lidar com a alteração no dropdown de filtro
document.getElementById('filtro').addEventListener('change', function () {
    var filtro = this.value; // Obtém o valor selecionado no dropdown de filtro
    var tarefas = document.getElementById('tarefas').getElementsByTagName('li'); // Obtém todos os elementos <li> dentro da div com ID 'tarefas'
    
    // Esconde todos os itens
    for (var i = 0; i < tarefas.length; i++) {
        tarefas[i].style.display = 'none';
    }
    
    // Mostra os itens correspondentes ao filtro selecionado
    if (filtro === 'todos') {
        // Se 'todos' estiver selecionado, mostra todos os itens de tarefa definindo seu estilo de exibição como 'block'
        for (var i = 0; i < tarefas.length; i++) {
            tarefas[i].style.display = 'block';
        }
    } else {
        // Se um filtro específico estiver selecionado, mostra apenas os itens de tarefa que correspondem ao status do filtro
        for (var i = 0; i < tarefas.length; i++) {
            var status = tarefas[i].getAttribute('data-status'); // Obtém o atributo 'data-status' de cada elemento
            if (status == filtro) {
                tarefas[i].style.display = 'block'; // Mostra o item se corresponder ao filtro
            }
        }
    }
});

